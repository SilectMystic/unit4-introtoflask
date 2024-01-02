from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos_list = ['hacer comida', 'limpiar la casa']

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form['new_todo']
        todos_list.append(new_todo)
    return render_template('todos.html.jinja', todos_list=todos_list)

@app.route('/delete_todo/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
    del todos_list[todo_index]
    return redirect('/')