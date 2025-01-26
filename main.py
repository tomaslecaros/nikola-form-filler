import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from slider_function import update_slider

# Leer datos desde el archivo JSON con codificación UTF-8
with open("form_data.json", "r", encoding="utf-8") as f:
    FORM_CASES = json.load(f)

with open("locators.json", "r", encoding="utf-8") as f:
    LOCATORS = json.load(f)

# Configuración del navegador
driver = webdriver.Chrome()

# Iterar sobre cada caso en FORM_CASES
for case in FORM_CASES:
    # Navegar a la página
    driver.get("https://nikola.cl/empecemos")
    time.sleep(2)  # Esperar a que la página cargue completamente

    # Completar los campos del formulario
    # Nombre Completo
    name_field = driver.find_element(By.NAME, LOCATORS["name_field"])
    name_field.clear()
    name_field.send_keys(case["name"])

    # Correo Electrónico
    email_field = driver.find_element(By.NAME, LOCATORS["email_field"])
    email_field.clear()
    email_field.send_keys(case["email"])

    # Teléfono
    phone_field = driver.find_element(By.NAME, LOCATORS["phone_field"])
    phone_field.clear()
    phone_field.send_keys(case["phone"])

    # Dirección
    address_field = driver.find_element(By.NAME, LOCATORS["address_field"])
    address_field.clear()
    address_field.send_keys(case["address"])
    time.sleep(2)
    address_field.send_keys(Keys.ARROW_DOWN)
    address_field.send_keys(Keys.ENTER)

    # Tipo de Instalación (Dropdown)
    dropdown = Select(driver.find_element(By.NAME, LOCATORS["installation_type_dropdown"]))
    dropdown.select_by_visible_text(case["installation_type"])

    # Slider
    desired_value = case["desired_value"]
    slider_value, tooltip_value = update_slider(driver, desired_value)
    print(f"Nuevo valor del slider: {slider_value}")
    print(f"Nuevo valor del tooltip: {tooltip_value}")

    # Cómo nos encontraste (Dropdown)
    dropdown_found_us = Select(driver.find_element(By.NAME, LOCATORS["found_us_dropdown"]))
    dropdown_found_us.select_by_visible_text(case["found_us"])

    # Subir un archivo
    file_path = os.path.abspath(case["file_path"])
    file_input = driver.find_element(By.NAME, LOCATORS["slider_input"])
    file_input.send_keys(file_path)

    print(f"Archivo '{file_path}' subido correctamente para {case['name']}.")

    # Esperar antes de procesar el siguiente caso
    time.sleep(2)

# Cerrar el navegador después de procesar todos los casos
driver.quit()
