from flask import Flask  # Necesario para comenzar el proyecto.
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    return '<h1>Hello!</h1>'

# Añadir al final del proyecto
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)