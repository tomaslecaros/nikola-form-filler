from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def fill_text_field(driver, locator, value):

    """
    Limpia y rellena un campo de texto.

    Args:
        driver (WebDriver): Instancia de Selenium WebDriver.
        locator (str): Nombre del campo en el DOM.
        value (str): Valor que se ingresará en el campo.
    """
    field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, locator))
    )
    field.clear()
    field.send_keys(value)

def select_dropdown(driver, locator, value):
    """
    Selecciona una opción de un dropdown por texto visible.

    Args:
        driver (WebDriver): Instancia de Selenium WebDriver.
        locator (str): Nombre del campo en el DOM.
        value (str): Valor que se seleccionará en el dropdown.
    """
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, locator))
    )
    Select(dropdown).select_by_visible_text(value)

def upload_file(driver, locator, relative_file_path):
    """
    Sube un archivo a través de un input type="file".

    Args:
        driver (WebDriver): Instancia de Selenium WebDriver.
        locator (str): Nombre del campo en el DOM.
        relative_file_path (str): Ruta relativa del archivo a subir.
    """
    # Convertir la ruta relativa a absoluta
    file_path = os.path.abspath(relative_file_path)

    # Esperar a que el campo de archivo esté presente
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, locator))
    )

    # Subir el archivo
    file_input.send_keys(file_path)

def fill_address_field(driver, field_name, address):
    """
    Rellena el campo de dirección, espera a que aparezcan sugerencias y selecciona la primera opción.

    Args:
        driver (WebDriver): Instancia de Selenium WebDriver.
        field_name (str): Nombre del campo de dirección (atributo NAME).
        address (str): Dirección a ingresar.
    """
    # Esperar a que el campo sea visible y clickeable
    address_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, field_name))
    )

    # Limpiar y rellenar el campo
    address_field.clear()
    address_field.send_keys(address)

    # Esperar un momento para que se carguen las sugerencias
    time.sleep(2)

    # Seleccionar la primera sugerencia
    address_field.send_keys(Keys.ARROW_DOWN)
    address_field.send_keys(Keys.ENTER)
    
def send_form(driver, submit_button_id):
    """
    Envía el formulario haciendo clic en el botón de envío.

    Args:
        driver (WebDriver): Instancia de Selenium WebDriver.
        submit_button_id (str): ID del botón de envío en el formulario.
    """
    # Esperar a que el botón de envío sea interactuable
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, submit_button_id))
    )

    # Hacer clic en el botón de envío
    submit_button.click()
    print("Formulario enviado con éxito.")


