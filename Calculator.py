def menu():
    print("1- SOMA")
    print("2- SUB")
    print("3- MULTI")
    print("4- DIV")

    a = int(input('digite um valor: '))
    b = int(input('digite outro valor: '))
    op = int(input('OPERAÇÃO'))
    if op <= 0 or op > 4:
        print('opção invalida')
        exit(0)
    if op == 1:
        print(soma(a,b))
    if op == 2:
        print(sub(a,b))
    if op == 3:
        print(multi(a,b))
    if op == 4:
        print(div(a,b))
def soma(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
menu()
