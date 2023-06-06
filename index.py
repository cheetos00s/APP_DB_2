from flask import Flask, render_template, request, redirect, url_for
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
      
    mycursor.close()
    mydb.close()
  
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

        # Cierra la conexión
        mycursor.close()
        mydb.close()

        return redirect(url_for('tables'))

    except mysql.connector.Error as error:
        
      return f'Error al ejecutar el procedimiento almacenado: {str(error)}'
      
@app.route("/query_aux", methods=['POST'])
def query_aux():
  # Crear una lista de objetos TableData
  query_aux = "select * from tabla_aux"
  mycursor.execute(query_aux)
  result_aux = mycursor.fetchall()
  
  mycursor.close()
  mydb.close
  return render_template("tables.html", data=result_aux)


@app.route("/query_tr", methods=['POST'])
def query_tr():
  # Crear una lista de objetos TableData
  query_tr = "select * from tratamiento_registro"
  mycursor.execute(query_tr)
  result_tr = mycursor.fetchall()
  
  mycursor.close()
  mydb.close
  return render_template("tables.html", data=result_tr)

  
      
@app.route("/tables")
def tables():
    return render_template('tables.html')


if __name__ == '__main__':
    app.run(debug=True)

