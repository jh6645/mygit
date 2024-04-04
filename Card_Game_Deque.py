import time

from collections import deque
import random
class GameManager:
    def __init__(self,p_name=None,p_point=0):
        self.p_name=p_name
        self.GameSetting()
        self.p_point=p_point

    def GameSetting(self):
        print('Your name?',end=' ')
        self.p_name=input()

    def GameStart(self):
        print(self.p_name)
        G=Game(self.p_name)
        self.p_point+=G.GainPoint(G.a,G.b)
        print(f'Your total point : {self.p_point}')
        print('Next Game?(y/n)',end=' ')
        a=input()
        if a=='y':
            self.GameStart()
        elif a=='n':
            self.GameEnd()

    def GameEnd(self):
        print(f'Good Game,{self.p_name}')
        print(f'Your Total Point is {self.p_point}')

class Game:
    def __init__(self,p_name=None):
        self.p_name=p_name
        self.Explain()
        self.deck=deque()
        self.DeckSetting()
        self.a=self.AI_Play()
        self.b=self.Player_Play()
        self.GainPoint(self.a,self.b)



    def Explain(self):
        print('플레이어의 점수-AI의 점수=총 획득 포인트')

    def DeckSetting(self):
        pic_list=['Spade   ','Diamond ','Heart   ','Clover  ']
        num_list=['A']+[str(i) for i in range(2,11)]+['J','Q','K']
        deck_list=[]
        for i in pic_list:
            for j in num_list:
                deck_list.append(i+j)
        random.shuffle(deck_list)
        for i in deck_list:
            self.deck.append(i)
        print('Deck is Shuffled')

    def AI_Play(self):
        print('AI turn:')
        AI_point=0
        print('AI get a card')
        time.sleep(2)
        AI_pick=self.deck.pop()
        if AI_pick[8:]=='A':
            AI_point+=1
        elif AI_pick[8:]=='J':
            AI_point+=11
        elif AI_pick[8:]=='Q':
            AI_point+=12
        elif AI_pick[8:]=='K':
            AI_point+=13
        else:
            AI_point+=int(AI_pick[8:])
        print(f'AI got {AI_pick}',end=' ')
        print(AI_point)
        return AI_point


    def Player_Play(self):
        print(f'{self.p_name} turn:')
        Player_point = 0
        print(f'{self.p_name} get a card')
        print('Enter to get a card')
        input()
        Player_pick = self.deck.pop()
        if Player_pick[8:] == 'A':
            Player_point += 1
        elif Player_pick[8:] == 'J':
            Player_point += 11
        elif Player_pick[8:] == 'Q':
            Player_point += 12
        elif Player_pick[8:] == 'K':
            Player_point += 13
        else:
            Player_point += int(Player_pick[8:])
        print(f'{self.p_name} got {Player_pick}',end=' ')
        print(Player_point)
        return Player_point

    def GainPoint(self,a,b):
        return (b-a)

if __name__ == '__main__':
    GM=GameManager()
    GM.GameStart()