from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def handle_installation_type(driver, case, locators):
    # Seleccionar el tipo de instalación del primer dropdown
    select_dropdown_by_text(driver, "installation_type", case["installation_type"], locators)

    if case["installation_type"] == "Carport":
        # Manejo de dropdown para Carport
        select_dropdown_by_text(driver, "roof_type_detail", case["roof_type_detail"], locators)
        if case["roof_type_detail"] == "Otro":
            handle_other_input(driver, case, locators)

    elif case["installation_type"] == "Techo":
        # Manejo de dropdown para Techo
        select_dropdown_by_text(driver, "roof_type", case["roof_type"], locators)
        select_dropdown_by_text(driver, "roof_type_detail", case["roof_type_detail"], locators)
        if case["roof_type_detail"] == "Otro":
            handle_other_input(driver, case, locators)
            

def select_dropdown_by_text(driver, locator_name, value, locators):
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, locators[locator_name]))
    )
    Select(dropdown).select_by_visible_text(value)

def handle_other_input(driver, case, locators):
    if "other_detail" in case:
        other_input = driver.find_element(By.NAME, locators["other_installation_detail"])
        other_input.clear()
        other_input.send_keys(case["other_detail"])

