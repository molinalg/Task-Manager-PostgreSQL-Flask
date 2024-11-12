from flask import Flask, render_template, request, redirect, url_for
from db_control import add_user, add_project, add_task, get_users, get_projects, get_tasks

app = Flask(__name__)

# Route to main screen
@app.route('/')
def index():
    return render_template('index.html')

# Route to total users screen
@app.route('/users')
def users():
    total_users = get_users()
    return render_template('users.html', users=total_users)

# Route to total projects screen
@app.route('/projects')
def projects():
    total_projects = get_projects()
    return render_template('projects.html', projects=total_projects)

# Route to total tasks screen
@app.route('/tasks')
def tasks():
    total_tasks = get_tasks()
    return render_template('tasks.html', tasks=total_tasks)

# Route to add users screen
@app.route('/add_user', methods=['GET', 'POST'])
def add_user_route():
    # Process entries from the form to insert into the DB
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        add_user(username, email)
        return redirect(url_for('users'))
    return render_template('add_user.html')

# Route to add projects screen
@app.route('/add_project', methods=['GET', 'POST'])
def add_project_route():
    # Process entries from the form to insert into the DB
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        add_project(name, description)
        return redirect(url_for('projects'))
    return render_template('add_project.html')

# Route to add tasks screen
@app.route('/add_task', methods=['GET', 'POST'])
def add_task_route():
    # Process entries from the form to insert into the DB
    if request.method == 'POST':
        title = request.form['title']
        t_description = request.form['t_description']
        project_id = request.form['project_id']
        t_user_id = request.form['t_user_id']
        due_date = request.form['due_date']
        add_task(title, t_description, project_id, t_user_id, due_date)
        return redirect(url_for('tasks'))
    return render_template('add_task.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
