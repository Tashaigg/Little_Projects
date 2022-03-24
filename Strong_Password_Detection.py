#Strong_Password_Detection.py
#Este programa verifica se a senha digitada é segura, ou seja:
#Possui 8 ou mais caracteres. Há letras maiúsculas. Há letras minúsculas. Há números. Não há nenhuma palavra em português ou inglês.
import enchant, re

pt = enchant.Dict('pt_BR')
en = enchant.Dict("en_US")

longregex = re.compile('.{8,}')         #regex para verificar se senha contem 8 ou mais digitos
digregex = re.compile('\d')             #regex para verificar se senha contem numeros
lowerregex = re.compile('[a-z]')        #regex para verificar se senha contem letras minúsculas
upperregex = re.compile('[A-Z]')        #regex para verificar se senha contem letras maiúsculas
wordregex = re.compile('[a-z|A-Z]+')    #regex para salvar as combinaçoes de letras para na linha 23 verificar se há palavras em ingles ou portugues

print('Este programa verifica se a senha digitada é segura, ou seja:\nPossui 8 ou mais caracteres.\nHá letras maiúsculas.\nHá letras minúsculas.\nHá números.\nNão há nenhuma palavra em português ou inglês.')
while True:
    senha = input('Digite a senha para teste:\n')
    iswords = wordregex.findall(senha)
    islong = longregex.search(senha)
    isdig = digregex.search(senha)
    islowwer = lowerregex.search(senha)
    isupper = upperregex.search(senha)
    words = []

    for pal in range(len(iswords)):#para cada conjunto de letras encontradas
        if len(iswords[pal]) > 3:#se o conjunto for maior que 3, palavras com 3 ou menos caracteres são ignoradas
            for n in range(0,(len(iswords[pal])-3)):#index1
                for m in range((n+4),(len(iswords[pal])+1)):#index2
                    chunck = iswords[pal][n:m]#salva na variavel chunck a string [index1:index2]
                    #print(f'index {n} e {m}. chunck: {chunck}')##printa indexs e chunk
                    if pt.check(chunck) or en.check(chunck):#se chunck é uma palavra em en-US ou pt-BR
                        words.append(chunck)#adiciona chunck a lista de palavras encontradas
    if islong == None or isdig == None or islowwer == None or isupper == None or words != []:#se senha falhar em qualquer requisito
        print('Senha inválida')
        if islong == None:#se for curta
            print('A senha deve conter pelo menos 8 caracteres.')
        if isdig == None:#se não houver números
            print('A senha deve conter pelo menos 1 número.')
        if islowwer == None:#se não houver minúsculas
            print('A senha deve conter pelo menos 1 letra minúscula.')
        if isupper == None:#se não houver maiúsculas
            print('A senha deve conter pelo menos 1 letra maiúscula.')
        if words != []:#se houver palavras
            if len(words) == 1:
                print(f'A senha contem a palavra {words}, A senha não pode conter palavras do português ou inglês.')
            if len(words) > 1:
                print(f'A senha contem as palavras {words}, A senha não pode conter palavras do português ou inglês.')
    else:
        print(f'{senha} é uma senha válida')
        break

input('FIM DO PROGRAMA, APERTE ENTER PARA CONTINUAR')
