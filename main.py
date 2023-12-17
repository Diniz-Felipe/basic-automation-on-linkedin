from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

# Carregar variáveis de ambiente
load_dotenv()

# Obter credenciais do LinkedIn do arquivo .env
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Configuração inicial
base_url = 'https://www.linkedin.com'
search_query = 'Engenheiro de Software'  # Você pode ajustar conforme necessário

# Configurar o caminho para o geckodriver
chromedriver_path = './chrome'

# Inicializar o WebDriver
browser = webdriver.Chrome(executable_path=chromedriver_path)

# Navegar para a página de login
browser.get(base_url)
time.sleep(2)

# Preencher as informações de login e fazer login
email_elem = browser.find_element(By.ID, 'session_key')
password_elem = browser.find_element(By.ID, 'session_password')
submit_elem = browser.find_element(By.CLASS_NAME, 'sign-in-form__submit-btn')

email_elem.send_keys(email)
password_elem.send_keys(password)
submit_elem.click()

# Esperar o login ser concluído
time.sleep(7)

# Realizar a pesquisa por perfis
search_box = browser.find_element(By.XPATH, "//input[@placeholder='Pesquisar']") #search-global-typeahead__input
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Esperar pelos resultados da pesquisa
time.sleep(5)

# Coletar informações dos perfis
profile_links = browser.find_elements(By.XPATH, "//span[@class='name actor-name']")
for link in profile_links:
    profile_name = link.text
    print(f"Encontrado perfil: {profile_name}")

# Encerrar o navegador
browser.quit()
