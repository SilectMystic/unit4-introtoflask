from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    connection = pymysql.connect(
    database = 'cvasquez_todos',
    user = 'cvasquez',
    password = '242590909',
    host = '10.100.33.60',
    cursorclass = pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    cursor.execute("SELECT `description` FROM `todos`")
    results = cursor.fetchall()
    if request.method == 'POST':
        new_todo = request.form['new_todo']
        cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ({new_todo})")
    return render_template('todos.html.jinja', todos_list=results)

# @app.route('/delete_todo/<int:todo_index>', methods=['POST'])
# def todo_delete(todo_index):
#     del todos_list[todo_index]
#     return redirect('/')