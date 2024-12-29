#printar
print("Quero meu primeiro emprego!")

#bolean
is_python = True
is_java = False

#armazenando condições
ingressos = 50
compradores = 250
tem_ingresso_suficiente = (ingressos >= compradores)
print(tem_ingresso_suficiente)

#Tipos
nome = "Vitor" #string
idade = 20 #int
peso = 90.2 #float

print(nome)
print(idade)
print(peso)

#input
nome = input("Digite seu nome: ") #input sempre retorna uma string, se quisermos outro tipo, precisamos converter
idade = int(input("Digite sua idade ")) #convertido para int
peso = float(input("Digite seu peso: ")) #convertido para float

print(nome)
print(idade)
print(type(idade))
print(peso)
print(type(peso))

#operadores aritméticos
soma = 1 + 1
multiplicacao = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2

print("soma", soma)
print("multiplicacao", multiplicacao)
print("divisao", divisao)
print("potencia", potencia)


#operadores lógicos
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Entrada permitida!")
else:
    print("Entrada bloqueada!")

salario = float(input("Digite seu salário: "))

if salario <= 3000:
    print("Programador júnior!")
elif salario > 3000 and salario <= 6000: #and = e, podemos usar o or(ou) também
    print("Programador pleno!")
elif salario > 6000 and salario <= 15000:
    print("Programador sênior!")
else:
    print("Gerente de projetos!")

#listas
lista = [1, 2, 3]
print(lista[0])
print(lista[1])
print(lista[2])

#funções nativas do python
lista.append(4) #adicina um elemento no fim da lista
print(lista)
lista.insert(1, 0) #adiciona um elemento para a posição dada
print(lista)
lista.pop() #remove o último elemento da lista, podemos passar o index de qual desejamos remover
print(lista)
lista.sort() #ordena em ordem crescente
print(lista)
lista.reverse() #ordena em ordem decrescente
print(lista) 
print(lista.index(0)) #retorna o index do itme que foi passado
print(lista.count(1)) #retorna o número de ocorrências do item
lista.remove(3) #remove a primeira ocorrência do item
print(lista) 

print(len(lista)) #retorna o tamanho
print(max(lista)) #retorna o maior item
print(min(lista)) #retorna o menor item

#loops
for x in range(5):
    print(x)

notas = []

for x in range(3):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("Quantidade de notas: ", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM ", codigo_aluno, "tirou a nota: ", nota)

#dicionário
player = {
    "nome" : "Guilherme",
    "level" : 2,
    "hp": 30,
    "exp": 450,
    "dano": 15
}

#lista de dicionários
npcs = [
    {"nome" : "Monstrinho", "level" : 1, "hp": 10, "exp": 45, "dano": 5,},
    {"nome" : "Monstro", "level" : 2, "hp": 20, "exp": 300, "dano": 10,},
    {"nome" : "Monstrão", "level" : 3, "hp": 35, "exp": 450, "dano": 15,},
    {"nome" : "Chefão", "level" : 4, "hp": 50, "exp": 500, "dano": 25,}
]

#funções
def minha_funcao(valor1, valor2):
    return valor1 + valor2


while True:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    resposta = minha_funcao(valor1, valor2)
    print("Resposta: ", resposta)
