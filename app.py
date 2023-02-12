from flask import Flask, request, render_template

app = Flask(__name__)
todos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        todos.append(task)

    return render_template("index.html", todos=todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0')