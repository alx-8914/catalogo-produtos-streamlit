import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pyodbc
import uuid
import json
from dotenv import load_dotenv
load_dotenv()

blobConnectionString = os.getenv('BLOB_CONNECTION_STRING')
blobContainerName = os.getenv('BLOB_CONTAINER_NAME')
blobaccountName = os.getenv('BLOB_ACCOUNT_NAME')

SQL_SERVER = os.getenv('SQL_SERVER')
SQL_DATABASE = os.getenv('SQL_DATABASE')
SQL_USER = os.getenv('SQL_USER')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')

st.title('Cadastro de Produtos')

#Fomulário de cadastro de produtos
product_name = st.text_input('Nome do Produto')
product_price = st.number_input('Preço do Produto', min_value=0.0, format='%.2f')
product_description = st.text_area('Descrição do Produto')
product_image = st.file_uploader('Imagem do Produto', type=['jpg', 'png', 'jpeg'])

#Salve on blob image storage
def upload_blob(file):
  blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
  container_client = blob_service_client.get_container_client(blobContainerName)
  blob_name = str(uuid.uuid4()) + file.name
  blob_client = container_client.get_blob_client(blob_name)
  blob_client.upload_blob(file.read(), overwrite=True)
  image_url = f"https://{blobaccountName}.blob.core.windows.net/{blobContainerName}/{blob_name}"
  return image_url

def insert_product(product_name, product_price, product_description, product_image):
    try:
        imagem_url = upload_blob(product_image)

        conn_str = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={SQL_SERVER};'
            f'DATABASE={SQL_DATABASE};'
            f'UID={SQL_USER};'
            f'PWD={SQL_PASSWORD};'
            'TrustServerCertificate=yes;'
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        insert_sql = """
            INSERT INTO Products (nome, preco, descricao, imagem_url)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_sql, (product_name, product_price, product_description, imagem_url))
        conn.commit() 
        conn.close()

        return True  
    except Exception as e:
        st.error(f"Erro ao inserir produto: {e}")
        return False

def list_products():
  try:
    conn_str = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={SQL_SERVER};'
        f'DATABASE={SQL_DATABASE};'
        f'UID={SQL_USER};'
        f'PWD={SQL_PASSWORD};'
        'TrustServerCertificate=yes;'
    )
    conn = pyodbc.connect(conn_str)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return rows
  except Exception as e:
    st.error(f"Erro ao listar produtos: {e}")
    return []

  
def list_products_screen():
  products = list_products()
  if products:
    cards_por_linha = 3
    cols = st.columns(cards_por_linha)
    for i, product in enumerate(products):
      col = cols[i % cards_por_linha]
      with col:
        st.markdown(f"### {product[1]}")
        st.write(f"**Descrição:** {product[2]}")  
        st.write(f"**Preço:** R$ {product[3]:.2f}")  
        if product[4]:  
          html_img = f'<img src="{product[4]}" alt="Imagem do Produto" width="200" height="200">'
          st.markdown(html_img, unsafe_allow_html=True)
        st.markdown("---")
      if (i + 1) % cards_por_linha == 0 and i + 1 < len(products):
        cols = st.columns(cards_por_linha)
  else:
    st.info('Nenhum produto encontrado.')

      
  
if st.button('Cadastrar Produto', key='btn_cadastrar'):
    sucesso = insert_product(product_name, product_price, product_description, product_image)
    if sucesso:
        st.success('✅ Produto cadastrado com sucesso!')
        st.balloons()  # 🎈 animação bacana!

    else:
        st.error('❌ Ocorreu um erro ao cadastrar o produto.')

if st.button('Listar Produtos', key='btn_listar'):
  list_products_screen()
  return_message = 'Produtos listados com sucesso!'