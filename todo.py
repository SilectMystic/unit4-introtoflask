from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'hehe' : 'haha'
}

connection = pymysql.connect(
    database = 'cvasquez_todos',
    user = 'cvasquez',
    password = '22590909',
    host = '10.100.33.60',
    cursorclass = pymysql.cursors.DictCursor
)

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/', methods=['GET','POST'])
@auth.login_required
def index():
    if request.method == 'POST':
        cursor = connection.cursor()
        new_todo = request.form['new_todo']
        cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{new_todo}');")
        cursor.close()
        connection.commit()

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `todos` ORDER BY `complete`")
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

@app.route('/complete_todo/<int:todo_index>', methods=['POST'])
def complete_todo(todo_index):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE `todos` SET `complete` = 1 WHERE `id` = {todo_index}")
    cursor.close()
    connection.commit()
    return redirect('/')

@app.route('/uncomplete_todo/<int:todo_index>', methods=['POST'])
def uncomplete_todo(todo_index):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE `todos` SET `complete` = 0 WHERE `id` = {todo_index}")
    cursor.close()
    connection.commit()
    return redirect('/')