def valor_minimo_p2(q2, p1, n2):
    # Função para calcular o valor mínimo de p2 para que a média final seja 7
    def media_final(p2):
        n1 = (q2 * 0.3) + ((p1 + p2) / 2) * 0.7
        return (n1 + n2) / 2

    # Inicializando p2 como 0 e incrementando até encontrar o valor mínimo
    p2 = 0
    while media_final(p2) < 7:
        p2 += 0.01  # Incremento pequeno para precisão

    return round(p2, 2)

q2 = float(input())
p1 = float(input())
n2 = float(input())

# Chamando a função e imprimindo o resultado
valor_minimo = valor_minimo_p2(q2=q2, p1=p1, n2=n2) # passa os parametros aqui e é bala
print(f"O valor mínimo de p2 para que a média final seja 7 é: {valor_minimo}")