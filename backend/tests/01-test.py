import pytest

from app.controllers.alumni_ctr import get_all_alumni_ctr, get_alumni_ctr, update_alumni_ctr, delete_alumni_ctr
from app.blueprints.alumni import blueprint


@pytest.mark.parametrize('id, expected_status_code, expected_data', [
    (2, 200, {'id': 2, 'nome': 'name', 'ano_formacao': 2023, 'curso': 'SI'}),
    (100, 404, {'mensagem': 'Aluno não encontrado'}),
    ('abc', 400, {'mensagem': 'Formato de ID inválido'}),
])
def test_get_alumni_route(id, expected_status_code, expected_data):
    with blueprint.test_request_context(f'/alumni/{id}'):
        response = blueprint.dispatch_request()

        assert response.status_code == expected_status_code
        assert response.json == expected_data
