from flask import Flask

# Cria uma instância do Flask
app = Flask(__name__)

# Define a rota "/" e o método de requisição "GET"
@app.route('/')
def hello():
    return "Hello, World!"

# Inicia a aplicação web na porta 5000 (ou em outra porta, se especificada)
if __name__ == '__main__':
    app.run(port=5000)
