from Datas import Data
from datetime import datetime, timedelta
c1 = Data()
print(c1.momento)
print(c1.mes_cadastro())
print(c1.dia_semana())
print(c1)
hoje = datetime.today()
amanha = datetime.today() + timedelta(days= 1, hours=27)
print(amanha-hoje)
print(c1.tempo_de_cadastro())