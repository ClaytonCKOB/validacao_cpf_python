from validar_cpf import Cpf

cpf_user = input("Insira seu cpf: ")


c1 = Cpf(cpf_user)
c1.filtro_de_valores(cpf_user)

lista_numerica = c1.separar(cpf_user)
digito_01 = c1.calculo_d1(lista_numerica)
digito_02 = c1.calculo_d2(lista_numerica, digito_01)

print(c1.verificar(lista_numerica, digito_01, digito_02))
