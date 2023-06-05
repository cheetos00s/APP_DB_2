from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
import pandas as pd
import mysql.connector

info = ("xddd", "huevo", "hambre", "zanahoria", "gato")
csvData = ();

app = Flask(__name__)

#sql connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0720",
  database="refugio_animales"
)

# sql test connection

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

# List All Databases
for x in mycursor:
  print(x)

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template('index.html', informacion=csvData)

# Get the uploaded files
@app.route("/upload", methods=['POST'])
def upload():
  csvfile = request.files['csvfile']
  df = pd.read_csv(csvfile)
  df = df.fillna('')
  
 
  aux_tabla = 'tabla_aux'
 
  for _, row in df.iterrows():
    sql = f"INSERT INTO `{aux_tabla}` (`ID_AUX`, `ID_MASCOTA`, `NOMBRE_MASCOTA`,`EDAD_MASCOTA`,`RAZA_MASCOTA`,`FECHA_INGRESO`,`ESTADO_MASCOTA`, `GENERO_MASCOTA`,`ESPECIE_MASCOTA`,`ID_REFUGIO`,`ID_SITIO`,`ID_PERSONA`,`NOMBRE_PERSONA`,`EDAD_PERSONA`,`EMPLEO_PERSONA`,`SALARIO_PERSONA`,`DIRECCION_PERSONA`,`CIUDAD_PERSONA`,`NOMBRE_REFUGIO`, `DIRECCION_REFUGIO`,`HORARIO_REFUGIO`,`MAIL_REFUGIO`,`TELEFONO_REFUGIO`,`ID_SEDE`,`ID_DONACION`,`TIPO_DONACION`,`DESCRIPCION_DONACION`,`ID_DONANTE`,`NOMBRE_DONANTE`,`EDAD_DONANTE`,`TELEFONO_DONANTE`,`MAIL_DONANTE`,`NOMBRE_SEDE`,`DIRECCION_SEDE`,`NOMBRE_RESCATE`,`DIRRECCION_RESCATE`,`ID_TRATAMIENTO`,`FECHA_TRATAMIENTO`,`TIPO_TRATAMIENTO`,`DESCRIPCION_TRATAMIENTO`) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s,%s,%s,%s,%s,%s)"
    values = (row['ID_AUX'], row['ID_MASCOTA'], row['NOMBRE_MASCOTA'], row['EDAD_MASCOTA'], row['RAZA_MASCOTA'], row['FECHA_INGRESO'], row['ESTADO_MASCOTA'], row['GENERO_MASCOTA'], row['ESPECIE_MASCOTA'] , row['ID_REFUGIO'], row['ID_SITIO'], row['ID_PERSONA'],row['NOMBRE_PERSONA'], row['EDAD_PERSONA'], row['EMPLEO_PERSONA'], row['SALARIO_PERSONA'], row['DIRECCION_PERSONA'], row['CIUDAD_PERSONA'], row['NOMBRE_REFUGIO'], row['DIRECCION_REFUGIO'],row['HORARIO_REFUGIO'], row['MAIL_REFUGIO'], row['TELEFONO_REFUGIO'], row['ID_SEDE'], row['ID_DONACION'],   row['TIPO_DONACION'],  row['DESCRIPCION_DONACION'],row['ID_DONANTE'],  row['NOMBRE_DONANTE'], row['EDAD_DONANTE'], row['TELEFONO_DONANTE'], row['MAIL_DONANTE'], row['NOMBRE_SEDE'], row['DIRECCION_SEDE'], row['NOMBRE_RESCATE'], row['DIRRECCION_RESCATE'], row['ID_TRATAMIENTO'], row['FECHA_TRATAMIENTO'], row['TIPO_TRATAMIENTO'], row['DESCRIPCION_TRATAMIENTO'])
    bandera = mydb.cursor()
    bandera.execute(sql,values)
    mydb.commit()
    bandera.close()
  mydb.close()
  return redirect(url_for('home'))

 
#def uploadFiles():
      # get the uploaded file
   #   uploaded_file = request.files['file']
   #   if uploaded_file.filename != '':
    #       file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
     #      uploaded_file.save(file_path)
      #     parseCSV(file_path)
          # save the file
     # return redirect(url_for('home'))


@app.route("/contacto")
def contacto():
    return "pagina de contacto"

def parseCSV(filePath):
      # CVS Column Names
      col_names = ['first_name','last_name','address', 'street', 'state' , 'zip']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,names=col_names, header=None)
      # Loop through the Rows
      for i,row in csvData.iterrows():
             print(i,row['first_name'],row['last_name'],row['address'],row['street'],row['state'],row['zip'],)
if __name__ == '__main__':
    app.run(debug=True)

