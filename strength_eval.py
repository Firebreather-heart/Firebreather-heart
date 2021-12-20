import string
sto = []
bb = string.ascii_uppercase[:]
pp =string.punctuation[:]
class checkMech:
    def __init__(self,key):
       self.key = key 
    def evalKey(self):
        '''Checks if key is string only or alphanumeric or numeric only or combined '''
        if self == '':
            return 0
        if self.isalpha() == True:
            return 5
        if self in bb :
            for i in self:
                return 8
        elif self.isdigit() == True:
            return 1
        elif self.isalnum() == True:
            return 10

        else:
            for i in self:
                if i in pp:
                
                    #sto.append(i)
                    return 15
    def multiplier(self):
        if len(self)==0:
            return 0 
        elif len((self)) >0 and len(self)<=6:
            return 2 
        elif len(self) >6 and len(self) <=12:
            return 4 
        else:
            return 6
    def mulspecial(self):
        for i in self:
                if i in pp:
            
                    sto.append(i)
        if len(sto)>0 and len(sto)<=5:
            return 3
        elif len(sto)>5 and len(sto)<=12:
            return 7 
        elif len(sto) > 12:
            return 9
        else:
            return 0
        
def evaluator(key):
    '''this will evaluate the strength of a given passkey'''
    one = checkMech.evalKey(key)
    two = checkMech.multiplier((key))
    three = checkMech.mulspecial(key)
    pow = one+two+three 
    return pow


