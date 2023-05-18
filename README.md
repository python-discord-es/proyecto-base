# Estructura básica de un proyecto

El repositorio contiene elementos para poder configurar y estructurar
un proyecto base con Python para generar un módulo para distribuir.

## Estructura proyecto base

La idea de esta estructura, es poder generar un módulo de Python con cierta
funcionalidad para ser distribuido a través de PyPi.

En este ejemplo, se considera:
* documentación,
* tests,
* construcción del módulo
* módulo con funcionalidad

El siguiente es una estructura de los archivos y directorios:

```
.
├── LICENSE
├── README.md
├── docs
├── mimodulo
│   ├── __init__.py
│   └── matematicas.py
├── pyproject.toml
├── requirements.txt
└── tests
    └── test_matematicas.py

```

Es importante destacar que `LICENSE` dependerá de la licencia que el proyecto
sea liberado, y `README.md` incluirá todas las notas necesarias para que las
personas puedan entender como instalar, contribuir, y utilizar el módulo.

En este caso un módulo de prueba llamado `mimodulo` es utilizado,
que contiene un archivo con funciones en `matematicas.py`.

El archivo `pyproject.toml` reemplaza al típico archivo `setup.py` que podrías
conocer, y es necesario para generar paquetes Python (wheels), que luego pueden
ser instalados con `pip`.

Para empaquetar el módulo, solo es necesario ejecutar `python -m build` en
la raíz del proyecto.

## Documentación

En esta situación, utilizaremos `sphinx` como herramienta para crear
la documentación.

Creamos un directorio llamado `docs` y comenzamos el script de sphinx para
crear un nuevo proyecto:

```
sphinx-quickstart docs/
```

Luego, dentro del directorio, y habiendo escrito toda la documentación de tu
código, podemos ejecutar

```
sphinx-apidoc  -o source ../mimodulo
```

para generar archivos `rst` con el contenido.

Es importante modificar un poco el archivo `docs/source/conf.py` para poder (1)
importar el módulo sin tenerlo instalado, y (2) generar automáticamente la
documentación de las funciones. Para ello podemos agregar algunos extensiones
como:

```
'sphinx.ext.doctest',
'sphinx.ext.autodoc',
'sphinx.ext.autosummary',
```

## Pruebas (Testing)

Para realizar los tests, utilizaremos `pytest`.
Al crear un directorio llamado `tests`, tendremos la posibilidad de ejecutar
`python -m pytest` en la raíz del proyecto, y que automáticamente los tests
sean ejecutados.

Dentro del directorio `tests` debes crear archivos de la forma
`test_<nombre>.py`, por ejemplo, si quisiera hacer un test de mi función
`calcular` podríamos crear un archivo `test_calcular.py` para poder escribir
los casos dentro.

Cada archivo, puede utilizar muchas funcionalidades que ofrece `pytest`
pero para tener una implementación simple, solo usaremos `assert` para
verificar que el resultado de algunas operaciones es el esperado.

Más información sobre `pytest` [acá](https://docs.pytest.org).


## Consejos generales y herramientas

Para el estilo y formato de tu código, existen muchas herramientas
de mucha utilidad, pero para comenzar puedes mirar principalmente
[black](https://www.tldrlegal.com/) para modificar tu código,
y [flake8](https://www.tldrlegal.com/) para ver mensajes de advertencia
relacionado al estilo.

Actualmente (2023), otras herramientas populares como
[ruff](https://www.tldrlegal.com/) son recomendadas, puedes leer sobre ella
también.

## Motivación

Esta estructura es una plantilla bastante básica, para personas que quieran
comenzar a aprender, pero sin embargo, existen otras herramientas que ayudan
a comenzar proyectos con muchas más opciones y utilidades, como
[hatch](https://hatch.pypa.io/latest/) y [poetry](https://hatch.pypa.io/latest/).
