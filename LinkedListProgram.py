from clist import CList
import random
class GameManager:
    def __init__(self,Dnum=3,Rnum=1,Pnum=2):
        self.Dnum=Dnum
        self.Rnum=Rnum
        self.Pnum=Pnum

    def GameSet(self):
        print('='*60,end='\n\n')
        print(' '*25+'Dice Game!'+' '*25,end='\n\n')
        print(' '*12+'insert Dice Number and Round Number!'+' '*12)
        self.Dnum=int(input(' '*26+'D num : '))
        self.Rnum=int(input(' '*26+'R num : '))
        self.Pnum=int(input(' '*22+'How many Players?'))

class Game:
    def __init__(self,Dnum=3,Rnum=1,Pnum=2):
        self.Dnum=Dnum
        self.Rnum=Rnum
        self.Pnum=Pnum
        self.PointC=CList()
        self.DiceLog=[[0 for _ in range(Rnum)] for _ in range(Pnum)]
        self.Point=[0 for _ in range(Pnum)]

    def DiceRoll(self,r,p):
        sum=0
        for i in range(self.Dnum):
            x=random.randint(1,6)
            print(str(x),end=' ')
            sum+=x
        print('')
        print('sum=',sum)
        self.DiceLog[r][p]=sum
        return sum

    def PrintLog(self):
        print(self.DiceLog)
        print(self.Point)
        self.PointC.last = self.PointC.last.next
        self.PointC.print_list()

    def GameStart(self):
        for _ in range(self.Pnum):
            self.PointC.insert(0)
        print('='*25+'Game Start'+'='*25)
        for i in range(self.Rnum):
            for j in range(self.Pnum):
                self.Turn(j,i)

    def Turn(self,p,r):
        print(f'Player {p+1} Turn, Round {r+1}')
        a=self.DiceRoll(p,r)
        self.Point[p]+=a
        self.PointC.last.item+=a
        self.PointC.last=self.PointC.last.next
        input()




GM=GameManager()
GM.GameSet()
g=Game(GM.Dnum,GM.Rnum,GM.Pnum)
g.GameStart()
g.PrintLog()