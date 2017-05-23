from flask import Flask, render_template

class CustomFlask(Flask):
	jinja_options = Flask.jinja_options.copy()
	jinja_options.update(dict(
		block_start_string='{%',
		block_end_string='%}',
		variable_start_string='((',
		variable_end_string='))',
		comment_start_string='{#',
		comment_end_string='#}',
	))

app = CustomFlask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/todo")
def todo():
    return render_template('todo.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')