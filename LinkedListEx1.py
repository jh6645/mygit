from clist import CList
import random
s=CList()
class Game:
    def __init__(self,num,TurnNum=0,dnum=0):
        self.PlayerNum = num
        self.TurnNum=TurnNum
        self.DiceNum=dnum
        self.DiceRoll_list=[[0 for _ in range(self.DiceNum)] for _ in range(self.PlayerNum)]

    def Start(self):
        print('\n\n\n\n\n\n\n\n\n')
        print('Start the game.')
        for i in range(self.PlayerNum):
            s.insert((self.PlayerNum - i))
        s.last=s.last.next
        print('Total Player : ' + str(self.PlayerNum))
        print('player'+str(s.last.item)+'\'s turn')
        print('press any key to change the turn')
        input()
        print(self.DiceRoll_list)


    def TurnChange(self):
        s.last=s.last.next
        self.TurnNum+=1
        print('player'+str(s.last.item)+'\'s turn')
        print('press any key to change the turn')
        input()

    def DiceRoll(self,pnum,rnum):
        self.DiceRoll_list[3 * rnum][pnum] = random.randint(1,6)
        self.DiceRoll_list[3 * rnum+1][pnum] = random.randint(1, 6)
        self.DiceRoll_list[3 * rnum+2][pnum] = random.randint(1, 6)
        print(self.DiceRoll_list[3 * rnum][pnum],self.DiceRoll_list[3 * rnum+1][pnum],self.DiceRoll_list[3 * rnum+2][pnum])
        print(self.DiceRoll_list)

g=Game(int(input('How many players?')))
g.Start()
g.TurnChange()
g.DiceRoll(0,0)