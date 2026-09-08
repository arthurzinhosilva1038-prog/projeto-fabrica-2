produto = input("Digite o nome do produto: ")
mercado1 = input("Digite o nome do 1ª mercado: ")
preco1 = float(input(f"Digite o valor do 1ª{mercado1}: "))
mercado2 = input("Digite o nome do 2ª mercado: ")
preco2 = float(input(f"Digite o valor do 2ª{mercado2}: "))
mercado3 = input("Digite o nome do 3ª mercado: ")
preco3 = float(input(f"Digite o valor do 3ª{mercado3}: "))

if preco1 < preco2 and preco1 < preco3:
    print(f"O mercado {mercado1} tem o menor preço, que é de R$ {preco1}")
elif preco1 < preco1 and preco2 < preco3:
    print(f"O mercado {mercado2} tem o menor preço, que é de R$ {preco2}")
elif preco1 < preco1 and preco3 < preco2:
    print(f"O mercado {mercado3} tem o menor preço, que é de R$ {preco3}")