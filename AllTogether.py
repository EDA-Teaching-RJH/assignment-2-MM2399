### Part Four -- your code goes here. 
import random

def main():
    print (remove_even_numbers(create_list(10)))
 
#creates the list of random numbers 
def create_list(length):
    list = []
    for _ in range(length):
        list.append(random.randint(1,100))
    return list

#removes even numbers from the list
def remove_even_numbers(list):
    removed_even = []
    #used a for loop instead of while loop
    for _ in range(len(list)):
        if list[_] % 2 != 0:
            removed_even.append(list[_])
    return removed_even

main()