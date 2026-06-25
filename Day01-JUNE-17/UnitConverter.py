'''JUNE 17'''

'''C - K 
atm to Pa
kg - g 
foot inches
poise centipoise pascal'''


'''1'''
print("---------°C -> K converter-------")
# c = input("enter temp in degree celcius") 

# --------this is wrong as "c is taken as a string"----------------
c = float(input("enter temp in degree celcius")) 
print(c , "°C = ", end="")
K = c + 273.15
print(K, "K")

'''2'''
print("---------atm -> Pa converter-------")
atm = float(input("enter pressure in atm: ")) 
print(atm , "atm = ", end = "")
pascal = 101325*atm
print(pascal, "Pa")
