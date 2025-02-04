# %% [markdown]
# # Module: SQLite3 Assignments
# ## Lesson: SQLite3
# ### Assignment 1: Creating and Connecting to a Database
# 
# 1. Write a Python function to create a new SQLite3 database named `test.db`.

# %%
import sqlite3

def create_database():
    conn = sqlite3.connect('test.db')
    conn.close()
    print("Database created and successfully connected.")

# Test the function
create_database()

# %% [markdown]
# 2. Write a Python function to create a table named `employees` with columns `id` (integer), `name` (text), `age` (integer), and `department` (text) in the `test.db` database.

# %%
def create_table():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Table 'employees' created successfully.")

# Test the function
create_table()

# %% [markdown]
# ### Assignment 2: Inserting Data
# 
# 1. Write a Python function to insert a new employee into the `employees` table.

# %%
def insert_employee(id, name, age, department):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (id, name, age, department)
        VALUES (?, ?, ?, ?)
    ''', (id, name, age, department))
    conn.commit()
    conn.close()
    print("Employee inserted successfully.")

# Test the function
insert_employee(1, 'Alice', 30, 'HR')

# %% [markdown]
# 2. Insert at least 5 different employees into the `employees` table.

# %%
# Insert 5 different employees
insert_employee(2, 'Bob', 25, 'Engineering')
insert_employee(3, 'Charlie', 28, 'Sales')
insert_employee(4, 'David', 35, 'Marketing')
insert_employee(5, 'Eve', 22, 'HR')

# %% [markdown]
# ### Assignment 3: Querying Data
# 
# 1. Write a Python function to fetch and display all records from the `employees` table.

# %%
def fetch_all_employees():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    records = cursor.fetchall()
    conn.close()
    for record in records:
        print(record)

# Test the function
fetch_all_employees()

# %% [markdown]
# 2. Write a Python function to fetch and display all employees from a specific department.

# %%
def fetch_employees_by_department(department):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE department = ?', (department,))
    records = cursor.fetchall()
    conn.close()
    for record in records:
        print(record)

# Test the function
fetch_employees_by_department('HR')

# %% [markdown]
# ### Assignment 4: Updating Data
# 
# 1. Write a Python function to update the department of an employee based on their `id`.

# %%
def update_employee_department(employee_id, new_department):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE employees
        SET department = ?
        WHERE id = ?
    ''', (new_department, employee_id))
    conn.commit()
    conn.close()
    print("Employee department updated successfully.")

# Test the function
update_employee_department(1, 'Finance')

# %% [markdown]
# 2. Update the department of at least 2 employees and display the updated records.

# %%
# Update the department of 2 employees
update_employee_department(2, 'Research')
update_employee_department(3, 'Customer Support')

# Fetch and display all records
fetch_all_employees()

# %% [markdown]
# ### Assignment 5: Deleting Data
# 
# 1. Write a Python function to delete an employee from the `employees` table based on their `id`.

