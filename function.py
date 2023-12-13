'''
def myself_anu():
    print("I am anusha")
    print("welcome")

print("Yo")
print("There is a function, invoke it")
myself_anu()
-----------
'''
'''
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print("Hello")

greet('en')
greet('es')
-----------
'''
'''
def greet():
    return "Hello"

print(greet(), "Anu")
print("Welcome")
-----------
'''

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
    
print(greet('en'),'Anu')
print(greet('es'),'Etikala')