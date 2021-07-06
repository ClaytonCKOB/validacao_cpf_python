# O cálculo do cadastro de pessoa física (cpf) é padronizado. Logo, 
# as linhas de código a seguir buscam executá-lo para verificar sua 
# validade.

class Cpf:
    def __init__(self, cpf): #Módulo Construtor
        self.cpf = cpf
    
    def filtro_de_valores(self, cpf):
        if len(cpf) > 14:
            print("Número de caracteres inseridos ultrapassou o permitido.")
        elif not cpf in "0123456789.-":
            print("Valores inseridos não são permitidos.")

    def separar(self, cpf): #Módulo que fragmenta o cpf
        lista = []
        for numero in cpf:
            if numero in ".-":
                continue
            else:
                lista.append(numero)
        return lista
    
    def calculo_d1(self, lista): #Módulo para o cálculo do primeiro dígito
        soma = 0
        contagem = 10
        for numero in lista:
            if contagem == 1:
                break
            else:
                soma = soma + int(numero)*contagem
                contagem -= 1
        if (soma % 11) < 2:
            return 0
        else:
            return 11 - (soma % 11)
    
    def calculo_d2(self, lista, d1): #Módulo para o cálculo do segundo dígito
        soma = 0
        contagem = 11
        for numero in lista:
            if contagem == 2:
                soma = soma + 2*d1
                break
            else:
                soma = soma + int(numero)*contagem
                contagem -= 1
        if (soma % 11) < 2:
            return 0
        else:
            return 11 - (soma % 11)

    def verificar(self, lista, d1, d2): #Módulo para a verificação dos dois últimos dígitos
        digito_01_input = int(lista[9])
        digito_02_input = int(lista[10])

        if lista[12] != None:
            return "CPF é inválido"
        elif digito_01_input == d1 and digito_02_input == d2:
            return "CPF é válido."
        else: 
            return "CPF é inválido."
