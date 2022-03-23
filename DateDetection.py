#DateDetection.py
#Busca em um texto datas no formato DD/MM/AAAA, verifica se as datas são válidas (meses com 30, 31 ou 28dias e anos bissextos) printa uma lista com as datas válidas
import re

#Expressão regular para achar a data nos formatos DD/MM/AAAA DD/M/AAAA D/MM/AAAA D/M/AAAA
dataregex = re.compile(r'''(
    (\d?\d)             #dia com 1 ou 2 dígitos
    \/                  #separador /
    (\d?\d)             #mes com 1 ou 2 dígitos
    \/                  #separador /
    (\d\d\d\d)          #ano com 4 dígitos
    )''',re.VERBOSE)

datas = input('Insira o texto para retirada de datas:\n') #entra o texto
datasfinais = []

datasorg = dataregex.findall(datas) #salva todas as possiveis datas encontradas com o regex em datasorg
for i in range(len(datasorg)):#loop vai rodar a mesma quantidade de possiveis datas encontradas
    dia = int(datasorg[i][1])#definindo cada variavel para verificação
    mes = int(datasorg[i][2])
    ano = int(datasorg[i][3])
    resul = ""
    if dia >= 1 and dia <= 31:#dia deve estar entre 1 e 31
        if mes >= 1 and mes <= 12:#mes deve estar entre 1 e 12
            if ano >= 1000 and ano <= 2999:#ano deve estar entre 1000 e 2999
                if mes in (4,6,9,11) and dia <= 30:#se o mes for 4,6,9 ou 11, o dia deve ser no max 30
                    resul = 'verificado'
                elif (
                (mes == 2 and ano%400 == 0 and dia <= 29)#Se o ano for divisível por 400 # é bissexto
                or (mes == 2 and ano%100 == 0 and dia <= 28)#Se o ano for divisível por 100 # não é bissexto
                or (mes == 2 and ano%4 == 0 and ano%100 != 0 and dia <= 29)#Se o ano for divisível por 4 mas não por 100 # é bissexto
                or (mes == 2 and ano%4 != 0 and dia <= 28)):#Se o ano não for divisível por 4 não é bissexto
                    resul = 'verificado'
                elif mes in (1,3,5,7,8,10,12) and dia <= 31:#se o mes for 1,3,5,7,8,10ou12 o dia deve ser no max 31
                    resul = 'verificado'
                else:
                    resul = 'falhou verificação'

    if resul == 'verificado':#se passou em todas verificações
        datasfinais.append(datasorg[i][0])#adiciona data na lista datasfinais
        continue#volta para o inicio do loop e verifica próxima data
    else:
        print(f'Erro na data {datasorg[i][0]}, data inválida.')#printa erro com a data inválida

print(f'Datas Verificadas: {datasfinais}')
input('FIM DO PROGRAMA, APERTE ENTER PARA CONTINUAR')
