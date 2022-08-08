import re
s = 'joaoantonio@gmail.com.br pedrofpereira222@gmail.com      joaoantonio@gmail.com'
x = '11111111111  11 111113123213213131111 11 98506423432421267 11 98506-1254353454367 11 8553454354354306-1267'
padrao_email = re.compile('[\w]{5,50}[@][\w]{3,5}[.][\w]{1,3}([.][\w]{1,3})?')
print(re.search(padrao_email,s).group())
padrao_cel = '[0-9]{2} [0-9]{4,5}[-]?[0-9]{4}'
print(re.findall(padrao_cel, x))

class Telefone():
    def __init__(self, num):
        num = str(num)
        if self.valida_cel(num):
            self.telefone = num
        else:
            raise ValueError("Número inválido.")

    def valida_cel(self, num):
        padrao = '([0-9]{2,3})([0-9]{2})([ ])?([0-9]{4,5})([-])?([0-9]{4})$'
        x = re.match(padrao, num)
        if x:
            return True
        else:
            return False

    def __str__(self):
        padrao = '([0-9]{2})([0-9]{2})([ ])?([0-9]{4,5})([-])?([0-9]{4})$'
        telefone = re.search(padrao, self.telefone)
        return '+{} {} {}-{}'.format(telefone.group(1), telefone.group(2), telefone.group(4), telefone.group(6))


x1 = Telefone('5511 98506-1267')
print(x1)
print(x1.telefone)