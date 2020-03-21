from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MYSQL CONFIGURATION
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'jayabalaji'
app.config['MYSQL_DB'] = 'DBS'

mysql = MySQL(app)


# python flask api to Fetch the data from Database
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM MYUSERS")
    data = cur.fetchall()
    cur.close()
    return render_template('Home.html', data=data)


if __name__ == '__main__':
    app.run()
