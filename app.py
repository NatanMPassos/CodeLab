from flask import Flask, request
import json

# Flask(): Inicializa a aplicação Flask
app = Flask(__name__)

# @app.route(): Define a rota/caminho que o usuário vai acessar.
# Nesse caso, a rota "/" representa a página inicial.
@app.route("/")
def home():
    # return: Retorna a resposta que será exibida no navegador do usuário.
    return "<h1>hello world</h1>"

@app.route("/exercise/<int:id>", methods=['GET', 'POST'])
def exercise(id):
    with open('exercises.json', 'r', encoding='utf-8') as file:
        exercises_list = json.load(file)
    exercise_dictionary = next((item for item in exercises_list if item['id'] == id), None)
    if exercise_dictionary is None:
        return "Exercise not found", 404

    if request.method == 'POST':
        code = request.form['code']
        print(code)
        return "Code received"
    else:
        return f"""
        <h2>{exercise_dictionary['exercise']}</h2>
        <form method="POST">
            <textarea name="code"></textarea>
            <button type="submit">Enviar</button>
        </form>
        """

# app.run(): Executa o servidor de desenvolvimento local
if __name__ == "__main__":
    app.run(debug=True)

