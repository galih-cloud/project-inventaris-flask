from flask import Flask, render_template

app = Flask(__name__)

# Route untuk Halaman Dashboard (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# Route untuk Halaman Data Inventaris (tables.html)
@app.route('/tables')
def tables():
    return render_template('tables.html')

# Route untuk Halaman Login (login.html)
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)