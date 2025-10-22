from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/climate_change')
def climate_change():
    return render_template('climate_change.html')


@app.route('/deforestation')
def deforestation():
    return render_template('deforestation.html')


@app.route('/pollution')
def pollution():
    return render_template('pollution.html')


if __name__ == '__main__':
    app.run(debug=True)
