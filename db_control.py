import psycopg2, config

def connect_db():
    """Function to connect to the database of this project"""
    try:
        # Perform the connection
        connection = psycopg2.connect(
            host = "localhost",
            database = "tasks_manager",
            user = config.DB_USER,
            password = config.DB_PASSWORD
        )
        return connection
    except psycopg2.Error as e:
        print("There was an error trying to connect to the database: {}".format(e))
        return None

def add_user(username, email):
    """Function to add a user to the database"""
    # Connect to the DB and obtain the cursor
    connection = connect_db()
    cursor = connection.cursor()

    # Insert the data received into the DB
    try:
        cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
        connection.commit()
        print("User inserted: {}".format(username))
    # Rollback if there was an error
    except Exception as e:
        print("Error while adding a user: {}".format(e))
        connection.rollback()
    # Close the cursor and connection once finished
    finally:
        cursor.close()
        connection.close()

def add_project(name, description):
    """Function to insert a project into the database"""
    # Connect to the DB and obtain the cursor
    connection = connect_db()
    cursor = connection.cursor()

    # Insert the data received into the DB
    try:
        cursor.execute("INSERT INTO projects (p_name, p_description) VALUES (%s, %s)", (name, description))
        connection.commit()
        print("Project inserted: {}".format(name))
    # Rollback if there was an error
    except Exception as e:
        print("Error while adding a project: {}".format(e))
        connection.rollback()
    # Close the cursor and connection once finished
    finally:
        cursor.close()
        connection.close()

def add_task(title, description, project_id, user_id, due_date):
    """Function to insert a task into the database"""
    # Connect to the DB and obtain the cursor
    connection = connect_db()
    cursor = connection.cursor()

    # Insert the data received into the DB
    try:
        cursor.execute(
            "INSERT INTO tasks (title, t_description, project_id, t_user_id, due_date) VALUES (%s, %s, %s, %s, %s)",
            (title, description, project_id, user_id, due_date)
        )
        connection.commit()
        print("Task inserted: {}".format(title))
    # Rollback if there was an error
    except Exception as e:
        print("Error while adding a task: {}".format(e))
        connection.rollback()
    # Close the cursor and connection once finished
    finally:
        cursor.close()
        connection.close()

def get_users():
    """Function to get all the users in the database"""
    # Connect to the DB and obtain the cursor
    connection = connect_db()
    cursor = connection.cursor()

    # Select all the users
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return users
    # Notify if there was an error
    except Exception as e:
        print("Error while reading the users: {}".format(e))
        return []
    # Close the cursor and connection once finished
    finally:
        cursor.close()
        connection.close()

def get_projects():
    """Function to get all the projects in the database"""
    # Connect to the DB and obtain the cursor
    connection = connect_db()
    cursor = connection.cursor()

    # Select all the projects
    try:
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall()
        return projects
    # Notify if there was an error
    except Exception as e:
        print("Error while reading the projects: {}".format(e))
        return []
    # Close the cursor and connection once finished
    finally:
        cursor.close()
        connection.close()

def get_tasks():
    """Function to get all the tasks in the database"""
    # Connect to the DB and obtain the cursor
    connection = connect_db()
    cursor = connection.cursor()

    # Select all the tasks
    try:
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        return tasks
    # Notify if there was an error
    except Exception as e:
        print("Error while reading the tasks: {}".format(e))
        return []
    # Close the cursor and connection once finished
    finally:
        cursor.close()
        connection.close()

def get_user_from_id(user_id):
    """Function to get a user from it's ID"""
    # Connect to the DB and obtain the cursor
    connection = connect_db()
    cursor = connection.cursor()

    # Select the user
    try:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        return user
    # Notify if there was an error
    except Exception as e:
        print("Error while reading a user from it's ID: {}".format(e))
        return None
    # Close the cursor and connection once finished
    finally:
        cursor.close()
        connection.close()

def get_project_from_id(project_id):
    """Function to get a project from it's ID"""
    # Connect to the DB and obtain the cursor
    connection = connect_db()
    cursor = connection.cursor()

    # Select the project
    try:
        cursor.execute("SELECT * FROM projects WHERE id = %s", (project_id,))
        project = cursor.fetchone()
        return project
    # Notify if there was an error
    except Exception as e:
        print("Error while reading a project from it's ID: {}".format(e))
        return None
    # Close the cursor and connection once finished
    finally:
        cursor.close()
        connection.close()

def get_task_from_id(task_id):
    """Function to get a task from it's ID"""
    # Connect to the DB and obtain the cursor
    connection = connect_db()
    cursor = connection.cursor()

    # Select the task
    try:
        cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
        task = cursor.fetchone()
        return task
    # Notify if there was an error
    except Exception as e:
        print("Error while reading a task from it's ID: {}".format(e))
        return None
    # Close the cursor and connection once finished
    finally:
        cursor.close()
        connection.close()
