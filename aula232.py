from abc import ABC, abstractmethod

class Notificaçao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        
    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificaçaoEmail(Notificaçao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True

class NotificaçaoSMS(Notificaçao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False    # apenas para fins didáticos/exemplo

def notificar(notificacao: Notificaçao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')    
    else:
        print('Notificação NÃO enviada')    
        
notificacao_email = NotificaçaoEmail('Testando por e-mail')
notificar(notificacao_email)

notificacao_sms = NotificaçaoSMS('Testando por SMS')
notificar(notificacao_sms)