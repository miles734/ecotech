# 🌱 EcoTech — Sistema de Gestión de Tiempos y Usuarios

EcoTech es una aplicación de consola desarrollada en Python, diseñada para facilitar la administración de usuarios, empleados, departamentos, proyectos y tiempos de trabajo dentro de una organización.

El sistema cuenta con una arquitectura modular por capas, autenticación mediante credenciales y control de acceso basado en roles, diferenciando las funcionalidades disponibles para administradores y empleados.

Además, incorpora herramientas complementarias como indicadores de desempeño, consulta de la cotización del dólar e historial de consultas de divisas.

## 🚀 Características principales

- **Autenticación de usuarios:** inicio de sesión mediante credenciales y validación segura.
- **Control de acceso por roles:** permisos diferenciados para administradores y empleados.
- **Gestión de empleados:** administración de la información del personal.
- **Gestión de departamentos:** organización y administración de las áreas de trabajo.
- **Gestión de proyectos:** creación y administración de proyectos.
- **Registro de tiempos:** seguimiento de las horas dedicadas a las actividades laborales.
- **Perfil de usuario:** visualización de la información personal de cada usuario.
- **Indicadores de desempeño:** consulta de métricas relacionadas con el rendimiento laboral.
- **Consulta del dólar:** obtención de información actualizada sobre la cotización de la divisa.
- **Historial de consultas:** almacenamiento y consulta de operaciones anteriores relacionadas con divisas.

## 🛠️ Tecnologías y requisitos

Para ejecutar correctamente EcoTech, se necesitan las siguientes herramientas:

- Python 3.10 o superior.
- pip (administrador de paquetes de Python).
- SQLite / MySQL, según la configuración del proyecto.
- Visual Studio Code (editor recomendado).
- Git (opcional, para clonar el repositorio).

## 📦 Instalación

Sigue los siguientes pasos para configurar y ejecutar EcoTech en tu equipo.

### 1. Acceder al directorio del proyecto

Abre una terminal y ejecuta:

```bash
cd ecotech-p.v
```

### 2. Crear un entorno virtual

Se recomienda utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar las dependencias

Con el entorno virtual activado, ejecuta:

```bash
pip install -r requirement.txt
```

### 4. Configurar las variables de entorno

Si deseas utilizar un archivo de configuración personalizado, puedes copiar el archivo de ejemplo.

**Windows:**

```powershell
copy .env.example .env
```

El archivo `.env.example` contiene la configuración inicial del proyecto y los parámetros necesarios para su ejecución.

## 📚 Dependencias de Python

EcoTech utiliza las siguientes librerías externas:

| Librería | Versión | Descripción |
|---|---|---|
| PyMySQL | 1.2.3 | Permite la conexión y comunicación con bases de datos MySQL. |
| python-dotenv | 1.2.3 | Facilita la lectura de variables de entorno desde archivos `.env`. |
| bcrypt | 5.0.0 | Permite generar hashes seguros para proteger las contraseñas de los usuarios. |

Estas dependencias se encuentran definidas en el archivo `requirement.txt`.

### Instalación individual

Si necesitas instalar las librerías manualmente, puedes utilizar los siguientes comandos:

```bash
pip install PyMySQL==1.2.3
pip install python-dotenv==1.2.3
pip install bcrypt==5.0.0
```

## 🧩 Extensiones recomendadas para Visual Studio Code

Para facilitar el desarrollo, mantenimiento y ejecución del proyecto, se recomienda instalar las siguientes extensiones:

| Extensión | Desarrollador | Funcionalidad |
|---|---|---|
| Python | Microsoft | Permite ejecutar y administrar proyectos Python. |
| Pylance | Microsoft | Ofrece autocompletado inteligente y detección de errores. |
| Python Debugger | Microsoft | Permite depurar y analizar la ejecución del código. |
| SQLite Viewer | Extensión de VS Code | Facilita la visualización y consulta de bases de datos SQLite. |
| DotENV | Extensión de VS Code | Proporciona reconocimiento y resaltado de archivos `.env`. |

### Instalación de extensiones

1. Abre Visual Studio Code.
2. Presiona `Ctrl + Shift + X`.
3. Busca cada extensión por su nombre.
4. Selecciona **Instalar**.

También puedes instalar las principales extensiones de Python desde la terminal:

