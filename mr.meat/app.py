from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Necesario para manejar sesiones

DATABASE = 'data/menu.db'

def init_db():
    if not os.path.exists('data'):
        os.makedirs('data')
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS menu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    categoria TEXT NOT NULL,
                    nombre TEXT NOT NULL,
                    precio REAL NOT NULL
                )''')
    
    menu_items = [
        ('TRUCHAS', "TRUCHA A LA PARRILLA", 65.00),
        ('PARRILLAS', "PARRILLA PARA 1 PERSONA", 90.00),
        ('PORCIONES EXTRA', "ARROZ CON QUESO", 12.00),
        ('PLATOS FUERTES', "PICAÑA", 85.00),
        ('CORTES NACIONALES', "CUADRIL", 90.00),
        ('PASTAS', "FETUCCINI AL PESTO", 65.00),
        ('ESPECIALIDAD DEL CHEF', "MILANESA NAPOLITANA", 80.00),
        ('POSTRES', "FRAPEADO DE FRUTA DE TEMPORADA", 20.00),
        ('BEBIDAS', "COCA COLA", 20.00),
        ('JUGOS', "JUGO DE LIMON", 30.00),
        ('TES', "CAFE", 7.00),
        ('CERVEZAS', "PACEÑA", 28.00),
        ('VINOS', "VINO TANAT", 20.00),
        ('LICORES', "FERNET", 20.00)
    ]

    c.executemany('INSERT INTO menu (categoria, nombre, precio) VALUES (?, ?, ?)', menu_items)
    conn.commit()
    conn.close()

init_db()

# Función para obtener todos los elementos del menú
def get_menu_items():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT id, categoria, nombre, precio FROM menu')
    menu_items = c.fetchall()
    conn.close()
    return menu_items

# Ruta para mostrar el menú en la plantilla typography.html
@app.route('/typography.html')
def typography():
    menu_items = get_menu_items()
    return render_template('typography.html', menu_items=menu_items)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
