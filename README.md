# proyecto-final-automation-testing-federico-carboni

## Descripción del proyecto

Framework de automatización de pruebas desarrollado como proyecto final del curso de Automation Testing. Combina pruebas de UI con Selenium WebDriver y pruebas de API con Requests, aplicando el patrón Page Object Model.

## Tecnologías utilizadas

- **Python 3.12** — Lenguaje de programación principal.
- **Pytest** — Framework de testing para descubrimiento, ejecución y generación de reportes.
- **Selenium WebDriver** — Automatización del navegador Chrome para pruebas de interfaz de usuario.
- **Requests** — Librería HTTP para pruebas de API REST.
- **pytest-html** — Plugin para generar reportes HTML autocontenidos con resultados de tests.
- **webdriver-manager** — Gestión automática del driver de Chrome (ChromeDriver) sin instalación manual.

## Estructura del proyecto

```
proyecto-final-automation-testing-federico-carboni/
├── pages/                  → Clases Page Object Model (login, inventory, cart, checkout)
├── tests/
│   ├── ui/                 → Tests de interfaz de usuario con Selenium
│   └── api/                → Tests de API REST con Requests
├── utils/                  → Módulos auxiliares (logger, data_loader)
├── data/                   → Archivos de datos de prueba (JSON y CSV)
├── reports/                → Reportes HTML generados (ignorado por git)
├── screenshots/            → Capturas en caso de fallo (ignorado por git)
├── conftest.py             → Fixtures y hooks globales de pytest
├── pytest.ini              → Configuración de pytest
└── requirements.txt        → Dependencias del proyecto
```

## Instalación

1. **Clonar el repositorio**

   ```bash
   git clone <url-del-repositorio>
   cd proyecto-final-automation-testing-federico-carboni
   ```

2. **Crear entorno virtual**

   ```bash
   python -m venv .venv
   ```

3. **Activar entorno virtual**

   - **macOS / Linux:**

     ```bash
     source .venv/bin/activate
     ```

   - **Windows:**

     ```bash
     .venv\Scripts\activate
     ```

4. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución de tests

```bash
# Todos los tests
pytest tests/ -v

# Solo tests de UI
pytest tests/ui/ -v -m ui

# Solo tests de API
pytest tests/api/ -v -m api

# Un test específico
pytest tests/ui/test_saucedemo.py::test_flujo_checkout_completo -v

# Tests parametrizados de login
pytest tests/ui/test_login_parametrizado.py -v
```

El reporte HTML se genera automáticamente en `reports/report.html`.

## Casos de prueba

### Tests de UI (saucedemo.com)

| Test | Descripción | Tipo |
|---|---|---|
| `test_login_exitoso` | Login con credenciales válidas y verificación del inventario | UI |
| `test_login_credenciales_invalidas` | Login con credenciales inválidas y verificación del mensaje de error | UI |
| `test_cantidad_productos_inventario` | Verifica que el inventario muestra exactamente 6 productos | UI |
| `test_agregar_producto_al_carrito` | Agrega un producto al carrito y verifica el badge | UI |
| `test_flujo_checkout_completo` | Flujo completo: login, agregar producto, checkout, confirmación | UI |
| `test_logout` | Verifica que el logout redirige a la página de login | UI |
| `test_login_parametrizado` | Login parametrizado con 4 usuarios desde JSON (2 exitosos, 2 con error) | UI |

### Tests de API (jsonplaceholder.typicode.com)

| Test | Descripción | Método HTTP |
|---|---|---|
| `test_get_post_by_id` | Obtener un post por ID y validar sus claves | GET |
| `test_get_all_posts` | Obtener todos los posts y verificar cantidad (100) | GET |
| `test_create_post` | Crear un nuevo post y validar los datos retornados | POST |
| `test_delete_post` | Eliminar un post y verificar respuesta vacía | DELETE |
| `test_get_posts_by_user_chained` | Obtener el primer usuario y luego filtrar sus posts | GET (encadenado) |

## Reportes

- El reporte HTML se genera automáticamente en `reports/report.html` al ejecutar `pytest`.
- Incluye el estado de cada test (PASSED / FAILED), duración y logs capturados.
- En caso de fallo, se adjunta automáticamente un screenshot en el reporte con ruta absoluta.
- El archivo de log detallado se genera en `reports/test_execution.log` con formato `YYYY-MM-DD HH:MM:SS [LEVEL] name: mensaje`.

## Patrones y decisiones de diseño

- **Page Object Model (POM):** Separa la lógica de localización e interacción con los elementos de la página de los tests, facilitando el mantenimiento y la reutilización de código.

- **Logout via JavaScript / Storage:** El logout se implementa limpiando `localStorage` y `sessionStorage` y navegando directamente a la URL de login, en lugar de usar el menú hamburguesa. Esto evita la inestabilidad causada por animaciones CSS no determinísticas en Chrome headless.

- **Esperas explícitas (WebDriverWait):** Se utiliza `WebDriverWait` con `expected_conditions` en lugar de `time.sleep()` para sincronización con la página, haciendo los tests más rápidos y confiables al adaptarse dinámicamente a los tiempos de carga.
