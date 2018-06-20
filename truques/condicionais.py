a, b, c, d = 1, 2, 3, 4

if a == 1 and b == 2 and c == 3 and d == 4:
    print('all True!')

condicoes = [
    a==1, 
    b==2, 
    c==3, 
    d==4
]

if all(condicoes):
    print('todas as condições eram verdadeiras!')

if any(condicoes):
    print('ao menos uma condição era verdadeira!')