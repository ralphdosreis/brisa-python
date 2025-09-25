from flask import Flask

app = Flask(__name__)

@app.route('/')
def boas_vindas():
    return 'Bem vindos alunos'

if __name__ == '__main__':
    app.run()