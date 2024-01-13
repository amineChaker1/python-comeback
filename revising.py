print(4 + 5)
rent = 525
expenses = 129
income = 925
surplus = income - (rent + expenses)
print(surplus)
print("the total expenses are " + str(rent + expenses))
# to dedcut a float to a certain decimal we use round
speedKmh = 65
distanceKm = 123
time = distanceKm / speedKmh
print(time)
# the variable time is very long in decimals
print(round(time , 3))
print(round(time , 2))
# also the python language is not good with storing floats so we fix it with round
nonBinaryFloat = 6- 5.7
print(nonBinaryFloat)
print(round(nonBinaryFloat , 2))

#strings are immutable in python and can be accessed like lists 
# when accessing keep in mind the first int is always counted where the last is -1
name = 'Amine Chaker'
print(name[:5])

phrase = '''this is a phrase
we can write it in multi line 
using three quotes
'''
print(phrase)
