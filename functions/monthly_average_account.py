from selenium.webdriver.common.by import By

def monthly_average_account(driver, desired_value):
    """
    Args:
        driver (WebDriver): Instancia de Selenium WebDriver.
        desired_value (int): Valor deseado para el slider.
    """
    # Ajustar el valor si está fuera del rango permitido
    if desired_value < 0:
        print(f"Valor deseado {desired_value} menor a 0, ajustando a 0.")
        desired_value = 0
    elif desired_value > 1000000:
        print(f"Valor deseado {desired_value} mayor a 1,000,000, ajustando a 1,000,000.")
        desired_value = 1000000

    # Formatear el número para el JavaScript
    desired_value_formatted = f"${desired_value:,}".replace(",", ".")  # Formato chileno para separadores

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
    touchArea.setAttribute('data-value', '{desired_value}');

    // Log de prueba
    console.log('Slider actualizado al valor: {desired_value}');
    """

    # Ejecutar el script en el navegador
    driver.execute_script(script)

