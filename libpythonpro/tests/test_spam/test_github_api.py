from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'renan-delgado-freitas', 'id': 135972069, 'node_id': 'U_kgDOCBrE5Q',
        'avatar_url': 'https://avatars.githubusercontent.com/u/135972069?v=4', 'gravatar_id': '',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('renan-delgado-freitas')
    assert 'https://avatars.githubusercontent.com/u/135972069?v=4' == url
