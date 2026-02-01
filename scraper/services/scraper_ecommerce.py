# services/scraper_ecommerce.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Para Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scraper_ecommerce_website():
    # Configurar Selenium
    options = Options()
    options.add_argument('--headless')  # Ejecutar en modo headless
    options.add_argument('--no-sandbox')  # Requerido para algunos servidores
    options.add_argument('--disable-dev-shm-usage')  # Para evitar errores de memoria

    # 🔹 Aquí inicializamos correctamente `service`
    service = Service(ChromeDriverManager().install())

    # Para Chrome
    # Selenium Manager se encargará de descargar y gestionar el WebDriver
    #service = Service()  # No es necesario especificar el ejecutable
    driver = webdriver.Chrome(service=service, options=options)

    # Navegar al sitio web
    url = "https://webscraper.io/test-sites/e-commerce/allinone"
    driver.get(url)
    print(driver.title)  
# Esperar a que los elementos estén presentes
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "thumbnail"))
        )

        products = driver.find_elements(By.CLASS_NAME, "thumbnail")
        
        scraped_data = []
        for product in products:
            # 카드 내부에서 각각의 정보를 추출
            title_element = product.find_element(By.CSS_SELECTOR, "a.title")
            title = title_element.get_attribute("title")
            link = title_element.get_attribute("href")
            price = product.find_element(By.CSS_SELECTOR, "h4.price").text
            description = product.find_element(By.CSS_SELECTOR, ".description").text

            scraped_data.append({
                "title": title,
                "url": link,
                "price": price,
                "description": description
            })

    except Exception as e:
        print("Error al encontrar los elementos:", e)
        driver.quit()
        return []

    print("Scraped data:", scraped_data)  # Para depuración
    driver.quit()
    return scraped_data