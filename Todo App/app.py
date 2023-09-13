from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    task_list = [{'index': i, 'task': task} for i, task in enumerate(tasks)]
    return render_template('index.html', task_list=task_list)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_index>')
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
