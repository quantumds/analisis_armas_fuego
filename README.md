# Análisis de Armas de Fuego

La siguiente es la entrega de la práctica 4 para la asignatura _Programación para la Ciencia de Datos_ del máster en Data Science de la UOC.

Hemos creado un paquete llamado `analisis_armas_fuego` que da respuesta a todas las preguntas de la práctica 4, excepto la última. El ejercicio 6 ha sido un reto y la única pregunta que no hemos sido capaces de compilar exitosamente en PyCharm, nuestro IDE favorito y el cual hemos utilizado para esta práctica. 

Toda la práctica se puede ejecutar a través del fichero `main.py`

Este fichero incorpora la cadena de ejecución de todas las preguntas de  la práctica. Hemos adaptado todas las funciones para que se ejecuten de manera escalonada, tal cual aparece en el enunciado. Además, hemos incluido mensajes por el canal estándar de salida que especifican la pregunta que se está resolviendo en cada momento. Incluso las teóricas.

Hemos también subido toda la práctica a nuestro repositorio `Git` que se puede encontrar en la URL: [https://github.com/quantumds/analisis_armas_fuego](URL) Éste ha sido el repositorio que he utilizado a lo largo de todo el máster para realizar las prácticas, contiene una batería de funciones Python compilada de más de 10 años de experiencia laboral en Data Science y universitaria. Se accede a través de índices de temática.

Hemos decidido subir toda la práctica a Git en caso de que existan problemas con el fichero `zip`

No es necesario especificar constantes o "hardcodear" (como se le conoce en el gremio a esta práctica) rutas específicas de nuestros ordenadores. En el mundo de la empresa privada esta es una pésima práctica que debe ser evitada a toda costa. Hemos utilizado la librería `Git`, `pathlib` y `subprocess` que automaticamente escanean el esqueleto de la estructura de directorios y de forma genérica nos dan la raiz de nuestro proyecto. De esta manera, lo podremos ejecutar siempre independientemente de la ubicación en el ordenador. 

Hemos respetado en todo momento la sintáxis PEP8, hemos hecho uso de Google Docstrings (nuestra forma preferida de escribir funciones en python) y también hemos incorporado _type hints en todas las funciones_.

Ahora, procedemos a dar paso por paso todas las indicaciones para ser capaz de ejecutar este proyecto Python y obtener nuestras respuestas a las preguntas planteadas.

## Pasos para ejecutar el proyecto

### Descargamos el proyecto
En el caso de que se quiera seguir la via de `Git` simplemente clonamos nuestro repo en el ordenador:
```
git clone https://github.com/quantumds/analisis_armas_fuego.git
cd analisis_armas_fuego
```

En el caso de que se quiera utilizar el archivo `zip` simplemente lo descomprimimos en la ubicación preferida en nuestro ordenador.

### Creamos y activamos el entorno virtual:

Instalamos el entorno virtual:
```
python3 -m venv venv
source venv/bin/activate
```

### Instalamos las dependencias:
Utilizamos el archivo `setup.py` para instalar las dependencias:
```
pip install .
```

### Ejecutamos el proyecto

Una vez habiendo seguido todos estos pasos, simplemente ejecutamos el fichero main el cual tiene todas las respuestas:
```
python main.py
```

### Licencia

Hemos escogido la licencia MIT pues es una excelente opción para un proyecto Python universitario que deseamos sea código libre.

La licencia MIT provee flexibilidad, fomento de la colaboración y simplicidad.

Entre sus rasgos más especiales podemos destacar los siguientes:

- A diferencia de otras licencias de código abierto, la MIT no impone restricciones estrictas sobre cómo se puede utilizar o distribuir el código.
- El texto de la licencia MIT es conciso y fácil de entender, lo que reduce la ambigüedad.
- La licencia MIT es compatible con muchas otras licencias de código abierto, lo que permite integrar fácilmente nuestro proyecto con otros componentes de software.
