from flask import Flask, jsonify, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
import pandas as pd
import mysql.connector

app = Flask(__name__)



#sql connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0720",
  database="refugio_animales"
)


mycursor = mydb.cursor()

UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template('index.html')



# Get the uploaded files
@app.route("/upload", methods=['POST'])
def upload():
  try:
    csvfile = request.files['csvfile']
    df = pd.read_csv(csvfile)
    df = df.fillna('')
  
 
    aux_tabla = 'tabla_aux'
 
    for _, row in df.iterrows():
    
      sql = f"INSERT INTO `{aux_tabla}` (`ID_AUX`, `ID_MASCOTA`, `NOMBRE_MASCOTA`,`EDAD_MASCOTA`,`RAZA_MASCOTA`,`FECHA_INGRESO`,`ESTADO_MASCOTA`, `GENERO_MASCOTA`,`ESPECIE_MASCOTA`,`ID_REFUGIO`,`ID_SITIO`,`ID_PERSONA`,`NOMBRE_PERSONA`,`EDAD_PERSONA`,`EMPLEO_PERSONA`,`SALARIO_PERSONA`,`DIRECCION_PERSONA`,`CIUDAD_PERSONA`,`NOMBRE_REFUGIO`, `DIRECCION_REFUGIO`,`HORARIO_REFUGIO`,`MAIL_REFUGIO`,`TELEFONO_REFUGIO`,`ID_SEDE`,`ID_DONACION`,`TIPO_DONACION`,`DESCRIPCION_DONACION`,`ID_DONANTE`,`NOMBRE_DONANTE`,`EDAD_DONANTE`,`TELEFONO_DONANTE`,`MAIL_DONANTE`,`NOMBRE_SEDE`,`DIRECCION_SEDE`,`NOMBRE_RESCATE`,`DIRRECCION_RESCATE`,`ID_TRATAMIENTO`,`FECHA_TRATAMIENTO`,`TIPO_TRATAMIENTO`,`DESCRIPCION_TRATAMIENTO`) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s,%s,%s,%s,%s,%s)"
      values = (row['ID_AUX'], row['ID_MASCOTA'], row['NOMBRE_MASCOTA'], row['EDAD_MASCOTA'], row['RAZA_MASCOTA'], row['FECHA_INGRESO'], row['ESTADO_MASCOTA'], row['GENERO_MASCOTA'], row['ESPECIE_MASCOTA'] , row['ID_REFUGIO'], row['ID_SITIO'], row['ID_PERSONA'],row['NOMBRE_PERSONA'], row['EDAD_PERSONA'], row['EMPLEO_PERSONA'], row['SALARIO_PERSONA'], row['DIRECCION_PERSONA'], row['CIUDAD_PERSONA'], row['NOMBRE_REFUGIO'], row['DIRECCION_REFUGIO'],row['HORARIO_REFUGIO'], row['MAIL_REFUGIO'], row['TELEFONO_REFUGIO'], row['ID_SEDE'], row['ID_DONACION'],   row['TIPO_DONACION'],  row['DESCRIPCION_DONACION'],row['ID_DONANTE'],  row['NOMBRE_DONANTE'], row['EDAD_DONANTE'], row['TELEFONO_DONANTE'], row['MAIL_DONANTE'], row['NOMBRE_SEDE'], row['DIRECCION_SEDE'], row['NOMBRE_RESCATE'], row['DIRRECCION_RESCATE'], row['ID_TRATAMIENTO'], row['FECHA_TRATAMIENTO'], row['TIPO_TRATAMIENTO'], row['DESCRIPCION_TRATAMIENTO'])
    
      mycursor.execute(sql,values)
      mydb.commit()
      

  
    return redirect(url_for('home'))

  except Exception as error:
        error_message = str(error)
        return render_template('error.html', error_message=error_message)


# Ruta para llamar al procedimiento almacenado
@app.route("/insertar_datos", methods=['POST'])
def insert_data():
    try:

        # Llama al procedimiento almacenado
        mycursor.callproc('InsertarDatos')

        # Confirma los cambios en la base de datos
        mydb.commit()

    


        return redirect(url_for('tables'))

    except mysql.connector.Error as error:
        
      return f'Error al ejecutar el procedimiento almacenado: {str(error)}'


