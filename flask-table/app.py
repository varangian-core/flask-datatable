#app.py
from flask import Flask, render_template, json, request, redirect
import pymysql
#from flaskext.mysql import MySQL
#from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
from datetime import datetime
  
app = Flask(__name__)
  
app.secret_key = "caircocoders-ednalan-2020"
  

db = pymysql.connect(host = 'localhost',user = 'v', password = 'test123TEST!@#', database = 'elite')

  
@app.route('/')
def main():
    return redirect('/useradmin')
    
@app.route('/dbtest')
def test_db():
    cur= db.cursor()
    sql = '''SELECT hash_id,form, document, revision, date_issue,
          date_rev, LOCATIONS_STATUS, file_name from documents
          INNER JOIN file_info ON form LIKE concat(substring(file_name,1,12), '%')
          UNION
          SELECT DISTINCT hash_id, form, document, revision, date_issue, 
          date_rev, LOCATIONS_STATUS, file_name from documents
          INNER JOIN file_info
          ON concat(form, ' ') = substring(file_name, 1, length(form)+1)
          UNION
          SELECT hash_id, form, document, revision, date_issue, 
          date_rev, LOCATIONS_STATUS, file_name from documents
          INNER JOIN file_info ON substring(file_name, 1,
          length(file_name)-4) = form'''

    cur.execute(sql)
    # cur.execute("SELECT * from documents")
    docs= cur.fetchall()
    return render_template('document1.html', docs=docs)

    
@app.route('/useradmin')
def useradmin():
    cur = db.cursor()
    result = cur.execute("SELECT * FROM employee")
    employee = cur.fetchall()
    return render_template('useradmin.html', employee=employee)


@app.route('/updatedocs', methods=['POST'])
def updatedocs():
        pk = request.form['pk']
        name = request.form['name']
        value = request.form['value']
        cur = db.cursor()
        if name == 'name':
           cur.execute("UPDATE employee SET name = %s WHERE id = %s ", (value, pk))
        elif name == 'email':
           cur.execute("UPDATE employee SET email = %s WHERE id = %s ", (value, pk))
        elif name == 'phone':
           cur.execute("UPDATE employee SET phone = %s WHERE id = %s ", (value, pk))
        db.commit()
        return json.dumps({'status':'OK'})
 
@app.route('/updateemployee', methods=['POST'])
def updateemployee():
        pk = request.form['pk']
        name = request.form['name']
        value = request.form['value']
        cur = db.cursor()
        if name == 'name':
           cur.execute("UPDATE employee SET name = %s WHERE id = %s ", (value, pk))
        elif name == 'email':
           cur.execute("UPDATE employee SET email = %s WHERE id = %s ", (value, pk))
        elif name == 'phone':
           cur.execute("UPDATE employee SET phone = %s WHERE id = %s ", (value, pk))
        db.commit()
        return json.dumps({'status':'OK'})
             
if __name__ == '__main__':
    app.run(DEBUG=true)
