from difficulty_settings import difficulty_settings
from time import time

while True:
    difficulty = input('Selecione uma dificuldade [1, 2, 3]: ')
    if(difficulty not in ('1', '2', '3')):
        print('O valor fornecido não é válido. Tente novamente.')
    else:
        break

difficulty = difficulty_settings.get(difficulty)
score: int = 0
time_start = time()
time_delta = 0


# Game Loop

userInput = ''

while userInput != 'n':
    question = difficulty.get_question()
    
    while(True):
        try:
            response = float(input('\n' + question[0]))
            break;
        except:
            print('Valor inválido. Tente novamente!')    
    
    if(response == question[1]):
        score += 1
        print('Correto!\n')
    else:
        print('Errado!\n')

    userInput = input('Continuar? ([s] / n): ' )

time_delta = time() - time_start

print(
f'''
Obrigado por jogar!
Sua pontuação final foi: {score};
Seu tempo de jogo foi: {round(time_delta, 3)} segundos;
Resultando em {round(score / time_delta, 3)} pontos por segundo.
'''
)


