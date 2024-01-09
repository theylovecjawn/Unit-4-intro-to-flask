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


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_todo = request.form["new_todo"].strip()
        cursor = conn.cursor()
        cursor.close
        if new_todo:
            cursor.execute(f"INSERT INTO `todos`(`description`) VALUES ('{new_todo}')")
            conn.commit()
    cursor = conn.cursor()
    cursor.execute("SELECT * from `todos`")
    results = cursor.fetchall()
    cursor.close()
    return render_template("todo.html.jinja", todos=results)


@app.route('/delete_todo/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM `todos` WHERE `id` = ('{todo_index}')")
    conn.commit()
    cursor.close()
    return redirect('/')

@app.route('/update_todos', methods=['POST'])
def update_todos():
    cursor = conn.cursor()
    results = cursor.fetchall()
    for todo in results:
        todo_id = str(todo['id'])
        if f"todo_{todo_id}" in request.form:
            
            todo['completed'] = True
        else:
            
            todo['completed'] = False
    return render_template('todos.html', todos= results)


if __name__ == "__main__":
    app.run(debug=True)