# %%
def delete_employee(employee_id):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM employees
        WHERE id = ?
    ''', (employee_id,))
    conn.commit()
    conn.close()
    print("Employee deleted successfully.")

# Test the function
delete_employee(5)

# %% [markdown]
# 2. Delete at least 1 employee and display the remaining records.

# %%
# Delete an employee
delete_employee(4)

# Fetch and display all records
fetch_all_employees()

# %% [markdown]
# ### Assignment 6: Advanced Queries
# 
# 1. Write a Python function to fetch and display employees older than a certain age.

# %%
def fetch_employees_older_than(age):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE age > ?', (age,))
    records = cursor.fetchall()
    conn.close()
    for record in records:
        print(record)

# Test the function
fetch_employees_older_than(25)

# %% [markdown]
# 2. Write a Python function to fetch and display employees whose names start with a specific letter.

# %%
def fetch_employees_name_starts_with(letter):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE name LIKE ?', (letter + '%',))
    records = cursor.fetchall()
    conn.close()
    for record in records:
        print(record)

# Test the function
fetch_employees_name_starts_with('A')

# %% [markdown]
# ### Assignment 7: Handling Transactions
# 
# 1. Write a Python function to insert multiple employees into the `employees` table in a single transaction. Ensure that if any insertion fails, none of the insertions are committed.

# %%
def insert_multiple_employees(employees):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    try:
        cursor.executemany('''
            INSERT INTO employees (id, name, age, department)
            VALUES (?, ?, ?, ?)
        ''', employees)
        conn.commit()
        print("All employees inserted successfully.")
    except Exception as e:
        conn.rollback()
        print("Error occurred, transaction rolled back.")
        print(e)
    finally:
        conn.close()

# Test the function with valid and invalid data
employees = [
    (6, 'Frank', 40, 'Finance'),
    (7, 'Grace', 29, 'Engineering'),
    (8, 'Hannah', 35, 'Marketing'),
    (9, 'Ivan', 38, 'Sales'),
    (6, 'Jack', 45, 'HR')  # Duplicate ID to cause an error
]
insert_multiple_employees(employees)

# %% [markdown]
# 2. Write a Python function to update the age of multiple employees in a single transaction. Ensure that if any update fails, none of the updates are committed.

# %%
def update_multiple_employees_ages(updates):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    try:
        cursor.executemany('''
            UPDATE employees
            SET age = ?
            WHERE id = ?
        ''', updates)
        conn.commit()
        print("All employee ages updated successfully.")
    except Exception as e:
        conn.rollback()
        print("Error occurred, transaction rolled back.")
        print(e)
    finally:
        conn.close()

# Test the function with valid and invalid data
updates = [
    (32, 1),
    (26, 2),
    (33, 3),
    (41, 4),  # Non-existing ID to cause an error
    (23, 5)
]
update_multiple_employees_ages(updates)

# %% [markdown]
# ### Assignment 8: Creating Relationships
# 
# 1. Create a new table named `departments` with columns `id` (integer) and `name` (text).

# %%
def create_departments_table():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Table 'departments' created successfully.")

# Test the function
create_departments_table()

# %% [markdown]
# 2. Modify the `employees` table to include a foreign key referencing the `id` column in the `departments` table.

# %%
def add_department_foreign_key():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        PRAGMA foreign_keys=off;
        BEGIN TRANSACTION;
        ALTER TABLE employees RENAME TO old_employees;
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT,
            department_id INTEGER,
            FOREIGN KEY(department_id) REFERENCES departments(id)
        );
        INSERT INTO employees (id, name, age, department)
        SELECT id, name, age, department FROM old_employees;
        DROP TABLE old_employees;
        COMMIT;
        PRAGMA foreign_keys=on;
    ''')
    conn.commit()
    conn.close()
    print("Table 'employees' modified successfully.")

# Test the function
add_department_foreign_key()

# %% [markdown]
# 3. Write a Python function to insert data into both the `departments` and `employees` tables, ensuring referential integrity.

# %%
def insert_department_and_employee(department_id, department_name, employee_id, name, age, department):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO departments (id, name)
            VALUES (?, ?)
        ''', (department_id, department_name))
        cursor.execute('''
            INSERT INTO employees (id, name, age, department, department_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (employee_id, name, age, department, department_id))
        conn.commit()
        print("Department and employee inserted successfully.")
    except Exception as e:
        conn.rollback()
        print("Error occurred, transaction rolled back.")
        print(e)
    finally:
        conn.close()

# Test the function
insert_department_and_employee(1, 'Finance', 10, 'Zara', 28, 'Finance')

# %% [markdown]
# ### Assignment 9: Indexing and Optimization
# 
# 1. Create an index on the `name` column of the `employees` table.

# %%
def create_index_on_name():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('CREATE INDEX idx_name ON employees(name)')
    conn.commit()
    conn.close()
    print("Index on 'name' column created successfully.")

# Test the function
create_index_on_name()

# %% [markdown]
# 2. Write a Python function to fetch and display all employees whose names start with a specific letter. Compare the performance with and without the index.

# %%
import time

def fetch_employees_name_starts_with_performance(letter):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    start_time = time.time()
    cursor.execute('SELECT * FROM employees WHERE name LIKE ?', (letter + '%',))
    records = cursor.fetchall()
    end_time = time.time()
    conn.close()
    print("Time taken: {} seconds".format(end_time - start_time))
    for record in records:
        print(record)

# Test the function with the index
fetch_employees_name_starts_with_performance('A')

# %% [markdown]
# ### Assignment 10: Backing Up and Restoring Data
# 
# 1. Write a Python function to back up the `test.db` database to a file named `backup.db`.

# %%
import shutil

def backup_database():
    shutil.copy('test.db', 'backup.db')
    print("Database backed up successfully.")

# Test the function
backup_database()

# %% [markdown]
# 2. Write a Python function to restore the `test.db` database from the `backup.db` file.

# %%
def restore_database():
    shutil.copy('backup.db', 'test.db')
    print("Database restored successfully.")

# Test the function
restore_database()


