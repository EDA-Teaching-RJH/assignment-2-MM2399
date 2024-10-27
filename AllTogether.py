### Part Four -- your code goes here. 
import random

def main():
    list = create_list(10)
    #using both a for and while loop to remove the even numbers.
    #originally used a for loop but saw a request of using a while loop in the question so just kept both.
    print (remove_even_numbers(list))
    print (remove_even_numbers_2(list))
 
#creates the list of random numbers 
def create_list(length):
    list = []
    for _ in range(length):
        list.append(random.randint(1,100))
    return list

#removes even numbers from the list using FOR loop
def remove_even_numbers(list):
    removed_even = []
    #used a for loop instead of while loop
    for _ in range(len(list)):
        if list[_] % 2 != 0:
            removed_even.append(list[_])
    return removed_even

#removes even numbers from the list using WHILE loop
def remove_even_numbers_2(list):
    removed_even = []
    count = 0
    #uses while loop as requested
    while True:
        if (count) == len(list):
            return removed_even
        else:
            if list[count] % 2 != 0:
                removed_even.append(list[count])
        count += 1
            
        
main()