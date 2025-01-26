from selenium.webdriver.common.by import By

def monthly_average_account(driver, desired_value):
    desired_value_formatted = f"${desired_value:,}".replace(",", ".")  # Formatear el número como string para JS
    # Script para ejecutar en el navegador
    script = f"""
    var slider = document.querySelector('#gfrs_rangeslider_28 .noUi-handle');
    var inputHidden = document.querySelector('input[name="input_28"]');
    var connectBar = document.querySelector('#gfrs_rangeslider_28 .noUi-connect');
    var tooltip = document.querySelector('.noUi-tooltip');  // Seleccionar el tooltip
    var touchArea = document.querySelector('.noUi-touch-area');  // Seleccionar el touch area

    // Actualizar los valores en el HTML
    slider.setAttribute('aria-valuenow', '{desired_value}');
    slider.setAttribute('aria-valuetext', '{desired_value_formatted}');
    inputHidden.value = '{desired_value}';
    connectBar.style.transform = 'scale({desired_value / 1000000}, 1)';
    tooltip.innerHTML = '{desired_value_formatted}';  // Actualizar el contenido del tooltip

    // Agregar información al noUi-touch-area (opcional)
    touchArea.setAttribute('data-value', '{desired_value}');

    // Log de prueba
    console.log('Slider actualizado al valor: {desired_value}');
    """

    # Ejecutar el script en el navegador
    driver.execute_script(script)

    # Verificar y devolver el nuevo valor del slider
    slider_value = driver.find_element(By.CLASS_NAME, "noUi-handle").get_attribute("aria-valuenow")
    tooltip_value = driver.find_element(By.CLASS_NAME, "noUi-tooltip").text
