import os
import threading
from flask import Flask, render_template

# Usa la carpeta temples como carpeta de plantillas
app = Flask(__name__, template_folder="temples")


@app.route("/")
def menu():
    ruta_menu = os.path.join(app.template_folder, "menu.html")
    if not os.path.exists(ruta_menu):
        return f"<h2>Error: no se encontró {ruta_menu}</h2>"
    return render_template("menu.html")


def abrir_navegador():
    os.system("start http://127.0.0.1:5000")


if __name__ == "__main__":
    threading.Timer(1.0, abrir_navegador).start()
    app.run(debug=True)

