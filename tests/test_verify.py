password_false = {
    "password": "TesteSenhaForte!123&",
    "rules": [
        {
            "rule": "minSize", "value": 8
        },
        {
            "rule": "minSpecialChars", "value": 8
        },
        {
            "rule": "noRepeted", "value": 0
        },
        {
            "rule": "minDigit", "value": 8
        }
    ]
}

response_password_false = {
    "verify": "False",
    "noMatch": [
        "minSpecialChars",
        "minDigit"
    ]
}

password_true = {
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
            "rule": "minDigit", "value": 3
        }
    ]
}

response_password_true = {
    "verify": "True",
    "noMatch": []
}


def test_verify_is_false(client, app):
    with app.app_context():
        response = client.post("api/v1/verify", json=password_false)
        assert response.json == response_password_false
        assert response.status_code == 200


def test_verify_is_true(client, app):
    with app.app_context():
        response = client.post("api/v1/verify", json=password_true)
        assert response.json == response_password_true
        assert response.status_code == 200
