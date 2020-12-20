from flask import Flask, request, render_template, redirect, url_for
from forms import TodoForm
from models import todos

app = Flask(__name__)

app.config["SECRET_KEY"] = "make_it_rain"

@app.route("/todos/", methods=["GET", "POST"])
def todos_list():
    form = TodoForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            todos.create(tuple(form.data.values())[:3])
        return redirect(url_for("todos_list"))

    return render_template("todos.html", form=form, todos=todos.all(), error=error)


@app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
def todo_details(todo_id):
    todo = todos.get(todo_id)
    
    todo_dict = {
        'title' : todo[1],
        'description' : todo[2],
        'done' : todo[3]
    }
    
    form = TodoForm(data=todo_dict)

    if request.method == "POST":
        if form.validate_on_submit():
            todos.update(todo_id, tuple(form.data.values())[:3])
        return redirect(url_for("todos_list"))
    return render_template("todo.html", form=form, todo_id=todo_id)


if __name__ == "__main__":
    app.run(debug=True)