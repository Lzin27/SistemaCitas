
## 📋 Diagramas de Arquitectura
Integrantes: 
Leonardo 
Jhordan 
Milagros Leyva 

## Descripción
Sistema web para agendar y gestionar citas médicas de forma eficiente. Incluye API RESTful y interfaz web.

## Tecnologías Utilizadas
- **Backend:** Python (FastAPI o Flask - según tu `requirements.txt`)
- **Frontend:** HTML, CSS, JavaScript
- **Base de Datos:** SQLite / MySQL (ajusta según lo que uses)
- **Otros:** Git, GitHub


### 1. Diagrama de Casos de Uso
Muestra la interacción entre los actores (Paciente, Médico, Recepcionista) y las funcionalidades del sistema.


### 2. Diagrama de Componentes
Ilustra la estructura interna del sistema y cómo interactúan sus componentes entre sí.


### 3. Diagrama de Despliegue
Representa la infraestructura donde se ejecuta el sistema, incluyendo servidores y dispositivos.

Figma: Diagramas 
https://www.figma.com/design/UNpFBLYUVLsr4sdiBGYDvS/Sin-t%C3%ADtulo?node-id=0-1&t=nKwYHEleOsveDAHF-1

## 🚀 Instalación y Despliegue

### Prerrequisitos
- Java JDK 11+
- Node.js (para el frontend web)
- MySQL Server 8.0+
- Android Studio o Xcode (para compilar la app móvil)

### Pasos para Ejecutar
1.  Clona el repositorio:
    ```bash
    git clone https://github.com/[tu-usuario]/sistema-citas-medicas.git
    ```
2.  Configura la base de datos:
    - Importa el esquema desde `database/schema.sql`.
    - Configura las credenciales en `backend/src/main/resources/application.properties`.
3.  Ejecuta el backend:
    ```bash
    cd backend
    ./mvnw spring-boot:run
    ```
4.  Ejecuta el frontend web:
    ```bash
    cd frontend-web
    npm install
    npm run dev
    ```
5.  Abre tu navegador y ve a `http://localhost:3000`.


