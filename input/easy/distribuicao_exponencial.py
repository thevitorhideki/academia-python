import math

valor_lambda = float(input("Qual a taxa (λ)? "))
valor_x = float(input("Qual x, para calcular F(λ, x)? "))

def distribuicao_exponencial(valor_lambda, valor_x):
    resultado = 1 - math.pow(math.e, -valor_lambda * valor_x)
    resultado_arredondado = str(round(resultado, 4))
    
    if len(resultado_arredondado) <= 5:
        for i in range(6 - len(resultado_arredondado)):
            resultado_arredondado = resultado_arredondado + '0'
    return resultado_arredondado

print(distribuicao_exponencial(valor_lambda, valor_x))
