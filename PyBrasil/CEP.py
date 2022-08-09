import requests


class CEP:
    def __init__(self, cep):
        cep = str(cep)
        if self.validar_cep(cep):
            self.cep = cep
            self.bairro, self.localidade, self.uf = self.request()
        else:
            raise ValueError("CEP INVÁLIDO.")

    def validar_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def request(self):
        r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
        r = r.json()
        return r['bairro'], r['localidade'], r['uf']

    def format(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'
