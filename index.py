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
  password="toor",
  database="salida"
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
@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           parseCSV(file_path)
          # save the file
      return redirect(url_for('home'))


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
             sql = "INSERT INTO addresses (first_name, last_name, address, street, state, zip) VALUES (%s, %s, %s, %s, %s, %s)"
             value = (row['first_name'],row['last_name'],row['address'],row['street'],row['state'],str(row['zip']))
             mycursor.execute(sql, value, if_exists='append')
             mydb.commit()
             print(i,row['first_name'],row['last_name'],row['address'],row['street'],row['state'],row['zip'])

if __name__ == '__main__':
    app.run(debug=True)

