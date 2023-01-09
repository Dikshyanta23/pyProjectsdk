"""
author: Dikshyanta Uprety

The python script below contains the answers to the third question of the assignment.
The file has been divided into two parts, the first part is the head of the script which contains imports, supporting functions, global variables, etc.
The second part (body) contains the main script and asnwers to each question within the third question in the assignment

The head of the script is given below:

"""
# the imports
from random import randint
from time import time

# The supporting functions for the main script

# bubble sort, takes input an unsorted list and a number, will sort in ascending if 1 and descending if 0. Defaulted to 1.
def bubble_sort(the_list, num = 1):    
    length = len(the_list)
    # for all the elements in the list:
    for x in range(length):
        for y in range(0, length-x-1):      #For all elements, except the i elements already in place
            if (num == 1):                  # if num == 1, then the list will be sorted in ascending order
                if the_list[y] > the_list[y+1]:
                    the_list[y], the_list[y+1] = the_list[y+1], the_list[y]     #using x, y = y,x swap method in python

            else:           #num != 1
                if the_list[y] < the_list[y+1]:             # '>' on line 36 is replaced by '<' 
                    the_list[y], the_list[y+1] = the_list[y+1], the_list[y]
    return the_list 

# merge sort, takes input an unsorted list and a number, will sort in ascending if 1 and descending if 0. Defaulted to 1.
def merge_sort(the_list, num = 1):
    length = len(the_list)          
    if length > 1:                          # if length of the list is 1 or 0 , then no operation will be done on it
        mid = length//2                     # integer division 3//2 = 1
        first_sublist = the_list[:mid]      # slicing the array upto the middle element
        second_sublist = the_list[mid:]     # slicing rest of the array
        merge_sort(first_sublist, num)       # use merge sort on both sub-arrays
        merge_sort(second_sublist, num)
        i = j = k = 0                       # three variables to count indexes for 3 arrays, k for main array and i and j for sub-arrays
        if(num == 1):                       # then the list is sorted in ascending ordera
            while i < len(first_sublist) and j < len(second_sublist):
                if first_sublist[i] < second_sublist[j]:
                    the_list[k] = first_sublist[i]      #smaller number is put in the list first
                    i += 1
                else:
                    the_list[k] = second_sublist[j]
                    j += 1
                k += 1

            while i < len(first_sublist):                # any number remaining on the first sublist is added to the main list
                the_list[k] = first_sublist[i]
                i += 1
                k += 1
    
            while j < len(second_sublist):              # similarly any number remaining on the second sublist is added to the main list
                the_list[k] = second_sublist[j]
                j += 1
                k += 1
        else:                                           # this is when num != 1, that means the list is sorted in a descending order
            while i < len(first_sublist) and j < len(second_sublist):
                if first_sublist[i] > second_sublist[j]:    # the greater number is added first
                    the_list[k] = first_sublist[i]
                    i += 1
                else:
                    the_list[k] = second_sublist[j]
                    j += 1
                k += 1

            while i < len(first_sublist):               # numbers remaining on the first sublist added
                the_list[k] = first_sublist[i]
                i += 1
                k += 1
    
            while j < len(second_sublist):              # number remaining on the second sublist added
                the_list[k] = second_sublist[j]
                j += 1
                k += 1
    return the_list                                     # the sorted list (ascending or descending is returned)


#is odd function, determines if a number is odd
def is_odd(x):
    if x%2 != 0:    #if x is not divisible by 2
        return 1
    return 0

# generate random list function
def generate_random_list(number):
    # generate a nested list of dimension num*num with random values inside ranging from 1 to num
    new_list = [[randint(1,number) for y in range(number)] for x in range(number)]
    return new_list

# function to calculate the average for part III and IV 
def calcAverage(list):
    sum = 0                     # Initialization of sum
    for number in list:         # all members of the list
        sum = sum+ number       #add the numbers to sum
    average = sum/len(list)     # average = total_sum/ number_of_elements
    return average



"""
This marks the end of the head section of the program, the next part body will contain the main program. It will use the functions defined
in  the head section and asnwer the questions within the third question of the assignment.
"""


#Question 3(A)

"""
The question asks us to generate a nested list of size 100 * 100 and sort it so the sublists with:
1) odd indexes are sorted in ascending order
2) even indexes are sorted into descending order

Therefore, we need an algorithm to generate a list of 100* 100 dimensions with random numbers inside, and sort the list to meet the given conditions.

pseudo code

 algorithm: sort the odd indexed arrays inside a 2d array into ascending order and even indexed arrays into descending order:

declare array =[100][100] containing randint(1, 100) as all elements
for i in range(length of array)):
    if i is odd:
        array[i] = bubble_sort_ascending(array[i])
    else:
        array[i] = bubble_sort_descending(array[i])
    # the list is sorted

def bubble_sort_ascending(list):    
    for x in range(length of the list):
        for y in range(0, length-x-1):      
                if list[y] is greater than list[y+1]:
                    swap list[y] and list[y+1]

def bubble_sort_descending(list):    
    for x in range(length of the list):
        for y in range(0, length-x-1):      
                if list[y] is less than list[y+1]:
                    swap list[y] and list[y+1]
                    
                    
# In the real code, 1 function with two parameters instead of these two separate functions will be used for sorting the list
"""

