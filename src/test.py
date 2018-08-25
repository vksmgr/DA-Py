import bisect

c = [1,2,2,4,9]

pos = bisect.bisect(c, 10)
print("position : {}".format(pos))
bisect.insort(c,10)
print(c)
for (i, value) in enumerate(c):
    print(" I : {0} , value : {1}".format(i,value))

itme = 'i love you'

print(sorted(itme))
print(list(zip(c,itme)))

for (i, v) in enumerate(zip(c,itme)):
    print("i : {0}, value: {1}".format(i,v))

# the cleaver way to unzip is

first_value, last_value = zip(*zip(c,itme))

print(first_value)
print(last_value)

# dictionary (hashmaps)

dics = {1: 'one', 2: 'two', 3: 'three'}
print(dics[1])
dics[4] = 'four'
print(dics[4])

#dict function will accept a list of 2- tuples
ld = dict(zip(c,itme))
print(ld)

#arranging words by there first letter

words = ['apple', 'bar', 'boom']

by_first_letter = {}

for word in words:
    letter = word[0]
    if letter not in by_first_letter:
        by_first_letter[letter] = [word]
    else:
        by_first_letter[letter].append(word)
print(by_first_letter)

#you can do same thing in set default
by_first_letter_new = {}
for word in words:
    letter = word[0]
    by_first_letter_new.setdefault(letter, []).append(word)
print(by_first_letter_new)

#you can also use default dict

from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
print(by_letter)

#python comprehension feature

strings = [ 'a' , 'as' , 'bat' , 'car' , 'dove' , 'python' ]
val = [x.upper() for x in strings if len(x) > 2]
print(val)

#dict comprehensions

dict_comp = { index: val for index, val in enumerate(dics)}
print(dict_comp)

#dict comprehensions with strings

local_mapping = {idx: val.upper() for idx, val in enumerate(strings)}
print(local_mapping)

#nested comprehension
all_data = [[ 'John' , 'Emily' , 'Michael' , 'Mary' , 'Steven' ],
            [ 'Maria' , 'Juan' , 'Javier' , 'Natalia' , 'Pilar' ]]

#get a single list containing all names with two or more e’s in them

result = [name for names in all_data for name in names if name.count('e') > 1]
print(result)

#“flatten” a list of tuples of integers into a simple list of integers
some_tuples = [( 1 , 2 , 3 ), ( 4 , 5 , 6 ), ( 7 , 8 , 9 )]
simple_list = [x for tuple in some_tuples for x in tuple]
print(simple_list)

#produce list of list insted of just list
list_list = [[x for x in tuple]for tuple in some_tuples]
print(list_list)