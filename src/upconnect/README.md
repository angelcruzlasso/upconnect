# Guia de instalacion usuarios Linux (incluye WSL) 🐧📁

1. **Clonar el repositorio** del proyecto. lo recomendables es hacerlo en un directorio como **documents** o crear uno llamado **proyectos**.

    ```bash
    # Si desea crear una carpeta llamada proyectos; En caso contrario solo clone el repositorio como se muestra mas adelante
    mkdir proyectos

    # Una vez creado puede situarse a la carpeta que creo con el siguiente comando
    cd proyectos

    # luego clonamos el respositorio
    git clone https://github.com/angelcruzlasso/upconnect.git
    ```

2. **Activar el entorno virtual**, para mantener el proyecto bien estructurado, debe saber en que lugar debe crear la carpeta oculta de **venv** por lo tanto:

    ```bash
    upconnect
    ├── __pycache__
    └── src
    └── upconnect
        ├── assets
        ├── database
        ├── pages
        ├── __pycache__
        └── upconnect
            └── __pycache__
    ```

    Debe crear el archivo venv dentro de la carpeta **upconnect**!!

    ```bash
    # Nos situamos en la carpeta en donde crearemos el archivo venv
    cd ~/Documents/proyectos/upconnect/src/upconnect
    # Si usted no creo un directorio Documents y solo tiene alojado en su usuario la carpeta proyectos (usuarios WSL)
    cd ~/proyetos/upconnect/src/upconnect
    ```

    Ahora si podemos crear el archivo venv

    ```bash
    # Creacion del archivo oculto venv
    angelcl@archlinux:/upconnect/src/upconnect$ python -m venv .venv
    # Si esta en ubuntu
    angelcl@ubuntu:/upconnect/src/upconnect$ python3 -m venv .venv
    ```

    Procedemos a activar el entorno virtual

    ```bash
    # Activacion del entorno virtual (lo mismo para ubuntu)
    angelcl@archlinux:/upconnect/src/upconnect$ source .venv/bin/activate
    ```

3. **Instalacion de los paquetes** para instalar los paquetes nesesarios para el proyecto, esto se logra por el archivo requirements.txt

   ```bash
   # instalacion de paquetes como reflex...
   angelcl@archlinux:/upconnect/src/upconnect$ python install -r requirements.txt
   ```

4. **Arrancar reflex**, una vez instalado reflex un requisito para inicializar  reflex es tener **unzip** que descomprimira archivos comprimidos durante la inicializacion si instala con el siguiente comando.

    ```bash
    # Si esta en archlinux
    sudo pacman -S unzip
    # Si esta en ubuntu
    sudo apt -S unzip
    ```

    Luego, podemos seguir con lo siguiente:

    ```bash
    # Inicializamos la app de reflex
    reflex init

    # Corremos reflex
    reflex run
    ```

## Felicitaciones, ya estas listo para colaborar 👏🏼

Pronto hare una documentacion para git para el control de versiones del proyecto...
