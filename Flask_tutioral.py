from flask import Flask, render_template, request

app = Flask(__name__)
username = input('Enter name| ')
@app.route("/")
def home():
    return render_template('Coding_Portfolio.html', name=username)

if __name__ == "__main__":
    app.run(debug=True)

