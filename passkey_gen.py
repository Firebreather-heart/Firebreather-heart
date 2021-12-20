import string
from random import sample

letter =[i for i in string.ascii_lowercase] +[i for i in string.ascii_uppercase]
num = [i for i in range(10)] +[i for i in range(10)]+[i for i in range(10)]
punct = [i for i in string.punctuation]+[string.whitespace]
def passkey_type(strength):
    ''' This sets the strength of the passkey'''
    if strength == 'low':
        return 0
    elif strength == 'medium':
        return 1
    elif strength == 'high':
        return 2
    elif strength == 'extreme':
        return 3
def num_only(length):
    """" This function is to give a passkey made of numbers only given a speciified passkey length it takes only one argument: passkey length"""
    try:
        length=int(length)
        if str(length).isalpha()  == True:
            raise ValueError
        elif length == 0:
            raise SyntaxError
        elif length==0:
            raise NotImplementedError
    except ValueError:
        return 'your input should be a number'
    except SyntaxError:
        return 'This command is invalid!,you cannnot have a key with no body?'
    except NotImplementedError:
        return 'you are yet to give the password length'
    
    else:
        if length > len(num):
            return 'key length is excessive\n'
            gen_key =sample(num,len(num))
        else:
            gen_key=sample(num,length)
    try:
        gen_key=str(gen_key)
        gen_key = gen_key.replace(',','')
        gen_key = gen_key.replace('[','')
        gen_key = gen_key.replace(']','')
    except Exception as e:
        print()
    else:
       return gen_key

def word_key(length):
    """ This function returns a password of a specified length. It takes only on argument: length"""
    try:
        length=int(length)
        if str(length).isalpha()  == True:
            raise ValueError
        elif length == 0:
            raise SyntaxError
        elif length==0:
            raise NotImplementedError
    except ValueError:
        return 'your input should be a number'
    except SyntaxError:
        return 'This command is invalid!,you cannnot have a key with no body?'
    except NotImplementedError:
        return 'you are yet to give the password length'
    
    else:
        if length > len(letter):
            return 'key length is excessive\n'
            gen_key =sample(letter,len(letter))
        else:
            gen_key=sample(letter,length)
    try:
        gen_key=str(gen_key)
        gen_key = gen_key.replace(',','')
        gen_key = gen_key.replace('[','')
        gen_key = gen_key.replace(']','')
        gen_key = gen_key.replace("'",'')
        
    except Exception as e:
        print()
    else:
       return gen_key
    

def alnum(length):
    """ This function returns a combined password of a specified length. It takes only on argument: length"""
    base = letter + num
    try:
        length=int(length)
        if str(length).isalpha()  == True:
            raise ValueError
        elif length == 0:
            raise SyntaxError
        elif length==0:
            raise NotImplementedError
    except ValueError:
        return 'your input should be a number'
    except SyntaxError:
        return 'This command is invalid!,you cannnot have a key with no body?'
    except NotImplementedError:
        return 'you are yet to give the password length'
    
    else:
        if length > len(base):
            return 'key length is excessive\n'
            gen_key =sample(base,len(base))
        else:
            gen_key=sample(base,length)
    try:
        gen_key=str(gen_key)
        gen_key = gen_key.replace(',','')
        gen_key = gen_key.replace('[','')
        gen_key = gen_key.replace(']','')
        gen_key = gen_key.replace("'",'')
        
    except Exception as e:
        print()
    else:
       return gen_key

def strongest(length):
    """ This function returns a combined password of a specified length. It takes only on argument: length"""
    base = letter + num + punct
    try:
        length=int(length)
        if str(length).isalpha()  == True:
            raise ValueError
        elif length == 0:
            raise SyntaxError
        elif length==0:
            raise NotImplementedError
    except ValueError:
        return 'your input should be a number'
    except SyntaxError:
        return 'This command is invalid!,you cannnot have a key with no body?'
    except NotImplementedError:
        return 'you are yet to give the password length'
    else:
        if length > len(base):
            return 'key length is excessive\n'
            gen_key =sample(base,len(base))
        else:
            gen_key=sample(base,length)
    try:
        gen_key=str(gen_key)
        gen_key = gen_key.replace(',','')
        gen_key = gen_key.replace('[','')
        gen_key = gen_key.replace(']','')
        gen_key = gen_key.replace("'",'')
        
    except Exception as e:
        print()
    else:
       return gen_key








