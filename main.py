def atv_1():
    try:
        tamanho = int(input('digite o tamanho do bloco: '))
    except Exception:
        print('Insira um valor valido')
        raise Exception('Valor invalido')

    if tamanho <= 20:
        for i in range(1,tamanho+1):
            print('*'*i)
    else:
        print('Insira um tamanho menor que 20')

def atv_2():
    try:
        tamanho = int(input('digite o tamanho do bloco: '))
    except Exception:
        print('Insira um valor valido')
        raise Exception('Valor invalido')

    if tamanho <= 20:
        for i in range(1,tamanho+1):
            print('*'*tamanho)
    else:
        print('Insira um tamanho menor que 20')

def atv_3():
    try:
        tamanho = int(input('digite o tamanho do bloco: '))
    except Exception:
        print('Insira um valor valido')
        raise Exception('Valor invalido')

    if tamanho <= 20:
        for i in range(1, tamanho+1,):
            print(' '*(i) + '*'*(tamanho-i))
    else:
        print('Insira um tamanho menor que 20')

def atv_4():
    expressao = input("Digite uma expressão matematica: \n")
    pilha = []
    
    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    aberturas = pares.values()
    fechamentos = pares.keys()
    
    for caractere in expressao:
        if caractere in aberturas:
            pilha.append(caractere)
        
        elif caractere in fechamentos:
            if not pilha:
                print("Caractere inválido, você não abriu nenhuma expressão com ele")
            
            topo = pilha.pop()
            
            if topo != pares[caractere]:
                print("Ordem de fechamento errada")
    
    if pilha:
        print("Existem delimitadores abertos")
    
    print("Expressão correta")

def atv_5():
    string = "soma = 10 + 20 ;"

    partes = string.split(" ")

    for p in partes:
        if p == "=":
            print(p + " -> Atribuição")
        elif p == "+":
            print(p + " -> Operador")
        elif p == ";":
            print(p + " -> Fim de instrução")
        elif p == "10" or p == "20":
            print(p + " -> Número")
        else:
            print(p + " -> Identificador")

def atv_6():
    lista1 = [1,2,3]
    lista2 = [2,3,4]
    
    uniao = set(lista1+lista2)
    intercecao = set(lista1).intersection(set(lista2))
    print("União:", uniao)
    print("Interseção:", intercecao)

def atv_7():
    senha = input("Digite a senha: ex(2-3-4) \n")
    estado = 0
    senha = senha.split("-")

    if senha[0] == '1':
        estado += 1
    if senha[1] == '2':
        estado += 1
    if senha[2] == '3':
        estado += 1
        
    if estado == 3:
        print("Senha correta")
    else:
        print("Senha incorreta")



atv_1()
atv_2()
atv_3()
atv_4()
atv_5()
atv_6()
atv_7()