palavra = ['abacaxi', 'laranja', 'pera', 'brasil', 'argentina', 'inglaterra', 'amarelo', 'verde', 'azul']


def dica_palavra(palavra):

    if ((palavra == 'abacaxi') or (palavra == 'laranja') or (palavra == 'pera')):
        print(f"\n\nDica da palavra é: \033[1;33mFRUTAS\033[m")
    
    elif ((palavra == 'brasil') or (palavra == 'argentina') or (palavra == 'inglaterra')):
        print(f"\n\nDica da palavra é: \033[1;33mPAISES\033[m")
    

    elif ((palavra == 'amarelo') or (palavra == 'verde') or (palavra == 'azul')):
        print(f"\n\nDica da palavra é: \033[1;33mCORES\033[m")


def linha(tam = 60):
    return '-' * 60