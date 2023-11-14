from libpythonpro.spam.modelos import Usuario
from libpythonpro.tests.test_spam.conftest import sessao


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Renan')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Renan'), Usuario(nome='Agatha')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

