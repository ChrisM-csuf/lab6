"""
to start, we generate a random number between 1 and 20
based on that number we check if it falls into a certain range
if number > 15 we say charries
>5 plum
> 2 melon
> 1 bell
outside of those its bar

we iterate ove it using a loop 3 times
"""

"""
import random

num - generate random number

if num > 15
    result: charries
if num >10 
    result: orange
if number > 5
    result: plum
if number > 2
    result: melon
if num = 1
    result: bell
else
    result: bar

loop three times
    print to user
"""
import random

def main():
    for i in range(0,3):
        spin()
def spin(): 
    rand_num = random.randint(1,20)
    output = ""
    if rand_num > 15:
        output = "Cherries"
    elif rand_num > 10:
        output = "Orange"
    elif rand_num > 5:
        output = "Plum"
    elif rand_num > 2:
        output = "Bell"
    elif rand_num > 1:
        output = "Melon"
    else: 
        output = "Bar"

    print(output, end=" ")

main()