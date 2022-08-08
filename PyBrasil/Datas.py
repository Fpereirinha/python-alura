from datetime import datetime, timedelta


class Data():
    def __init__(self):
        self.momento = datetime.today()

    def mes_cadastro(self):
        meses = ['Janeiro',
                 'Fevereiro',
                 'Março',
                 'Abril',
                 'Maio',
                 'Junho',
                 'Julho',
                 'Agosto',
                 'Setembro',
                 'Outubro',
                 'Novembro',
                 'Dezembro']
        mes_cadastro = self.momento.month
        return meses[mes_cadastro-1]

    def __str__(self):
        return f'Usuário cadastrado em {self.mes_cadastro()} {self.dia_semana()}  data : {self.formatacao()}'

    def formatacao(self):
        return self.momento.strftime('%d/%m/%Y    %H:%M')

    def dia_semana(self):
        week = ['Segunda','Terça','Quarta','Quinta','Sexta','Sabado','Domingo']
        dia = self.momento.weekday()
        return week[dia]

    def tempo_de_cadastro(self):
        return (datetime.today() + timedelta(days=2)) - self.momento
