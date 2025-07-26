Recomendaciones:

# Crear entorno virtual antes de realizar el proyecto
# Ubuntu
sudo apt update
sudo apt install python3-venv
cd /ruta/del/directorio
python3 -m venv venv
source venv/bin/activate
pip install mysql-connector-python

#Para desactivar
deactivate

# Windows
python -m venv venv
venv\Scripts\activate
.\venv\Scripts\Activate
pip install mysql-connector-python

#Para desactivar
deactivate


*******************************************************************************************

Guia para realizar el proyecto: https://www.youtube.com/watch?v=TjaG7243BF0&t=632s

1. Instalar python 3 https://www.python.org/downloads/
2. Instalar pip "Abrir terminal y revisar si ya esta instalado " -> pip --version 
3. Instalar extensiones para visual studio
        #bootstrap 5 quick snippets
        #python de MICROSOFT

4. Instalar mediante pip Flask "frameword para desarrollo web Flask"
        #comando -> pip install flask

5.  Instalar el conector a la base de datos  -> OJO "no instalar la del video"
        #comando -> pip install mysql-connector-python

    #ojo cuando se importe debe ir este codigo: 
        # import mysql.connector 

6. Creacion de estructura web:
    carpeta -> templates "debe llamarse asi"

# Diseño
https://bootswatch.com/
descargar el archivo css 





# ProyectoBasePython
