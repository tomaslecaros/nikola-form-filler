# Nikola Form Filler

Nikola Form Filler es un programa diseñado para automatizar el llenado de formularios en la página web `https://nikola.cl/empecemos` utilizando Selenium. Su objetivo principal es simplificar el proceso, haciéndolo escalable, legible y modular para facilitar futuras mejoras o adaptaciones.

El programa utiliza un archivo JSON como entrada, que contiene la información requerida para llenar los formularios. Además, permite procesar múltiples casos en una sola ejecución, iterando automáticamente sobre cada conjunto de datos. Esto lo hace ideal para manejar grandes volúmenes de formularios de manera eficiente y confiable.


---

## Requisitos previos

Antes de ejecutar el programa, asegúrate de tener instalados los siguientes componentes:

### 1. **Python**
   - Descarga e instala Python 3.10 o superior desde [Python.org](https://www.python.org/).

### 2. **Instalación de dependencias**
   - Ejecuta el siguiente comando para instalar las librerías necesarias:
     ```bash
     pip install selenium
     ```

### 3. **Google Chrome y ChromeDriver**
   - Asegúrate de tener instalado Google Chrome.
   
   - con lo anterior debería ser suficiente, si tienes errores descarga la versión de ChromeDriver correspondiente a tu versión de Chrome desde [ChromeDriver](https://sites.google.com/chromium.org/driver/).
   - Agrega el archivo `chromedriver` al `PATH` o coloca el ejecutable en la misma carpeta del script.


---

## Configuración

### 1. **Archivos JSON**
- **`form_data.json`**: Contiene ejemplos de datos que serían enviados al formulario. Para efectos prácticos, estos datos son correctos y cumplen con los requisitos de la página para evitar conflictos. Sin embargo, este proceso podría mejorarse implementando validaciones adicionales en el código para verificar la veracidad y la estructura de la data enviada.

Ejemplo del contenido:

```json
[
    {
        "name": "Ana Gómez",
        "email": "ana.gomez@example.com",
        "phone": "987654321",
        "address": "Avenida Siempre Viva 742, Springfield",
        "installation_type": "Techo",
        "roof_type": "Plano",
        "roof_type_detail": "Zinc",
        "found_us": "Facebook",
        "file_path": "Examples/receipt.jpg",
        "desired_value": 200000
    }
]
```

- **`locators.json`**: Contiene los selectores de los elementos HTML del formulario:

```json
{
    "name_field": "input_1.3",
    "email_field": "input_2",
    "phone_field": "input_5",
    "address_field": "input_20",
    "installation_type": "input_24",
    "roof_type": "input_25",
    "roof_type_detail": "input_26",
    "other_installation_detail": "input_29",
    "slider_input": "input_27",
    "found_us_dropdown": "input_34"
}
```
- **`main.py`**: Contiene el archivo principal el cual debe ser ejecutado. muy importante que tiene
una flag llamada `submit_form` que esta en `False` para no enviar los formularios y enviar data falsa.
Si se quiere enviar los formulario, es deccir, presionar el botón "Cotiza aquí" de la página web se debe cambiar a True el booleano.

- **`functions`**: 
---

## Cómo ejecutar el programa


   ```bash
   python main.py
   ```

---

## Funcionamiento del programa

1. El programa utiliza Selenium para automatizar el llenado de formularios en la página `https://nikola.cl/empecemos`.
2. Procesa cada caso definido en `form_data.json` y completa los campos según los datos proporcionados.
3. Las funciones auxiliares están organizadas en la carpeta `funciones` para manejar tareas específicas:
   - **`fill_text_field`**: Rellena campos de texto.
   - **`select_dropdown`**: Selecciona opciones de dropdown.
   - **`upload_file`**: Sube archivos.
   - **`handle_installation_type`**: Gestiona la selección de tipo de instalación ya que dependiendo de que se seleccione pueden aparecer mas dropdowns o inputs de texto.
   - **`update_slider`**: Ajusta el valor del slider según el valor deseado.
4. Las boletas utilizadas en este programa son imágenes de prueba incluidas para mostrar de manera práctica cómo se implementa la carga de archivos.
5. Después de completar el formulario, el navegador se cierra automáticamente o envia el formulario dependiendo de si se desea.

---

## Notas

- Si necesitas ajustar los selectores (no debería ser necesario) o agregar más, modifícalos directamente en `locators.json`.
- Asegúrate de que si quieres agregar mas ejemplos en `form_data.json` tenga la estructura que se muestra en los ejemplos y que coincida con la página de la empresa .

---

## Mejoras futuras

- Implementar validaciones automáticas en el código para verificar la veracidad y estructura de los datos enviados antes de procesarlos.
- Agregar manejo de errores más robusto para casos en los que los datos proporcionados no cumplan con los requisitos del formulario.



