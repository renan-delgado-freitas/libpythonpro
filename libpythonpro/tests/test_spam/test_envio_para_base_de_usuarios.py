from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Renan', email='refreitas.ie@gmail.com'),
            Usuario(nome='Agatha', email='refreitas.ie@gmail.com')
        ],
        [
            Usuario(nome='Renan', email='refreitas.ie@gmail.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renanfreeiitas@gmail.com',
        'Cursos Python Pro',
        'Confira os modulos fantásticos do Python!'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renan', email='refreitas.ie@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'agatha@gmail.com',
        'Cursos Python Pro',
        'Confira os modulos fantásticos do Python!'
    )
    enviador.enviar.assert_called_once_with(
        'agatha@gmail.com',
        'refreitas.ie@gmail.com',
        'Cursos Python Pro',
        'Confira os modulos fantásticos do Python!'
    )
