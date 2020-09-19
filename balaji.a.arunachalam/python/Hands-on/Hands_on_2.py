#Given list of numbers, check if list contains three consecutive odd number:
#nums = [1,2,5,7,9,0,20]

def odd(lst):
    count=0
    for x in range(len(lst)):
        if lst[x]%2 != 0:
            count+=1
            if count ==3:
                return True
        else:
            count=0
    return False
# nums = [1,2,5,7,9,0,20]
# output=odd(nums)
# print(output)



#Print multiplication table of 5
def miltiple(num):
    for x in range(1,11):
        return (num*x)
#miltiple(5)

#print(list(5*x for x in range(1,11)))

#Thousand seperator:
#Input: 1234, Output: 1.234,Input: 1234567890, Output: 1.234.567.890

def seperator(num):
    if num/1000 < 1:
        return num
    else:
        a=str(num)
        b=[]
        count=0
        for x in range(len(a)):
            count+=1
            b.append(a[(len(a)-x-1)])
            if count==3 and x!=len(a)-1:
                b.append('.')
                count=0
    b=b[::-1]
    a=''.join(b)
    return a
#output=seperator(1234567890)
#print(output)

#create a class with class method,static method,decorator,global,local and non local variable in it

class Player(object):
    Board='BCCI'
    def __init__(self,fname,lname,age,country):
        global sport #Global variable,it can be accessed anywhere inside the class Player
        sport="Cricket"
        self.fname=fname
        self.lname=lname
        self.age=age
        self.country=country
    @property
    def full_name(self):
        return self.fname+" "+self.lname

    def Player_details(self,board):
        local_board=board #Local Variable,it can be accessed only inside this Player_details function
        return self.fname+" "+self.lname+" belongs to {0} and play {1} for all {2} tournaments".format(local_board,sport,Player.Board)

    @classmethod
    def name_change(cls,name):
        cls.Board=name

    @staticmethod
    def Game(name):
        if name.upper() =='CRICKET':
            return "Yeah,He belongs to {0} and play {1} sport".format(Player.Board,name)
        return "Nope,He play Cricket and belongs to {0} ".format(Player.Board)

    def player_skill(func_name):
        fielding='Average Fielder'
        def wrapper(skill):
            nonlocal fielding
            fielding="Good Fielder"#non local variable will change the value in main function
            print("He is a Good Player")
            return (func_name(skill,fielding))
        return wrapper

@Player.player_skill
def print_skill(skill,fielding):
    return "He is a {0} and {1}\n...............".format(skill,fielding)

Player.name_change("ICC") #Calling Class Method


# Player_1=Player('Virat','Kholi','31','India')
# Player_2=Player('Brett','Lee','40','Australia')
# Player_3=Player('Wasim','Akram','45','Pakistan')

# print(Player_1.Player_details('BCCI'))
# print(Player.Game("cricket")) #Calling Static Method
# print(print_skill("Batsman"))
#
# print(Player_2.Player_details('ACC'))
# print(Player.Game("Football")) #Calling Static Method
# print(print_skill("Fast Bowler"))
#
# print(Player_3.Player_details('PCB'))
# print(Player.Game("Cricket")) #Calling Static Method
# print(print_skill("Fast Bowler"))

class Sample(object):
    def add(self):
        pass
    def sub(self):
        pass