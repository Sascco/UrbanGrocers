Proyecto Sprint 6
Autor:
Sergio Solano Céspedes

QA Engineer - Cohorte 8

Tripleten

Acerca del proyecto:
Con este proyecto, estamos automatizando las pruebas pruebas que se deben hacer para el campo '''name''', en la solicitud de creación de un kit de productos.

Encontrarás lo necesario en 4 archivos, configuration.py, create_kit_name_kit_test.py, data.py, sender_stand_request.py, posteriormente, tendrás la información de cada uno de los archivos.

Con este proyecto, quiero exponerte lo que he aprendido en este bootcamp acerca de manejo de API's, Casos de Pruebas, Linea de Comandos y manejo de Librerias en Python.

Para mas información, abre la documentación para estudiar la API de la aplicación de Urban Grocers: /docs/

API Reference
endpoint para crear una kit de una tarjeta específica O de usuario.

Es obligatorio pasar el encabezado Authorisation O el parámetro cardId, para crear la kit

Si se recibe una solicitud con un encabezado Authorisation que contenga el authToken de un/a usuario/a en particular - se creará la kit de este/a usuario/a.

Si se recibe el parámetro cardId, se creará una kit dentro de la tarjeta correspondiente

Si no se pasa ninguno de los parámetros, se devolverá un error.

Cuando se pasan ambos parámetros, Authorization es la prioridad

  POST /api/v1/kits
Parameter	Type	Description
Authorization*	string	Encabezado de autorización en formato Bearer {authToken}. Cuando se pasa - se devuelven todos las cestas creadas por el/la usuario/a.
Content-Type*	string 	Valor por defecto: application/json
*Opcional

Tecnologías
PYTHON

La instalación de Python varía un poco según el sistema operativo que estés utilizando. A continuación, te presento los pasos para instalar Python en Windows, macOS y Linux:

En Windows:

Descarga el instalador de Python: Accede al sitio web oficial de Python https://www.python.org/downloads/ y descarga el instalador para tu sistema operativo (32 o 64 bits).

Ejecuta el instalador: Una vez descargado, ejecuta el instalador y sigue las instrucciones en pantalla. Asegúrate de seleccionar la opción "Agregar Python 3 a la ruta" durante la instalación.

Verifica la instalación: Abre una terminal o ventana de comandos y escribe python --version. Si la instalación fue correcta, debería mostrar la versión de Python instalada.

En macOS:

Descarga el instalador de Python: Accede al sitio web oficial de Python https://www.python.org/downloads/ y descarga el instalador para macOS.

Instalar Python usando hdiutil: Abre una terminal y navega hasta la carpeta donde descargaste el instalador de Python. Luego, ejecuta el siguiente comando:

hdiutil mount Python-3.x.x.dmg Reemplaza 3.x.x con la versión de Python que descargaste.

Ejecuta el instalador: Abre la imagen montada y ejecuta el instalador dentro de ella. Sigue las instrucciones en pantalla.

Desmonta la imagen: Una vez finalizada la instalación, desmonta la imagen usando el siguiente comando:

hdiutil unmount /Volumes/Python\ 3.x.x Verifica la instalación: Abre una terminal y escribe python --version. Si la instalación fue correcta, debería mostrar la versión de Python instalada. En Linux:

Utiliza el gestor de paquetes de tu distribución: La forma específica de instalar Python puede variar según la distribución de Linux que estés utilizando. Sin embargo, en general, puedes usar el siguiente comando: sudo apt install python3 # Debian/Ubuntu sudo yum install python3 # CentOS/RHEL sudo dnf install python3 # Fedora Verifica la instalación: Abre una terminal y escribe python3 --version. Si la instalación fue correcta, debería mostrar la versión de Python instalada.

PYTEST

Existen dos métodos principales para instalar pytest:

Mediante pip:
pip es el administrador de paquetes estándar para Python. Para instalar pytest con pip, abre una terminal o ventana de comandos y ejecuta el siguiente comando:

pip install pytest Este comando descargará e instalará pytest y sus dependencias en tu entorno de Python.

Utilizando un entorno virtual:
Se recomienda usar un entorno virtual para aislar las dependencias de tu proyecto. Para crear un entorno virtual y luego instalar pytest en él, puedes seguir estos pasos:

Para Windows:

Instala venv: https://docs.python.org/3/tutorial/venv.html si aún no lo has hecho. Puedes hacerlo ejecutando el siguiente comando en una terminal o ventana de comandos con privilegios de administrador:

python -m venv <nombre_entorno_virtual>

Activa el entorno virtual:

<nombre_entorno_virtual>\Scripts\activate Instala pytest dentro del entorno virtual: pip install pytest

Para macOS o Linux:

Crea el entorno virtual:

python3 -m venv <nombre_entorno_virtual>

Activa el entorno virtual: source <nombre_entorno_virtual>/bin/activate

Instala pytest dentro del entorno virtual:

pip install pytest

Verificación de la instalación:

Una vez que hayas instalado pytest, puedes verificar que la instalación se haya realizado correctamente ejecutando el siguiente comando en tu terminal o ventana de comandos:

pytest --version Este comando debería mostrar la versión de pytest que has instalado.

Librerias
REQUEST:

La librería Requests en Python es una herramienta poderosa para realizar peticiones HTTP y trabajar con APIs. Su uso simplifica la interacción con servidores web y la obtención de datos de diversas fuentes.

A continuación, te presento una guía básica sobre cómo usar la librería Requests en Python:

Instalación:
Asegúrate de tener Python instalado en tu sistema. Luego, puedes instalar la librería Requests utilizando el siguiente comando en tu terminal o ventana de comandos:

pip install requests

Importación:
Para usar la librería Requests en tu código Python, debes importarla al inicio de tu script. Puedes hacerlo de la siguiente manera:

Python import requests

Realizar una petición GET:
El método más común para obtener datos de un servidor web es mediante una petición GET. Para realizar una petición GET con Requests, utiliza la siguiente sintaxis:

Python

response = requests.get('https://ejemplo.com/api/datos')

En este ejemplo, se realiza una petición GET a la URL https://ejemplo.com/api/datos. La respuesta a la petición se almacena en la variable response.

Verificar la respuesta:
La variable response contiene información sobre la petición realizada y la respuesta recibida del servidor. Puedes acceder a esta información utilizando los siguientes atributos:

response.status_code: Código de estado HTTP de la respuesta (por ejemplo, 200 para éxito, 404 para no encontrado). response.headers: Diccionario con los encabezados de la respuesta. response.text: Texto de la respuesta en formato de cadena.

response.json(): Decodifica el JSON de la respuesta en un objeto de Python. Para verificar si la petición fue exitosa, puedes verificar el código de estado:

Python

if response.status_code == 200: print('Petición exitosa!') else: print('Error:', response.status_code) Use code with caution. content_copy

Procesar el contenido de la respuesta:
Dependiendo del formato del contenido de la respuesta, puedes procesarlo de diferentes maneras:

Texto: Si el contenido es texto plano, puedes acceder a él directamente como response.text. JSON: Si el contenido es JSON, puedes decodificarlo a un objeto de Python usando response.json(). Binario: Si el contenido es binario (por ejemplo, una imagen), puedes acceder a él como response.content.

Realizar otros tipos de peticiones:
Requests también permite realizar otros tipos de peticiones HTTP, como POST, PUT y DELETE. La sintaxis es similar a la de una petición GET, pero con algunos cambios:

POST: Envía datos al servidor. Se utiliza para crear o actualizar recursos. PUT: Actualiza un recurso existente en el servidor. DELETE: Elimina un recurso del servidor. Para más información sobre la sintaxis y el uso de estas peticiones, consulta la documentación oficial de Requests: https://requests.readthedocs.io/

Como ejecutar las pruebas:
Para ejecutar las pruebas que has proporcionado en la terminal, puedes seguir estos pasos:

Instalar pytest:
Si aún no lo has hecho, necesitas instalar la librería pytest para poder ejecutar pruebas unitarias en Python. Puedes instalarla usando el siguiente comando en tu terminal o ventana de comandos:

pip install pytest

Guardar el código de prueba:
Copia el código de prueba que has proporcionado en un archivo de Python. Puedes llamarlo test_kit_creation.py o cualquier otro nombre que consideres adecuado.

Navegar al directorio del archivo:
Abre una terminal o ventana de comandos y navega hasta el directorio donde guardaste el archivo de prueba (test_kit_creation.py). Puedes usar el comando cd para cambiar de directorio.

Ejecutar las pruebas:
Para ejecutar todas las pruebas en el archivo test_kit_creation.py, puedes usar el siguiente comando:

pytest

Este comando ejecutará todas las funciones que comiencen con la palabra test en el archivo.

Ejecutar pruebas específicas:
Si deseas ejecutar solo una prueba específica, puedes usar su nombre después del comando pytest. Por ejemplo, para ejecutar la prueba test_create_user_positive_1_letter, puedes usar:

pytest test_create_user_positive_1_letter

Ver los resultados:
Al ejecutar las pruebas, pytest mostrará un resumen de los resultados en la terminal. Deberás ver algo como esto:

collected 2 items

test_kit_creation.py . . . . . . . . . . . . . . [PASS]

test_kit_creation.py . . . . . . . . . . . . [PASS]

2 passed in 0.02s (visited 2) Esto indica que ambas pruebas se han ejecutado correctamente. Si alguna prueba falla, pytest mostrará un mensaje de error con más detalles sobre el error.

Lista de Pruebas
1 El número permitido de caracteres (1): kit_body = { "name": "a"}

2 El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}

3 El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }

4 El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }

5 Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }

6 Se permiten espacios: kit_body = { "name": " A Aaa " }

7 Se permiten números: kit_body = { "name": "123" }

8 El parámetro no se pasa en la solicitud: kit_body = None

9 Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }

Data
En el archivo data.py encontrarás la información necesaria para la creación del usuario User_body nombre, telefono, y dirección.

También encontrarás la información para usar en cada una de las pruebas en un diccionario.

Configuración
En el archivo <configuration.py> encontrarás la dirección URL del servidor en el cual se van a ejecutar las pruebas de acuerdo a los requerimientos.

Adicionalmente, podras identificar las rutas para crear Usuarios y Kits..

Creación de Kit
En el archivo create_kit_name_kit_test.py vas a encontrar el código que se elaboró para automatizar las pruebas.

Inicialmente, se importa la información del archivo sender_stand_request y data de acuerdo a los requerimientos.

Se establecen las funciones que se requieren para ejecutar las pruebas automotizadas.

Creación de Usuario
Se importa la información de los archivos configuration, requests y data

Están las funciones para crear un usuario, que permite generar el token de autenticación.

Contribuciones
Haz la diferencia en el mundo del software contribuyendo a nuestro proyecto de automatización de pruebas de código abierto. ¡Tu aporte es valioso!

Contribuciones son siempre bienvenidas.
