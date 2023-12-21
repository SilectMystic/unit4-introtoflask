from flask import Flask, render_template, request

app = Flask(__name__)

todos_list = ['hacer comida', 'limpiar la casa']

@app.route('/', methods=['GET','POST'])
def index():
    new_todo = request.form['new_todo']
    todos_list.append(new_todo)
    return render_template('todos.html.jinja', todos_list=todos_list)