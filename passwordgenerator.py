#code

list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list2= [ "~","!"  , "@" , "#",   "$",   "%" ,  "^"  , "&" ,  "*"  , "(" , ")"   ,"-"   ,"_"  , "="  , "+"   ,"{",  "}"  , "|" , "<" ,  ","   , ">"  , "/",".","?" ]





import random


a=random.choice(list1)
b=random.choice(list1)
c=random.choice(list1)
d=random.choice(list1)
e=random.choice(list2)
f=random.randrange(0,9)
g=random.randrange(0,9)
h=random.randrange(0,9)
f=str(f)
g=str(g)
h=str(h)
i=a+b+c+d+e+f+g+h


print("Your new genereated password is",i)

