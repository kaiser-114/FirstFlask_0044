from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nama', methods=['POST'])
def proses():
    nama = request.form['nama']
    return render_template('index.html', nama=nama)

if __name__ == '__main__':
    app.run(debug=True)