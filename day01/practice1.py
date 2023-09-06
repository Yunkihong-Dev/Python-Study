from random import *

users = list(range(1,21))

shuffle(users)
print(users)
print("치킨 당첨자 : "+str(sample(users,1)) + "커피 당첨자들",str(sample(users,3)))