# validacao_cpf_python


Algorítmo busca realizar a verificação da validade do CPF inserido.

Organização de dados baseada na POO.

O cadastro de pessoa física no Brasil é feito por meio de um código que é dividido em dois blocos:

XXX.XXX.XXX-YY

Os nove primeiros dígitos servirão para o cálculo do penúltimo e último caracteres.

CÁLCULO DO PRIMEIRO DÍGITO:

--> Os valores representados em 'X' são multiplicados um a um por uma progressão aritmétrica com o termo
inicial valendo 10, razão -1 e termo final valendo 2.

--> Após obtido os produtos, é feita a soma e, posteriormente, o módulo de 11. Caso o resultado final seja
menor que dois (2), o dígito um será considerado zero, caso contrário, será feita a subtração: (11 - r)
em que "r" representa o valor encontrado.

CÁLCULO DO SEGUNDO DÍGITO:

--> O processo é semelhante ao anterior, com a diferença de que o termo inicial da p.a. vale onze (11) e o último 
número a ser multiplicado será o dígito um.

--> Por fim, é feito o mesmo que a segunda etapa do primeiro cálculo.

*A explicação anterior é somente um esboço, para um melhor entedimento é necessária uma pesquisa mais
aprofundada.
*O código está sujeito a alterações para otimização.
