from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors

app = Flask(__name__)

connection = pymysql.connect(
    database = 'cvasquez_todos',
    user = 'cvasquez',
    password = '242590909',
    host = '10.100.33.60',
    cursorclass = pymysql.cursors.DictCursor
)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        cursor = connection.cursor()
        new_todo = request.form['new_todo']
        cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{new_todo}');")
        cursor.close()
        connection.commit()

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `todos`")
    results = cursor.fetchall()
    cursor.close()
        
    return render_template('todos.html.jinja', todos_list=results)


@app.route('/delete_todo/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM `todos` WHERE `id` = {todo_index}")
    cursor.close()
    connection.commit()
    return redirect('/')