def query_tr():
    try:
        # Crear una lista de objetos TableData
        mycursor = mydb.cursor(dictionary=True)
        query_tr = ("select * from tratamiento_registro")
        mycursor.execute(query_tr)
        result_tr = mycursor.fetchall()

        

        return result_tr

    except mysql.connector.Error as error:
        return f'Error al ejecutar la consulta: {str(error)}'

def query_donacion():
    try:
        # Crear una lista de objetos TableData
        mycursor = mydb.cursor(dictionary=True)
        query_don = ("select * from donacion")
        mycursor.execute(query_don)
        result_don = mycursor.fetchall()
        
       

        return result_don

    except mysql.connector.Error as error:
        return f'Error al ejecutar la consulta: {str(error)}'

 

def query_donante():
    try:
        # Crear una lista de objetos TableData
        mycursor = mydb.cursor(dictionary=True)
        query_dona = ("select * from donante")
        mycursor.execute(query_dona)
        result_dona = mycursor.fetchall()
        

        return result_dona

    except mysql.connector.Error as error:
        return f'Error al ejecutar la consulta: {str(error)}'

def query_refugio():
    try:
        # Crear una lista de objetos TableData
        mycursor = mydb.cursor(dictionary=True)
        query_re = ("select * from refugio")
        mycursor.execute(query_re)
        result_re = mycursor.fetchall()
        
    

        return result_re

    except mysql.connector.Error as error:
        return f'Error al ejecutar la consulta: {str(error)}' 

def query_mascota():
    try:
        # Crear una lista de objetos TableData
        mycursor = mydb.cursor(dictionary=True)
        query_mas = ("select * from mascota")
        mycursor.execute(query_mas)
        result_mas = mycursor.fetchall()
        
        print(result_mas)
        

        return result_mas

    except mysql.connector.Error as error:
        return f'Error al ejecutar la consulta: {str(error)}' 

      
def query_sede():
    try:
        # Crear una lista de objetos TableData
        mycursor = mydb.cursor(dictionary=True)
        query_se = ("select * from sede")
        mycursor.execute(query_se)
        result_se = mycursor.fetchall()
        


        return result_se

    except mysql.connector.Error as error:
        return f'Error al ejecutar la consulta: {str(error)}' 
 
def query_tratamiento():
    try:
        # Crear una lista de objetos TableData
        mycursor = mydb.cursor(dictionary=True)
        query_tra = ("select * from tratamiento")
        mycursor.execute(query_tra)
        result_tra = mycursor.fetchall()

    

        return result_tra

    except mysql.connector.Error as error:
        return f'Error al ejecutar la consulta: {str(error)}' 
      
def query_sitio_rescate():
    try:
        # Crear una lista de objetos TableData
        mycursor = mydb.cursor(dictionary=True)
        query_res = ("select * from sitio_rescate")
        mycursor.execute(query_res)
        result_res = mycursor.fetchall()

        

        return result_res

    except mysql.connector.Error as error:
        return f'Error al ejecutar la consulta: {str(error)}' 

def query_persona():
    try:
        # Crear una lista de objetos TableData
        mycursor = mydb.cursor(dictionary=True)
        query_per = ("select * from persona")
        mycursor.execute(query_per)
        result_per = mycursor.fetchall()

        

        return result_per

    except mysql.connector.Error as error:
        return f'Error al ejecutar la consulta: {str(error)}' 
      
           
@app.route("/tables")
def tables():
    result_tr = query_tr()
    result_donacion = query_donacion()
    result_donante = query_donante()
    result_refugio = query_refugio()
    result_mascota = query_mascota()
    result_sede = query_sede()
    result_tratamiento = query_tratamiento()
    result_persona = query_persona()
    result_sitio_rescate = query_sitio_rescate()
    print(result_tratamiento)
    return render_template('tables.html', datatr = result_tr, dataTratamiento = result_tratamiento, dataDonacion = result_donacion, dataSede = result_sede, dataRefugio = result_refugio, dataDonante = result_donante, dataMascota = result_mascota, dataPersona = result_persona, dataSitio = result_sitio_rescate)

@app.route('/calcular_media', methods=['GET', 'POST'])
def calcular_media():
    if request.method == 'POST':
        try:
            tabla = request.form['tabla']
            columna = request.form['columna']
            mycursor.callproc('CalcularMedia', [tabla, columna, 0])
            mycursor.execute('SELECT @media')
            media = mycursor.fetchone()[0] 
            print(media)
            print(tabla)
            print(columna)
            return render_template('index.html', media=media)
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

