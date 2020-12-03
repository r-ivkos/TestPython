
#decorations
def p_hw(func):
	def inner():
		print("Hello world")
		func()
	return inner

@p_hw
def hw():
	print ("Another hello world")

hw()

#sqlite3 library
import sqlite3 as sql
conn = sql.connect('example.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS t1 (num1 int, txt1 char(30))")
c.execute("INSERT INTO t1 VALUES(2, \'Hello WORLD\')")

for row in c.execute("SELECT * FROM t1 WHERE num1 <>10"):
	print(row[1])

conn.rollback()
conn.close()


#flask 
from flask import Flask, jsonify

app = Flask(__name__)


values = [1, 2, 3, 4, 5]

@app.route('/', methods=['GET'])
def hello_world():
	return jsonify(values[2])

@app.route('/', methods=['PUT'])
def hello_world2():
	return jsonify(values)

if __name__ ==  "__main__":
	app.run(debug=True)