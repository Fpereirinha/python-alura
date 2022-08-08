from validate_docbr import CPF as cpf
from validate_docbr import CNPJ


class CPF_CNPJ:
    def __init__(self, documento):
        tamanho = len(str(documento))
        if self.valida_documento(documento):
            self.cpf = str(documento)
        elif self.valida_cnpj(documento):
            self.cnpj = str(documento)

        else:
            if tamanho == 11:
                raise ValueError('Cpf inválido.')
            elif tamanho == 14:
                raise ValueError('CNPJ inválido.')
            else: raise ValueError('Quantidade de digitos inválida.')

    def __str__(self):
        if hasattr(self, 'cnpj'):
            return self.formatar_cnpj()
        else:
            return self.formatar_cpf()

    def valida_documento(self, documento):
        if len(str(documento)) == 11:
            valida = cpf()
            return valida.validate(str(documento))

    def formatar_cpf(self):
        # ou faria instanciado masking = cpf()
        # masking.mask(self.cpf)
        return cpf().mask(self.cpf)

    def formatar_cnpj(self):
        return CNPJ().mask(self.cnpj)

    def valida_cnpj(self, cnpj):
        if len(str(cnpj)) == 14:
            validator = CNPJ()
            return validator.validate(str(cnpj))
