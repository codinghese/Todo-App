from flask import Flask,render_template,request,redirect, url_for,flash, abort, session
import json
import requests
import os.path
import sqlite3  


app=Flask(__name__)

@app.route('/')
def index():

	conn = sqlite3.connect('Todo.db')
	data = conn.execute("select * from todolist");
	#conn.close();
	return render_template('home.html',data=data)

@app.route('/additem',methods=['POST'])
def additem():
		msg="msg"
		try:

			name=request.form['text']
			msg="test1"
			with sqlite3.connect("Todo.db") as con:
				msg="test2"
				cur = con.cursor()
				msg="test3"
				
				cur.execute('INSERT into todolist (name) values ("{0}")'.format(name))
				msg="test4"
				con.commit()
				msg = "Employee successfully Added"
		except:
			con.rollback()
			#msg = "We can not add the employee to the list"  
		finally:
			return redirect(url_for('index'))
		
			con.close()

@app.route("/deleteitem",methods = ["POST"])  
def deleteitem():  
    name=request.form['rowid']
    name.strip()
    msg="msg"
    with sqlite3.connect("Todo.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute('delete from todolist where name = "{0}"'.format(name))  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
	return redirect(url_for('index'))
    



