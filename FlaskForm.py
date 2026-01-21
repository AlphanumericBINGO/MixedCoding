from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("FirstFlaskForm.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    age = request.form["age"]
    return render_template("FirstFlaskForm.html", name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)
