import string
import random;



def GetWord():
    where = random.randrange(0,1000)
    with open('Words.txt','r',encoding='utf-8') as words:
        num = 0
        for word in words:
            if (num == where):
                return word;
            else:
                num+=1;
                #Adding New Thing




def PlayGame():
    print('#'*10,'HANGMAN','#'*10);
    rounds = 0;
    TheWord = list(GetWord())
    guesses = [];
    Hangman = list('#####');
    while True:
        art = (HangManFigures(len(guesses)))
        rounds+=1;
        if (Hangman[0:4] == TheWord[0:4]):
            print('WINNER')
            break
        if (art !='END'):
            print(art);
        else:
            print('LOSER')
            break
        print('#'*5,'Round %s'%rounds,'#'*5)
        print(Hangman);
        print('*'*20)
        print('WRONG GUESSES :  %s'%guesses);
        print('*'*30)
        ask = input('Pick a Letter : ').capitalize();
        if ask in TheWord:
            for i in range(5):
                if TheWord[i] == ask:
                    Hangman[i] = ask;
        else:
            try:
                guesses.append(ask);
            except:
                None;

        ##print('LETTERS LEFT : \n %s'%letters);
        print('~~~~~~~~~~~~~~~~~~~~')
    

def HangManFigures(t):
    if t==0:
        return '';
    if t==1:
       return  '''
        |
        |
        '''
    elif t==2:
        return  '''
        |
        |
        |
        |
        '''
    elif t==3:
        return '''
        |
        |
        |
        |____
        '''
    elif t==4:
        return '''
        ____
        |
        |
        |
        |____
        '''
    elif t==4:
        return '''
        ____
        |  |
        |
        |
        |____
        '''
    elif t==5:
        return '''
        ____
        |  |
        |  0
        |
        |____
        '''
    elif t==6:
        return '''
        ____
        |  |
        |  0
        |  T
        |____
        '''
    elif t==7:
        return '''
        ____
        |  |
        |  0
        | -T-
        | ! !
        |____
        '''
    elif t==8:
        return 'END';

PlayGame();