# a function to sort a list, will use the provided sort function(ascending order on odd indexes and descending order on even indexes)
def custom_sort(new_list, sort_function):         # dimension refers to the size of array and sort function is the function to be used
    for i in range(len(new_list)):                  # for all the lists within new_list
        new_list[i] = sort_function(new_list[i], is_odd(i)) # sort using the given sort function

# start the solution to question 3A
print("Question 3(A):\n")
# generate a random list of dimension 100 * 100
the_list = generate_random_list(100)
# print two lists inside the list to confirm the randomness
print("A 2d list of size 100 * 100 has been generated. The list's size is too big to be neatly outputted into the console.")
print("Therefore, two lists within the list, with index [2] and [3] will be printed before the sorting function is applied to it and after, to see the result of the sorts.\n")
print("The list with the index [2] before the sort:")
print(the_list[2])
print("\n The list with the index [3] before the sort:")
print(the_list[3])
# invoke the custom_sort function with the list as parameter to sort the list, use bubble sort
custom_sort(the_list, bubble_sort)
print("\nThe sorting algorithm has been applied to the list. The lists with index [2] and [3] are expected to be sorted in descending and ascending order respectively.")
# print the lists with index 2 and 3 again
print("\nThe list with index[2] after the sort:")
print(the_list[2])
print("\nThe list with index[3] after the sort:")
print(the_list[3])
print('\n')


#Question 3(B)

"""
The question is divided into four parts. However, all four parts contain sorting 10 instances of random lists and measuring their time.
The difference between the parts is the size of random list and the sort function to be used.

Therefore, for this body of question we will need an algorithm to sort lists of a given size using a given sort function.

pseudo code

algorithm: calculate the time for 10 instances of given sorting algorithm along with their average and output the results

# define a function to measure 10 instance timings and average timings of the chosen sort

def calculate_time_for_sorts(dimension of the random array, the sort function to be used):
    timings_array = []      # to store timing of individual instances
    for i in range(10):
        generate a random list using generate_random_list function in the head      # line 89 -93
        start = time()      # the timing start
            sort the list using the custom_sort function in part(A)         # line 147 - 150
        time_taken = time() - start         # measure the time taken
        append time_taken to timings_array
        output the time_taken    # this is the instance timing
    calculate the average timing using calcAverage function(pass timings_array)         # line 95 - 101
    print the average time

# in the real code, the results will be concatenated into a meaningful string before being outputted
"""

# function that will calculate the sort timing for 10 instances of random array. Will be used for part I, II and IV
# Takes the dimension of the array and sort function to be used and prints the time taken for 10 instances along with their average time
def calcualte_time_for_sorts(number, sort_function):
    times = []                      # a list is intialized, will store the times for the instances
    for i in range(10):             # 10 instances are tested
        random_list = generate_random_list(number)              # using predefined function to generate random list of dimension(number* number)
        start = time()                                      # time started before sorting
        custom_sort(random_list, sort_function)             # using custom sort defined in 3(A) to sort the generated random list
        time_taken = time() - start                                         # time is stopped and start is deducted to calculate operating time
        times.append(time_taken)                                            # added to array for average calculation 
        print("Instance "+str(i)+", time taken: "+str(round(time_taken, 3))+" seconds.") # instance result printed
    average = round(calcAverage(times), 3)          # calcAverage function is used to calculate average
    print("\nThe average time for the above instances is "+ str(average)+" seconds.\n") #average printed with the results


# start the solution
print("Question 3(B):\n")
print("This question is divided into four parts. Parts I, II, III, IV are answered below in the given order.\n")
# Part I
print("Part I")
print("For 10 instances, bubble sort (complexity:n^2) is used to sort the array(size 100 * 100). The time for these instances along with their average time:\n")
# invoke the calculate_time_for_sorts() function to output times for 10 instances of bubble sorts on a list of size 100 * 100 and their average 
calcualte_time_for_sorts(100, bubble_sort) 

# Part II
print("Part II")
print("For 10 instances, merge sort (complexity:n*log(n)) is used to sort the array(size 100 * 100). The time for these instances along with their average time:\n")
# invoke the calculate_time_for_sorts() function to output times for 10 instances of merge sorts on a list of size 100 * 100 and their average
calcualte_time_for_sorts(100, merge_sort)

# Part III - done in Q3.docx
print("\nPart III is done in a file called q3.docx, located in the same directory as this file.\n")

# Part IV
print("Part IV")
print("For 10 instances, bubble sort (complexity:n^2) is used to sort the array(size 500 * 500). The time for these instances along with their average time:\n")
# invoke the calculate_time_for_sorts() function to output times for 10 instances of bubble sorts on a list of size 500 * 500 and their average 
calcualte_time_for_sorts(500, bubble_sort)

# similarly, using merge sort
print("For 10 instances, merge sort (complexity:n*log(n)) is used to sort the array(size 500 * 500). The time for these instances along with their average time:\n")
# invoke the calculate_time_for_sorts() function to output times for 10 instances of merge sorts on a list of size 500 * 500 and their average
calcualte_time_for_sorts(500, merge_sort)

# the comparisions of the output time is done in the text file
print("\nThe second part of 'Part IV' is done in 'q3.docx'")


