import sys
class Constance:
    __slots__=()##ba in ravesh atrs ha ro faghat read only mikonim
    PI=3.14
    X=3
cons=Constance()
print(cons.PI)

print(sys.getsizeof(cons))
class Constance:
    __slots__=("width","hight")#maghadir atrs ro dar dakhele cotation bezar jahat taghit
    def __init__(self,width,hight):##ba in ravesh mishe maghadire atrs ro taghir dad
        self.width=width
        self.hight=hight

cons=Constance(120,"l")
print(cons.width)
cons.width=66
print(cons.width)


