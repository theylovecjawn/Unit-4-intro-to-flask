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
    cursor.execute("SELECT * from `todos` ORDER BY `completion`")
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

@app.route('/complete_todo/<int:todo_index>', methods=['POST'])
def todo_complete(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE `todos` SET `completion` = 1 WHERE `id` = {todo_index}")
    conn.commit()
    cursor.close()
    return redirect('/')

@app.route('/uncomplete_todo/<int:todo_index>', methods=['POST'])
def todo_uncomplete(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE `todos` SET `completion` = 0 WHERE `id` = {todo_index}")
    conn.commit()
    cursor.close()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
