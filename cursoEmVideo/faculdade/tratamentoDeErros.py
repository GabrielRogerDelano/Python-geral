while True:
    try:
        x = int(input('digite um número : '))
        break
    except ValueError:
        print('escreva um valor numérico inteiro')
print('fim do loop')

def dividir(x, y):
    try:
        resultado = x / y
        print('A resposta é = ', resultado)
    except ZeroDivisionError:
        print('Divisão por zero')
dividir(100, 0)

'''

A tabela a seguir traz alguns tipos comuns de exceção:

Exceção	Explicação
KeyboardInterrupt	Levantado quando o usuário pressiona CTRL+C, a combinação de interrupção.
OverflowError	    Levantado quando uma expressão de ponto flutuante é avaliada como um valor muito grande.
ZeroDivisionError	Levantado quando se tenta dividir por 0.
IOError	            Levantado quando uma operação de entrada/saída falha por um motivo relacionado a isso.
IndexError	        Levantado quando um índice sequencial está fora do intervalo de índices válidos.
NameError	        Levantado quando se tenta avaliar um identificador (nome) não atribuído.
TypeError	        Levantado quando uma operação da função é aplicada a um objeto do tipo errado.
ValueError	        Levantado quando a operação ou função tem um argumento com o tipo correto, mas valor incorreto.

'''
