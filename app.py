from flask import Flask, jsonify
from flask import render_template 
from flask import url_for
from flask import request                 #recepciona la informacion "DEL FORMULARIO"
from flask import redirect                #redirecciona "MUESTRA LA INFORMACION PARA LAS TABLAS"
import mysql.connector                    #Se importa libreria para conexion a base de datos 
from datetime import datetime             #Se importa para colocar un tiempo exacto "Para la imagen"
from flask import send_from_directory 
from flask import abort #obtenemos la informacion de la imagen, es necesaria para mostrar las imagenes
import os


       
app = Flask(__name__) #se crea la aplicacion

# Configuración de la conexión MySQL usando MySQL X Protocol
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'port': 3306,                  # Puerto para MySQL X Protocol
    'database': 'biblioteca'
}



@app.route('/')
def inicio():
    """ se crean las rutas de navegacion """
    print(url_for('inicio'))
    print(url_for('libros'))
    #print(url_for('nosotros'))
    return render_template('sitio/index.html')

@app.route('/templates/sitio/img/libros/<imagen>')
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join('template/sitio/img/libros'),imagen)

@app.route('/libros')
def libros():
    return render_template('sitio/libros.html')


@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')



@app.route('/admin/')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/login')
def admin_login():
    return render_template('loginAdmin.html')

@app.route('/librosAdmin')
def admin_libros():
        
    conn = mysql.connector.connect(**config) # Crear una conexión al servidor MySQL
    cursor = conn.cursor() # Crear un cursor para ejecutar comandos SQL    
    cursor.execute('SELECT * FROM libros') # Ejecutar una consulta SQL     
    listaLibros = cursor.fetchall() # Obtener los resultados de la consulta

    #print(f"conexion ok *********************{listaLibros} **************************" )

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    return render_template('admin/librosAdmin.html',listaLibros=listaLibros)

    

@app.route('/admin/librosAdmin/guardar', methods=['POST']) # Recibe los datos enviados por POST
def admin_libros_guardar():
   print(request.form['nombreLibro'])
   print(request.files['imagenLibro']) #este se debe recibir como un archivo
   print(request.form['urlDescarga'])
   
   return redirect('/librosAdmin')
   


   """  nombre = request.form['nombreLibro']
    imagen = request.files['imagenLibro']
    url = request.form['urlDescarga']

    #variable tiempo para cambiar el nombre de la imagen
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%Y%H%M%S')

    #cambio de nombre de la imagen y guardado
    if imagen.filename!="":
        nuevoNombreImagen = f"{horaActual}_{imagen.filename}"
        imagen.save("templates/sitio/img/libros/"+nuevoNombreImagen) """

    #insert a base de datos
""" 

    sql = "INSERT INTO `libros` (`nombre_libro`, `imagen_libro`, `url_libro`) VALUES (%s,%s,%s);"
    datos = (nombre,nuevoNombreImagen,url)  #Agregamos los datos a la consulta
    cursor = conexion.cursor()  #creamos un objeto
    cursor.execute(sql,datos) #ejecutamos el objeto con la consulta y los datos recibidos
    conexion.commit() #confirmamos la ejecucion 

    return redirect('/admin/libros')
"""
""" @app.route('/admin/libros/borrar',methods=['POST'])
def admin_libros_borrar():  

    id_libro = request.form['id_libro']
 """
""" #solo hace la consulta
    cursor.execute("SELECT * FROM libros WHERE id_libro = %s",(id_libro))
    libro = cursor.fetchall()
    conexion.commit()
    print(libro)
    #fin de la consulta

    #Eliminacion de registro
    cursor.execute("DELETE FROM libros WHERE id_libro = %s",(id_libro) )  
    conexion.commit() #confirmamos ejecucion
    #Fin de eliminacion registro
   """


"""
    return redirect('/admin/libros')"""




"""
Este comando es necesario para 
correr nuestra aplicacion
"""
if __name__ == '__main__':
    app.run(debug=True)



