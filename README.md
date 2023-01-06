# flask-password-verify

Foi desenvolvido uma API onde seu objetivo é verificar se um password é válido a partir de um conjunto de regras.
O padrão de comunicação é via JSON, onde a API recebe como entrada um JSON seguindo a seuginte estrutura.

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
        }
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

Para replicar o ambiente de desenvolvimento e colocar em execução a API, execute o comando logo abaixo. 
Destacando que é necessário que seu ambiente de desenvolvimento possua **Docker** instalado.
```
docker-compose up -d
```

Para executar o ambiente de desenvolvimento a partir do container execute o seguinte comando
```

```

A url de acesso a API é **http://127.0.0.1:5001/api/v1/ui**, caso deseje alterar a porta de acesso modifique
o arquivo **docker-compose.yml** no parametro **ports** (5001:5000).