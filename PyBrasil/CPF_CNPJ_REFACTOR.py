from validate_docbr import CPF as cpf
from validate_docbr import CNPJ as cnpj
class Documento:
    @staticmethod
    def cria_documento(documento):
        tamanho = len(str(documento))
        if tamanho == 11:
            return CPF(documento)
        elif tamanho == 14:
            return CNPJ(documento)
        else:
            raise ValueError("Dado digitado inválido. (quantidade)")


class CPF():
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_doc(documento):
            self.doc = documento
        else:
            raise ValueError("Cpf inválido.")

    def valida_doc(self, documento):
        return cpf().validate(documento)

    def __str__(self):
        return self.masking_doc()

    def masking_doc(self):
        return cpf().mask(self.doc)


class CNPJ():
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_doc(documento):
            self.doc = documento
        else:
            raise ValueError("CNPJ inválido.")

    def valida_doc(self, documento):
        return cnpj().validate(documento)

    def __str__(self):
        return self.masking_doc()

    def masking_doc(self):
        return cnpj().mask(self.doc)

cpf1 = Documento.cria_documento(473018048822222)
print(cpf1)