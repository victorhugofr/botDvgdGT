import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time
import os

# Configuração do WebDriver
driver = uc.Chrome()

driver.delete_all_cookies()


def comment_on_shorts(comment_text, screenshot_dir="screenshots"):
    # Cria o diretório para salvar screenshots se não existir
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    # Navegar para a seção de "Shorts"
    screenshot_count=0
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    while True:
        try:
            time.sleep(30)
            # Localizar a área de comentário e comentar
            print(f"tentando clicar no botao escrever")
            comment_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='DraftEditor-editorContainer']/div")))
            comment_box.click()
            time.sleep(2)
            comment_box.send_keys(current_date+' '+comment_text)
            comment_box.send_keys(Keys.ENTER)
            time.sleep(3)
            screenshot_path = os.path.join(screenshot_dir, f"screen_{current_date}_shot_{screenshot_count}.png")
            driver.save_screenshot(screenshot_path)
            screenshot_count += 1
            print(f"Comentário salvo e captura de tela tirada: {screenshot_path}")
            if(screenshot_count==35):
                break

            # Passar para o próximo vídeo
            next_button = driver.find_element(By.XPATH, "//*[@aria-label='Ir para o próximo vídeo']")
            next_button.click()
            time.sleep(10)
        except Exception as e:
            print(f"Erro: {e}")
            time.sleep(80)
            break

try:
    # Navegar para o YouTube
    driver.get("https://www.tiktok.com/explore")
    driver.maximize_window()
    
    # Esperar a página carregar
    time.sleep(80)
    # Obter a data atual
    current_date = datetime.now().strftime("%d-%m-%Y %H:%M")
    comment_on_shorts(f"GTA Torcidas é um server SA-MP onde simulamos a vida de um torcedor organizado, venha jogar conosco. https://taplink.cc/gta.torcidas")
finally:
    driver.quit()
