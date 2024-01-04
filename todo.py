from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print
conn = pymysql.connect(host='10.100.33.60',
                             user='cjohn',
                             password='224257683',
                             database='cjohn_todos',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



app = Flask(__name__)

todos = []

cursor = conn.cursor()

@app.route("/", methods=["GET", "POST"])
def index():
    cursor.execute("SELECT `description` from `todos`")
    
    results = cursor.fetchall()
    
    if request.method == "POST":
        new_todo = request.form["new_todo"].strip() 
        if new_todo:  
            cursor.execute("INSERT INTO `todos`(`description`) VALUES", new_todo)

    return render_template("todo.html.jinja", todos = results)

@app.route('/delete_todo/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
    del todos[todo_index]
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
