from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador)
    enviador_de_spam.enviar_emails(
        'renanfreeiitas@gmail.com',
        'Cursos Python Pro',
        'Confira os modulos fantásticos do Python!'
    )
