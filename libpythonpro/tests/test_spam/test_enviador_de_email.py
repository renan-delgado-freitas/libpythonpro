import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['renanfreeiitas@gmail.com', 'refreitas.ie@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()

    resultado = enviador.enviar(
        remetente,
        'renanfreeiitas@gmail.com',
        'Cursos Python Pro',
        'Primeiro turma Guido Von Rossum aberta'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'refreitas.ie']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'renanfreeiitas@gmail.com',
            'Cursos Python Pro',
            'Primeiro turma Guido Von Rossum aberta'
        )






