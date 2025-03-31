from flask import Flask, render_template, request
from db_config import get_connection  # your SQL Server config

#chat template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('your-html-file.html')  # must be in templates/

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

    return "Submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
