
<p align="center">
    <h2 align="center">Flask password verify</h2>
    <a href="https://github.com/jordansaran/flask-password-verify/actions">
      <img alt="Tests Passing" src="https://github.com/jordansaran/flask-password-verify/workflows/Test-Coverage/badge.svg" />
    </a>
    <a href="https://codecov.io/gh/jordansaran/flask-password-verify">
      <img src="https://codecov.io/gh/jordansaran/flask-password-verify/branch/main/graph/badge.svg" />
    </a>
    <a href="https://github.com/jordansaran/flask-password-verify/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/jordansaran/flask-password-verify?color=0088ff" />
    </a>
    <a href="https://github.com/jordansaran/flask-password-verify/pulls">
      <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/jordansaran/flask-password-verify?color=0088ff" />
    </a>
</p>

Foi desenvolvido uma API onde seu objetivo é verificar se um password é válido a partir de um conjunto de regras.
O padrão de comunicação é via JSON, onde a API recebe como entrada um JSON seguindo a seuginte estrutura.
# Instalação
Certifique-se de utilizar a última versão do código fonte, que normalmente fica na branch "main"(principal) do Git.
````shell
# clone o repositório
$ git clone https://github.com/jordansaran/flask-password-verify
$ cd flask-password-verify
````
Crie um virtualenv em ambiente Unix e ative-o:
````shell
$ python3 -m venv venv
$ . venv/bin/activate
````
Ou no Windows cmd:
````shell
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
````
Instalando flask-password-verify
````shell
$ pip install -r requirements.txt
````
Antes de executar a API crie um arquivo **.env** na raiz do projeto caso ele não tenha sido criado.
O arquivo deve conter os seguintes variáveis de ambiente.
````dotenv
SECRET_KEY=
FLASK_DEBUG=1
FLASK_APP="app.py"
````
A variável **SECRET_KEY** deve conter um hash que será utilizado quando a API for utilizada em **production**.
A variável **FLASK_DEBUG** deve possuir o valores 1 ou 0 para referenciar a condição de **True** ou **False** para
executar aplicação em modo **DEBUG**.
A variável **FLASK_APP** é utilizada para destacar qual o arquivo .py deve ser utilizado como referência para executar
a aplicação.
# Executar aplicação
````shell
$ python app.py
````
Abra http://127.0.0.1:5001/api/v1/ui em seu navegador para acessar a documentação da API.
# Teste/Coverage
````shell
$ python pytest
````
Executar com coverage report:
````shell
$ coverage run -m pytest
$ coverage report
$ coverage html  # abrir htmlcov/index.html em um navegador
````
# Utilizar Docker

Para replicar o ambiente de desenvolvimento e colocar em execução a API, execute o comando logo abaixo. 
Destacando que é necessário que seu ambiente de desenvolvimento possua [**Docker**](https://www.docker.com/products/docker-desktop/) instalado.
```
docker-compose up -d
```
## Observações
A url de acesso a API é **http://127.0.0.1:5001/api/v1/ui**, caso deseje alterar a porta de acesso modifique
o arquivo **docker-compose.yml** no parametro **ports** (5001:5001).
# Exemplo de input de dados na API

````
{
    "password": "TesteSenhaForte!123&",
    "rules": [
        {
            "rule": "minSize", "value": 8
        },
        {
            "rule": "minSpecialChars", "value": 2
        },
        {
            "rule": "noRepeted", "value": 0
        },
        {
            "rule": "minDigit", "value": 4
        }¡
    ]
}
````
A API retorna um JSON como resposta com a seguinte estrutura. a chave **verify** retorna se é True ou False para o password
e a chave **noMatch** retorna uma lista conténdo as regras que o password não é válido. 
````
{
  "verify": false,
  "noMatch": [
    "minSpecialChars",
    "minDigit"
  ]
}
````