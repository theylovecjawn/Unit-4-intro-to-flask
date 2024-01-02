from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = ["Make the basketball team", "Get 18 Certifications"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_todo = request.form["new_todo"].strip() 
        if new_todo:  
            todos.append(new_todo)
    return render_template("todo.html.jinja", todos=todos)

@app.route('/delete_todo/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
    del todos[todo_index]
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
