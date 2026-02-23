# Extraction d'informations de produits sur Cdiscount avec Selenium
# Nécessite : pip install selenium
# Télécharger ChromeDriver correspondant à votre version de Chrome et placer dans le PATH

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configuration du navigateur (mode sans interface)
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Lien de recherche sur books.toscrape.com (site de test)
search_url = "https://books.toscrape.com/catalogue/category/books_1/index.html"

# Démarrer le navigateur
browser = webdriver.Chrome(options=chrome_options)
browser.get(search_url)

# Attendre le chargement de la page
browser.implicitly_wait(5)


# Récupérer les livres
products = browser.find_elements(By.CSS_SELECTOR, 'article.product_pod')


if not products:
    print("Aucun livre trouvé sur la page.")

for product in products:
    try:
        title = product.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
    except:
        title = "N/A"
    try:
        url = product.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('href')
    except:
        url = "N/A"
    try:
        price = product.find_element(By.CSS_SELECTOR, 'p.price_color').text
    except:
        price = "N/A"
    try:
        description = product.find_element(By.CSS_SELECTOR, 'p.instock.availability').text.strip()
    except:
        description = "N/A"
    print(f"Titre : {title}")
    print(f"URL : {url}")
    print(f"Prix : {price}")
    print(f"Disponibilité : {description}")
    print("-"*40)

browser.quit()
