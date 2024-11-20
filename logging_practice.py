import logging

#logging.basicConfig(filename="test.log",level=logging.INFO,format="%(levelname)s:%(name)s:%(message)s")
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formater=logging.Formatter("%(levelname)s:%(name)s:%(message)s")
file_handler=logging.FileHandler("test1.log")
file_handler.setFormatter(formater)
stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formater)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        logger.debug('Created Employee:{}-{}'.format(self.fulname,self.email))
    @property
    def fulname(self):
        return '{}.{}'.format(self.fname,self.lname)
    @property
    def email(self):
        return '{}-{}@gmail.com'.format(self.fname,self.lname)
    
emp1=Employee("Mahsa","Rezaee")
emp2=Employee("Marjan","Emdadi")
emp3=Employee("Pooya","Asghari")
print("################")
import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formater=logging.Formatter("%(asctime)s :%(name)s- %(levelname)s - %(message)s")
file_handller=logging.FileHandler("test2.log")
file_handller.setFormatter(formater)
stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formater)
logger.addHandler(stream_handler)
logger.addHandler(file_handller)

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def division(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        logger.exception("Tried to divid by zero")
        logger.error(locals())
        #logger.error(globals())
    else:
        return result

x=10
y=0
add_result=add(x,y)
logger.info('Add:{}+{}={}'.format(x,y,add_result))
sub_result=sub(x,y)
logger.info('Sub:{}/{}={}'.format(x,y,sub_result))
mul_result=mul(x,y)
logger.info('Mul:{}*{}={}'.format(x,y,mul_result))
division_result=division(x,y)
logger.info('Div:{}/{}={}'.format(x,y,division_result))