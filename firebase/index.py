from flask import Flask
from db import DB
from flask import request

app = Flask(__name__)

@app.route('/todo/api/v1.0/tasks')
def index():
    data=DB().get_all().val()
    if(not data):
       return "No tasks found"

    return str(data)

@app.route('/todo/api/v1.0/tasks/<task_id>')
def get_task(task_id):
    data=DB().get_task(task_id).val()
    if(not data):
       return "No tasks found"

    return str(data)

@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def add_task():
    id=request.json['id']
    title=request.json['title']
    desc=request.json['description']
    done=request.json['done']
    DB().addToDo(id,desc,title,done)
    return 'The task is created successfully\n'


@app.route('/todo/api/v1.0/tasks/<task_id>', methods = ['PUT'])
def update_task(task_id):
    title=request.json['title']
    desc=request.json['description']
    done=request.json['done']
    DB().update_task(task_id,desc,title,done)
    return 'The task is updated successfully\n'

@app.route('/todo/api/v1.0/tasks/<task_id>', methods = ['DELETE'])
def delete_task(task_id):
    DB().remove_task(task_id)
    return 'The task is removed successfully\n'


if __name__ == '__main__':
    app.run(debug=True)