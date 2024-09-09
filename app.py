from flask import Flask, jsonify
from flask import render_template 
from flask import url_for
from flask import request                 #recepciona la informacion "DEL FORMULARIO"
from flask import redirect                #redirecciona "MUESTRA LA INFORMACION PARA LAS TABLAS"
import mysql.connector                    #Se importa libreria para conexion a base de datos 
from datetime import datetime             #Se importa para colocar un tiempo exacto "Para la imagen"
from flask import send_from_directory     #optenemos informacion de la imagen
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


""" Mostramos la imagen y la enviamos a la ruta  """
@app.route('/img/libros/<imagen>')
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join('templates/sitio/img/libros'),imagen)


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
    """ Esta funcion me sirve para mostrar todos los libros de mi base de datos          
          """
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
        
        """ Esta funcion me sirve para ingresar los datos enviados 
         mediente un formulario a mi base de datos. """   
             
        """ verifica si llegan bien los datos
        print(request.form['nombreLibro'])
        print(request.files['imagenLibro']) #este se debe recibir como un archivo
        print(request.form['urlDescarga']) """

        nombre_libro = request.form['nombre_libro']
        imagen_libro = request.files['imagen_libro'] #se debe recibir como documento
        url_libro    = request.form['url_libro']

        """ El siguente codigo es para cambiarle el nombre a la imagen 
         se cambia para que no genere conflicto con el nombre de la imagen 
          al momento de almacenarla """
        #variable tiempo para cambiar el nombre de la imagen
        tiempo = datetime.now()
        horaActual = tiempo.strftime('%Y%H%M%S')

        #cambio de nombre de la imagen y guardado
        if imagen_libro.filename!="":

            nuevoNombreImagen = f"{horaActual}_{imagen_libro.filename}"
            imagen_libro.save("templates/sitio/img/libros/"+nuevoNombreImagen)

        conn = mysql.connector.connect(**config) # Crear una conexión al servidor MySQL

        datos = (nombre_libro,nuevoNombreImagen,url_libro)  #Agregamos los datos a la consulta
        sql = "INSERT INTO `libros` (`nombre_libro`, `imagen_libro`, `url_libro`) VALUES (%s,%s,%s);"        
        cursor = conn.cursor() # Crear un cursor para ejecutar comandos SQL
        cursor.execute(sql, datos) # Ejecutar una consulta SQL 
        conn.commit() #confirma la insercion SQL.... sin este paso no se ejecuta nada
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        
   
        return redirect('/librosAdmin')
   


        

            
@app.route('/admin/librosAdmin/borrar',methods=['POST'])
def admin_libros_borrar():  

    id_libro = request.form['id_libro']
 
    conn = mysql.connector.connect(**config) # Crear una conexión al servidor MySQL

    """ seleccionamos el libro para borrarlo  """   
    sql2 = "SELECT libros.imagen_libro FROM libros WHERE libros.id_libro =  %s;"        
    cursor = conn.cursor() # Crear un cursor para ejecutar comandos SQL 
    cursor.execute(sql2,[id_libro])   
    libroParaEliminarImagen = cursor.fetchall() # Obtener los resultados de la consulta
    conn.commit()
    print(f"este libro se va a eliminar {libroParaEliminarImagen}")

    if os.path.exists("templates/sitio/img/libros/"+str(libroParaEliminarImagen[0][0])):
        os.unlink("templates/sitio/img/libros/"+str(libroParaEliminarImagen[0][0]))



    
    sql = "DELETE FROM libros WHERE id_libro =  %s;"        
    cursor = conn.cursor() # Crear un cursor para ejecutar comandos SQL
    cursor.execute(sql,[id_libro]) # Ejecutar una consulta SQL 
    conn.commit() #confirma la insercion SQL.... sin este paso no se ejecuta nada
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    return redirect('/librosAdmin')






"""
Este comando es necesario para 
correr nuestra aplicacion
"""
if __name__ == '__main__':
    app.run(debug=True)



