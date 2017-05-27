# declaration
# python doesn't care which value your variable has
pos_int = 3
neg_int = - 4
pos_float = 3.14
fake_int = '3'
string_ = 'hello world'
neg_float = pos_float * -1


# print() --> Output Console
print('------ printing Numbers ------')
print(pos_int)
print(neg_int)
print(pos_float)
print(fake_int)
print('------------\n\n')


# abs() --> print only positive Numbers
print('------ printing positive Numbers ------')
print(neg_float)
print(abs(-1*(2*4)))
print(abs(neg_float))
print(abs(neg_float + neg_float))
print('------------\n\n')


# print multiple Items
print('------ printing mixed Items (Numbers, String) ------')
print(pos_int, pos_float, fake_int, string_)
print(pos_int, '-', pos_float, '-', fake_int + '-' + string_)
print('------------\n\n')


# printing meaningful sentences
# in different ways
# the old way, was very C like

# old way
print('my positive Integer is %d' %(pos_int))

print('------ printing sentences with placeholder ------')
print('The sum of', pos_int, 'and', neg_int, 'is', pos_int + neg_int)
print('The sum of {} and {} is {}'.format(pos_int, neg_int, pos_int + neg_int))
print('The sum of ' + str(pos_int) + ' and ' + str(neg_int) + ' is '+ str(pos_int + neg_int))


# print string & a number is not working with plus
# print(a + d)
# use instead comma
print(pos_int, pos_float)
print('------------\n\n')


# print() --> Output Console
print('------ printing the type ------')
print(type(pos_int))
print(type(pos_float))
print(type(fake_int))
print(type(string_))
print('------------\n\n')


# calculation in print statement is possible
print('------ calculating in printing Statement ------')
print(pos_int + pos_float + pos_int * pos_float)
print(pos_int * pos_int)
print(pos_int * neg_int)
print(pos_int / pos_float)
print(pos_int / 2 * 20)
print('------------\n\n')

# Strings are powerful
print('------ lets talk about strings ------')
aString = 'nobody expects the spanish inquisition'
print(aString)
print(len(aString))

# Strings can be shorted by stop and start Position
# where xx: marking the beginning Position and :xx marking the end Position
print(aString[:-11])
print(aString[:11])
print(aString[-6:])
print(aString[6:])

# sometimes you only need a part of a Sting
# split() can be the Solution
# the result of a split is a list

sentence = 'is honduras the same as belize'
word = sentence.split(' ')
print(word)
print('------------\n\n')

#print(pos_int - fake_int) # Type Error

# Type Conversion
# str()     -->     for String
# int()     -->     for String
# str()     -->     for String
# float()   -->     for float

print('------ casting to diff. Formats ------')
print(pos_float - int(fake_int))
print()
print(type(pos_int))
print(type(str(pos_int)))
print(int(pos_float))
print(float(pos_int))




# formatting strings

print('{0:*^16}'.format('hi'))




# let's try some exercises
# ex_1_1 write an application that adding and printing the length of 2 Strings
# ex_1_2 write an application that counting the words of an sentence
# ex_1_3 reverse the order of Words in a sentence
# ex_1_4
# ex_1_5 counting the longest sequence of letters in alphabetical order

# functions

# lists



# dictionary


