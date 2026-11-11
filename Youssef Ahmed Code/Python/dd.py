from flask import Flask, render_template_string, redirect, request
import sqlite3

app = Flask(__name__)

# Initialize Database
def init_db():
    db = sqlite3.connect("database.db")
    db.cursor().execute("""
    CREATE TABLE IF NOT EXISTS employee(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        salary INTEGER
    )
    """)
    db.commit()
    db.close()

init_db()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Database Company</title>
    <link rel="icon" type="image/x-icon" href="https://img.atom.com/story_images/visual_images/logo-image-18348-database.company.jpg">
    <style>
:root {
    --bg-color: #0b0c10;
    --card-bg: rgba(20, 22, 30, 0.85);
    --cyan-glow: #00f0ff;
    --magenta-glow: #ff007f;
    --text-color: #e0e6ed;
    --border-color: rgba(0, 240, 255, 0.3);
}

body {
    background-color: var(--bg-color);
    color: var(--text-color);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 40px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    box-sizing: border-box;
}

.box {
    background: var(--card-bg);
    border: 2px solid var(--cyan-glow);
    border-radius: 16px;
    padding: 30px 40px;
    width: 100%;
    max-width: 500px;
    text-align: center;
    box-shadow: 0 0 20px rgba(0, 240, 255, 0.2), inset 0 0 15px rgba(0, 240, 255, 0.1);
    backdrop-filter: blur(8px);
    margin-bottom: 30px;
}

.box img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid var(--cyan-glow);
    margin-bottom: 15px;
    box-shadow: 0 0 10px var(--cyan-glow);
}

h1 {
    color: #fff;
    font-size: 1.8rem;
    margin-bottom: 20px;
    text-shadow: 0 0 10px var(--cyan-glow);
    letter-spacing: 1px;
}

input[type="text"],
input[type="date"] {
    width: 85%;
    padding: 12px 16px;
    margin: 8px 0;
    background: rgba(10, 14, 23, 0.9);
    border: 1px solid var(--cyan-glow);
    border-radius: 8px;
    color: #fff;
    font-size: 1rem;
    outline: none;
    transition: all 0.3s ease-in-out;
}

input[type="text"]:focus,
input[type="date"]:focus {
    border-color: var(--magenta-glow);
    box-shadow: 0 0 12px var(--magenta-glow);
}

button[type="submit"],
td button {
    background: linear-gradient(135deg, #00f0ff, #7000ff);
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 0.95rem;
    font-weight: bold;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 0 10px rgba(0, 240, 255, 0.4);
}

button[type="submit"]:hover,
td button:hover {
    background: linear-gradient(135deg, #ff007f, #7000ff);
    box-shadow: 0 0 20px rgba(255, 0, 127, 0.8);
    transform: scale(1.03);
}

table {
    background: var(--card-bg);
    border-collapse: collapse;
    border: 2px solid var(--magenta-glow);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 0 25px rgba(255, 0, 127, 0.2);
    width: 90%;
    max-width: 900px;
    margin-top: 10px;
}

th {
    background: rgba(255, 0, 127, 0.2);
    color: #fff;
    padding: 14px;
    font-size: 1.05rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 2px solid var(--magenta-glow);
    text-shadow: 0 0 8px var(--magenta-glow);
}

td {
    padding: 12px 16px;
    text-align: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    color: #fff;
}

tr:hover td {
    background: rgba(0, 240, 255, 0.04);
}

.delete-btn {
    color: #ff4757;
    text-decoration: none;
    font-weight: bold;
    padding: 6px 12px;
    border: 1px solid #ff4757;
    border-radius: 6px;
    transition: all 0.3s ease;
    display: inline-block;
}

.delete-btn:hover {
    background: #ff4757;
    color: #fff;
    box-shadow: 0 0 12px #ff4757;
}

td button[type="button"] {
    background: transparent;
    border: 1px solid var(--cyan-glow);
    color: var(--cyan-glow);
    padding: 6px 14px;
    margin-right: 6px;
}

td button[type="button"]:hover {
    background: var(--cyan-glow);
    color: #000;
    box-shadow: 0 0 12px var(--cyan-glow);
}
    </style>
</head>
<body>
    <div class="box">
        <img src="https://img.atom.com/story_images/visual_images/logo-image-18348-database.company.jpg" alt="Logo">
        <h1>Company Database</h1>
        <form action="/add" method="POST">
            <input name="Name" type="text" placeholder="Enter your Name" required><br><br>
            <input name="Salary" type="date" placeholder="Enter your Date" required><br><br>
            <button type="submit">Submit</button>
        </form>
    </div>
    <br> 
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Salary / Date</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for employee in employees %}
            <tr id="row-{{ employee[0] }}">
                <form action="/update/{{ employee[0] }}" method="POST">
                    <td>{{ employee[0] }}</td>
                    <td>
                        <span class="view_mode">{{ employee[1] }}</span>
                        <input name="Name" class="edit_mode" type="text" value="{{ employee[1] }}" style="display:none;" required>
                    </td>
                    <td> 
                        <span class="view_mode">{{ employee[2] }}</span>
                        <input name="Salary" class="edit_mode" type="date" value="{{ employee[2] }}" style="display:none;" required>
                    </td>
                    <td>
                        <button type="submit" class="edit_mode" style="display:none;">Save</button>
                        <button type="button" class="view_mode" onclick="edit('row-{{ employee[0] }}')">Edit</button>
                        <a href="/delete/{{ employee[0] }}" onclick="return confirm('Are you sure that you want to delete this record?')" class="delete-btn">Delete</a>
                    </td>
                </form>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <script>
function edit(rowId) {
    const row = document.getElementById(rowId);
    const viewElements = row.querySelectorAll(".view_mode");
    const editElements = row.querySelectorAll(".edit_mode");

    viewElements.forEach(element => element.style.display = 'none');
    editElements.forEach(element => element.style.display = 'inline-block');
}
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    cursor.execute("SELECT id, name, salary FROM employee")
    employees = cursor.fetchall()
    db.close()
    return render_template_string(HTML_TEMPLATE, employees=employees)

@app.route("/add", methods=['POST'])
def add():
    name = request.form['Name']
    salary = request.form['Salary']
    db = sqlite3.connect("database.db")
    db.cursor().execute("INSERT INTO employee (name, salary) VALUES (?, ?)", (name, salary))
    db.commit()
    db.close()
    return redirect("/")

@app.route("/delete/<id>", methods=['GET', 'POST'])
def delete(id):
    db = sqlite3.connect("database.db")
    db.cursor().execute("DELETE FROM employee WHERE id = ?", (id,))
    db.commit()
    db.close()
    return redirect("/")

@app.route("/update/<id>", methods=['POST'])
def update(id):
    name = request.form['Name']
    salary = request.form['Salary']
    db = sqlite3.connect("database.db")
    db.cursor().execute("UPDATE employee SET name = ?, salary = ? WHERE id = ?", (name, salary, id))
    db.commit()
    db.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)