data = {
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

response_data = {
    "verify": "False",
    "noMatch": [
        "minSpecialChars",
        "minDigit"
    ]
}


def test_verify_is_false(client, app):
    with app.app_context():
        response = client.post("api/v1/verify", json=data)
        assert response.json == response_data
        assert response.status_code == 200
