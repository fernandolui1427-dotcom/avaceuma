from app import app

cliente = app.test_client()


def test_tasks():
    response = cliente.get("/")
    assert response.status_code == 200
    assert len(response.json) == 2


def test_conteudo_das_tarefas():
    response = cliente.get("/")
    assert response.json == [
        {"id": 1, "title": "Estudar Docker"},
        {"id": 2, "title": "Criar o pipeline"},
    ]


def test_retorno_em_json():
    response = cliente.get("/")
    assert response.is_json
    assert response.content_type.startswith("application/json")
