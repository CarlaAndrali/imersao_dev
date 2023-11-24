def converter_dolar_para_real(cotacao_dolar, valor_em_dolar):
    try:
        valor_em_real = cotacao_dolar * float(valor_em_dolar)
        return round(valor_em_real, 2)  # Arredonda para 2 casas decimais
    except ValueError:
        print("Por favor, digite um valor válido.")
        return None

cotacao_dolar = 4.8 #como puxar a cotação diária?

valor_em_dolar = input("Qual valor em Dólar que deseja converter para Real? ")

resultado = converter_dolar_para_real(cotacao_dolar, valor_em_dolar)

if resultado is not None:
    print(f"US$ {valor_em_dolar} equivale a R$ {resultado}")



