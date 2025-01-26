from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def upload_file(driver, locator, file_path):
    """
    Sube un archivo a través de un input type="file".

    Args:
        driver (WebDriver): Instancia de Selenium WebDriver.
        locator (str): Nombre del campo en el DOM.
        file_path (str): Ruta completa al archivo a subir.
    """
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, locator))
    )
    file_input.send_keys(file_path)
