from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "super secret key"

#MYSQL CONNECTION
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='newrootpassword'
app.config['MYSQL_DB']='crud1'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql = MySQL(app)

#Loading Home page
@app.route("/")
def home():
    con = mysql.connection.cursor()
    sql = "SELECT * FROM users1"
    con.execute(sql)
    res = con.fetchall()
    return render_template("stanley_home.html", datas=res)

#New User
@app.route("/addUsers", methods=["GET","POST"])
def addUsers():
    if request.method == "POST":
        name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        con = mysql.connection.cursor()
        sql = "insert into users1(NAME,CITY,AGE) value (%s,%s,%s)"
        con.execute(sql,[name,city,age])
        mysql.connection.commit()
        con.close()
        flash("User Details Added")
        return redirect(url_for("home"))
    return render_template("stanley_addUsers.html")

# Update User
@app.route("/editUser/<string:id>)", methods=["GET","POST"])
def editUser(id):
    con = mysql.connection.cursor()
    if request.method == "POST":
        name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        con = mysql.connection.cursor()
        sql = "update users1 set NAME=%s,CITY=%s,AGE=%s WHERE ID=%s"
        con.execute(sql,[name,city,age,id])
        mysql.connection.commit()
        con.close()
        flash("User Details Updated")
        return redirect(url_for("home"))
        con=mysql.connection.cursor()

    sql = "select * from users1 where ID=%s"
    con.execute(sql,[id])
    res = con.fetchone()
    return render_template("stanley_editUser.html",datas = res)

#Delete User
@app.route("/deleteUser/<string:id>", methods=["GET","POST"])
def deleteUser(id):
    con = mysql.connection.cursor()
    sql = "delete from users1 where ID=%s"
    con.execute(sql,[id])
    mysql.connection.commit()
    con.close()
    flash("User Details Deleted")
    return redirect(url_for("home"))
if(__name__=='__main__'):
    app.run(debug=True)