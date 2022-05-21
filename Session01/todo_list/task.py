from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, content):
        self.content = content
        self.done = False

    def __repr__(self):
        return '<Content %s>' % self.content


db.create_all()


@app.route('/')
def task_list():
    tasks = Task.query.all()  # todo "select * from task"
    return render_template("list_task.html", tasks=tasks)


@app.route('/task',methods=['POST'])
def add_task():
    content = request.form['content']
    if not content:
        return 'Error'
    task = Task(content)
    db.session.add(task)
    db.session.commit()
    return redirect('/')


@app.route('/done/<int:task_id>')
def status_task(task_id):
    task= Task.query.get(task_id)

    if not task:
        return redirect('/')
    if task.done:
        task.done = False
    else:
        task.done = True

    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return redirect('/')

    db.session.delete(task) #todo delete from tarea id=1
    db.session.commit()
    return redirect('/')





if __name__ == '__main__':
    app.run(debug=True)