```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-python.debugpy
```

Las extensiones de SQLite y DotENV pueden instalarse directamente desde el buscador de extensiones.

**Nota:** Las extensiones son herramientas recomendadas para el entorno de desarrollo y no son obligatorias para ejecutar la aplicación.

## ▶️ Ejecución del sistema

Una vez completada la instalación, inicia la aplicación desde el directorio principal:

```bash
python src/main.py
```

Al iniciar, el sistema prepara automáticamente la base de datos y genera los usuarios iniciales necesarios para realizar las primeras pruebas.

## 🔐 Credenciales de acceso

EcoTech incorpora usuarios iniciales para facilitar las pruebas de funcionamiento.

### Iniciar sesión como administrador
- Usuario: `admin`
- Contraseña: `admin123`

### Iniciar sesión como empleado
- Usuario: `ana`
- Contraseña: `ana123`

> Estas credenciales vienen creadas automáticamente al iniciar la aplicación por primera vez.

**Importante:** Estas credenciales son exclusivamente para pruebas. Se recomienda modificarlas antes de utilizar el sistema en un entorno real.

## 📁 Estructura del proyecto

El proyecto utiliza una organización modular que separa las responsabilidades de cada componente.

```text
ecotech-p.v/
│
├── src/
│   ├── dominio/          # Entidades y reglas del negocio
│   ├── persistencia/     # Acceso y gestión de datos
│   ├── presentacion/     # Interfaz y menús de consola
│   ├── servicios/        # Lógica y operaciones del sistema
│   ├── main.py           # Punto de entrada de la aplicación
│   └── ...
│
├── tests/                # Pruebas del sistema
│
├── requirement.txt       # Dependencias de Python
├── .env.example          # Configuración de ejemplo
├── README.md             # Documentación principal
├── verify_login_flow.py  # Verificación del flujo de autenticación
└── .venv/                # Entorno virtual
```

## 🏗️ Arquitectura del sistema

EcoTech está desarrollado siguiendo una arquitectura modular basada en la separación de responsabilidades. Su estructura se divide en cuatro capas principales:

| Capa | Responsabilidad |
|---|---|
| **Dominio** | Define las entidades, estructuras y reglas fundamentales del negocio. |
| **Persistencia** | Gestiona el almacenamiento, recuperación y acceso a la información. |
| **Servicios** | Contiene la lógica de negocio y coordina las operaciones del sistema. |
| **Presentación** | Gestiona la interacción con el usuario mediante menús y opciones de consola. |

Esta organización facilita el mantenimiento, la reutilización del código, la detección de errores y la incorporación de nuevas funcionalidades.

## 🧪 Pruebas y validación

El proyecto dispone de un directorio destinado a pruebas (`tests/`) y de un archivo adicional para verificar el flujo de autenticación.

Para ejecutar la verificación del inicio de sesión:

```bash
python verify_login_flow.py
```

Estas herramientas permiten comprobar el comportamiento de determinados componentes y detectar posibles errores durante el desarrollo.

## 🤖 Uso de inteligencia artificial en el desarrollo

Durante el desarrollo de EcoTech, la inteligencia artificial puede utilizarse como herramienta de apoyo para mejorar la calidad del software y optimizar el proceso de programación.

Entre sus principales aplicaciones se encuentran:

- Análisis e interpretación de requerimientos.
- Propuestas de mejoras en la arquitectura del sistema.
- Revisión de la lógica de autenticación y autorización.
- Validación de menús, permisos y restricciones según el rol.
- Identificación y corrección de errores.
- Optimización de la experiencia de usuario en consola.
- Elaboración y mejora de documentación técnica.

La inteligencia artificial funciona como una herramienta complementaria al desarrollo, permitiendo agilizar tareas y detectar posibles problemas. Sin embargo, toda implementación debe ser revisada, probada y validada por el desarrollador.

## 📌 Consideraciones finales

EcoTech busca proporcionar una solución organizada y funcional para la gestión de personal, proyectos y tiempos de trabajo.

Su diseño modular permite mantener una estructura clara, separar las responsabilidades de cada componente y facilitar futuras ampliaciones.

El proyecto representa una aplicación práctica de conceptos de programación en Python, bases de datos, autenticación, control de acceso, arquitectura de software y gestión de información.

---

