import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from functions.monthly_average_account import monthly_average_account
from functions.installation_type import handle_installation_type
from functions.form_utils import fill_text_field, select_dropdown, upload_file, fill_address_field
import time

# Variable global para determinar si se envía el formulario o no
submit_form = False

def process_case(driver, case, locators):
    """
    Procesa un caso individual rellenando los campos del formulario.

    Args:
        driver (WebDriver): Instancia de Selenium WebDriver.
        case (dict): Datos del caso a procesar.
        locators (dict): Diccionario con los nombres de los elementos del DOM.
    """
    # Navegar a la página
    driver.get("https://nikola.cl/empecemos")

    # Completar los campos del formulario
    fill_text_field(driver, locators["name_field"], case["name"])
    fill_text_field(driver, locators["email_field"], case["email"])
    fill_text_field(driver, locators["phone_field"], case["phone"])
    fill_address_field(driver, locators["address_field"], case["address"])
    handle_installation_type(driver, case, locators)
    monthly_average_account(driver, case["desired_value"])
    select_dropdown(driver, locators["found_us_dropdown"], case["found_us"])
    upload_file(driver, locators["slider_input"], case["file_path"])


    # Enviar formulario si submit_form es True
    if submit_form:
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, locators["submit_button"])))
        submit_button.click()
        print("Formulario enviado con éxito")


def main():
    # Leer datos desde los archivos JSON
    with open("form_data.json", "r", encoding="utf-8") as f:
        FORM_CASES = json.load(f)

    with open("locators.json", "r", encoding="utf-8") as f:
        LOCATORS = json.load(f)

    # Configuración del navegador
    driver = webdriver.Chrome()

    try:
        # Iterar sobre cada caso en FORM_CASES
        for case in FORM_CASES:
            time.sleep(2)
            process_case(driver, case, LOCATORS)
            time.sleep(2)
    finally:
        # Cerrar el navegador después de procesar todos los casos
        driver.quit()

if __name__ == "__main__":
    main()
