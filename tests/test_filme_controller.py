import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_obter_dados(client):
    response = client.get('/dados')
    assert response.status_code == 200  # Verifica se a resposta é bem-sucedida (código 200)

    # Verifica se o tipo de conteúdo da resposta é JSON
    assert response.content_type == 'application/json'

    # Verifica o conteúdo da resposta (você pode ajustar isso com base nos dados esperados)
    data = json.loads(response.get_data(as_text=True))
    assert isinstance(data, list)  # Verifica se os dados são uma lista

    # Adicione mais verificações com base na estrutura esperada dos dados
    # Exemplo: assert 'Year' in data[0]  # Verifica se 'Year' está presente no primeiro item

if __name__ == '__main__':
    pytest.main()
