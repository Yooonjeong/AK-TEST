from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

tasks = []
next_id = 1


@app.route("/", methods=["GET", "POST"])
def index():
    global next_id

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            tasks.append({"id": next_id, "title": title, "completed": False})
            next_id += 1
        return redirect(url_for("index"))

    return render_template("index.html", tasks=tasks)


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
