import random
a = int(input(" valeur min "))
b = int(input(" valeur max "))
c = (random.randint(a,b))
while continuer:
    d = int(input(" tentez votre chance "))
    if d == c :
        print("Bien jouer")
        
    elif d< c :
        print(" c'est plus ") 
    elif d>c: 
        print("c'est moins ") 
 