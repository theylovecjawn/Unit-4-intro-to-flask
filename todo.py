from flask import Flask, render_template, request


app = Flask(__name__)

todos = ["Make the basketball team", "Get 18 Certifications"]

@app.route('/', methods=['GET','POST'])
def index():
    new_todo = request.form['new_todo']
    return render_template('todo.html.jinja', todos = todos)




