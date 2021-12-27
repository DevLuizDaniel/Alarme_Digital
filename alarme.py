"""
Software desenvolvido exclusivamente para ambiente Windows
"""

#Importando algumas bibliotecas e suas funções

from time import sleep
from os import system
from winsound import Beep

system("cls")
print('\n\t\t\t\tAlarme programável\n\n')

#Aqui será definido a hora, minuto e os segundos exatos  (hour, minute, seconds)

hora = int(input('Defina a hora: '))
minuto = int(input('Defina os minutos: '))
segundo = int(input('Defina os segundos: '))
frequencia = int(input('Defina a frequência que vai ser utilizada: '))

#Um laço de repetição será criado para visualizar o tempo

for h in range(00, 24):
    for m in range(00, 60):
        for s in range(00, 60):
            print(f'\n\tHorário:\t\tAlarme:\n\n\t{h}:{m}:{s}\t\tAlarme definido para às {hora}:{minuto}:{segundo}')
            sleep(1)
            system("cls")
            #Quando chegar ou passar do tempo definido pelo usuário nas opções acima, será ativado o beep com o som da frequência descrita
            if h >= hora and m >= minuto and s >= segundo:
                duracao = 980
                Beep(frequencia, duracao)
                system("cls")
            else:
                #Se ainda não for a hora, passe
                pass

#DevLuizDaniel ;)