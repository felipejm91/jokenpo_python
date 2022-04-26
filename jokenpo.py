#Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')

op = 0

while(op != 5):
    print
    print("\n\nEscolha sua jogada")
    print("{}0 - PEDRA{}" .format("\033[1;36m", "\033[m"))
    print("{}1 - PAPEL{}" .format("\033[1;35m", "\033[m"))
    print("{}2 - TESOURA{}" .format("\033[1;34m", "\033[m"))
    print("{}5 - SAIR DO PROGRAMA{}" .format("\033[1;31m", "\033[m"))
    op = int(input("OPÇÃO: "))

    if (op == 5):
        print ("\nAté a próxima!")
        break
    else:
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ')
        sleep(1)

        jogadapc = randint(0, 2)

        print('-=' * 10)
        print("COMPUTADOR = {}" .format(itens[jogadapc]))
        print("JOGADOR = {}" .format(itens[op]))
        print('-=' * 10)

        if(jogadapc == 0):
            if(op == 0):
                print("{}EMPATE{}" .format("\033[1;33m", "\033[m"))        
            elif(op == 1):               
                print("{}JOGADOR VENCEU{}" .format("\033[1;32m", "\033[m"))
            elif(op == 2):        
                print("{}JOGADOR PERDEU{}" .format("\033[1;31m", "\033[m"))
        elif(jogadapc == 1):
            if(op == 0):            
                print("{}JOGADOR PERDEU{}" .format("\033[1;31m", "\033[m"))
            elif(op == 1):
                print("{}EMPATE{}" .format("\033[1;33m", "\033[m"))
            elif(op ==2):
                print("{}JOGADOR VENCEU{}" .format("\033[1;32m", "\033[m"))
        elif(jogadapc == 2):                
            if(op == 0):
                print("{}JOGADOR VENCEU{}" .format("\033[1;32m", "\033[m"))                   
            elif(op == 1):
                print("{}JOGADOR PERDEU{}" .format("\033[1;31m", "\033[m"))
            elif(op ==2):
                print("{}EMPATE{}" .format("\033[1;33m", "\033[m"))
                        