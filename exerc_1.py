def obter_entrada_vendas():
    entrada = input()
    input_str = entrada.strip("[]")
    vendas = list(map(int, input_str.split(",")))
    return vendas

def analise_vendas(vendas):
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    return f"{total_vendas}, {media_vendas:.2f}"


vendas = obter_entrada_vendas()
print(analise_vendas(vendas))


# [120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190]