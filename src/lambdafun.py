#lambda function

ints = [1, 2, 3, 4, 5]

def app_toplist(ints, f):
    return [f(x) for x in ints]

print(app_toplist(ints, lambda x: x * 2))

strings = [ 'foo' , 'card' , 'bar' , 'aaaa' , 'abab' ]

#sort string by number of distinct letters
dis = strings.sort(key =  lambda x: len(set(list(x))))
print(strings)


#iterrating over dics will yiels dict key
dic = {1: 'one', 2: 'two', 3: 'three'}

for key in dic:
    print(dic[key])

#generator
def square( n= 10):
    print('generate square form 1 to {0}'.format(n ** 2))
    for i in range(1, n+1):
        yield i ** 2
gen = square()
print(gen)
for x in gen:
    print(x, end=' ')
#generator comprehension same as list dict
gn = (i ** 2 for i in range(5))
for x in gn:
    print(x, end= ' ')

# intertool
## groupby

import itertools
first_letter  = lambda x: x[0]

names = [ 'Alan' , 'Adam' , 'Wes' , 'Will' , 'Albert' , 'Steven' ]
for letter, name in itertools.groupby(names, first_letter):
    print("{0} : {1} ".format(letter, list(name)))

#### Error Handling in python
def attempt_flat(x):
    try:
        return float(x)
    except:
        return x
print("Convert to float {0}".format(attempt_flat('10.10.10')))