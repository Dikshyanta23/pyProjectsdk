"""
author: Dikshyanta Uprety

The python script below contains the answers to the second question of the assignment.
The file has been divided into three parts, the first part (head) contains imports, supporting functions, global variables, etc.

The second part (analysis) processes the data from the given csv file to compute some values. These values will be used to analyze the csv file and 
define some key parameters to be used in the simulation.

The third part (simulation) uses the parameters derived in analysis and creates a simulation as described in the question.

The head of the script is given below:

"""
#the imports
import csv
from random import randint

# global variables

# the amount of items 4 cooks and 6 cooks can cook are given in the question and will remain the same
# 4 members of staff can deliver 9 items in 10 minutes
time_for_1item_4cooks = 10/9
# 6 members of staff can deliver 16 items in 10 minutes
time_for_1item_6cooks = 10/16

# supporting functions

# function to calculate the average of a list
def calcAverage(list):
    sum = 0                     # Initialization of sum
    for number in list:         # all members of the list
        sum = sum + number      # add the numbers to sum
    average = sum/len(list)     # average = total_sum/ number_of_elements
    return average


# This function will take a list as an input and print out the elements and the number of times they occur in the list
# Used to analyze the number of items in the orders given in csv file, to evaluate the size of orders in the simulation
def summarize_a_list(list):
    content = []                    # contains all the elements in the list
    count = []                      # on the same index as the content, will store the number of occurance of that item
    for element in list:
        if (element not in content):            # if the element is not already present
            position = 0
            for i in range(len(content)):
                if content[i] < element:
                    position += 1
            content.insert(position, element)             # add it
            count.insert(position, 1)                     # set the instance value to one
        else:                                   # otherwise, just find the position of item in content
            pos = content.index(element)
            count[pos] += 1                     # and use increment the same index in count (which stores the occurance)
    for i in range(len(content)):               # print out the information so that we can analyze
        print("order-size: "+ str(content[i])+", count: "+ str(count[i]))



"""
This marks the end of the head section of the program.
The second part(analysis) consist of using the csv file provided to analyze and determine key parameters for the simulation

"""

# Use the given csv file to extract information to design the simulation

# Read values from the csv file
with open('car_orders.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # initialize counters to count the number of cars in A, B, and C in the given csv file (all set to 0) 
    counterA = counterB = counterC = 0
    
    # Intialize an array to store the size of each order, will be used to determine order size for the simulation
    items_ordered = []

    # skip the first two lines of the csv file, as they contain header information
    for i in range(2):
        next(csv_reader)

    #loop through each line in the csv file
    for line in csv_reader:               # each line represent one instance of order
        individual_car_order = 0          #counts the number of items in that order to store it in the items_ordered array

        for value in line:              # value is the individual values in the csv, could be car numbers, orders, or drive through id
            if (value.isnumeric()):     # only pure numeric values like 1, 2 and 3 are orders
                individual_car_order+= int(value)
        
        # the following if blocks will determine the number of cars in each drive through
        if line[0] == 'A':          
            counterA += 1
        if line[0] == 'B':                  # line[0] is the drive through info, each time there is a 'B' the counter for cars in B is incremented
            counterB += 1                   # the same is done for A and C, so that we know the number of cars in all drive throughs
        if line[0] == 'C':
            counterC += 1

        items_ordered.append(individual_car_order)     # the number of items in each order is appended to the array

    
    # Output the data obtained from the csv file and analyze the data

    # number of cars in each drive through
    drive_throughs = ['A', 'B', 'C']
    drive_through_counters = [counterA, counterB, counterC]
    print("Start of analysis section.\n")
    print("Each drive through with the number of cars in the given hour is listed below:\n ")
    for i in range(len(drive_throughs)):
        print("Drive through: "+ drive_throughs[i]+", total cars in an hour: "+ str(drive_through_counters[i]))
    
    # individual orders made by each car

    # the list of orders(items_ordered) made by each car is a long list of numbers and is not quite usable for analysis
    # Therefore, a function that prints unique order sizes (like 3, 11) and the number of times they occur is used.
    # The function is summarize_a_list() and is in the head section of this python file (#line 36 to 51)
    # The output produced by this function helps us better understand the orders and use it for simulation
    print("\nFrom the csv file, the number of items ordered for each order is recorded.")
    print("Each unique order size and the number of times they occur are listed below:\n")
    summarize_a_list(items_ordered)

    # Output the analysis
    print("\nAnalysis of the data obtained from CSV file:\n")
    print("The cars that came in 1 hour in the three drivethroughs are 13, 11 and 12 for A, B and C respectively.")
    print("These numbers are very close to each other, and to their average which is 12. Therefore, I will use an average rate of 12 cars per minute in the simulation.\n")
    print("As per the order size, it can be seen that the order sizes range from 3 to 15 and they occur in a range of 2 to 4 times.")
    print("The order size are listed by the number of times they occur below:\n")
    print("6, 12, 13, 14 order size occur 2 times")
    print("3, 4, 5, 7, 8, 9, 10, 15 order size occur 3 times")
    print("11 order size occurs 4 times")
    print("The number of times each order size occurs is also very close to each other with most order size occuring 3 times (which is the average of 2, 3 and 4).")
    print("Therefore, in the simulation, for each car, the order size will be a number between 3 and 15 with equal probability.\n")
    print("End of analysis section.\n")


# from the analysis, derive key parameters for the simulation

# an average of 12 cars per hour is determined for the simulation
cars_per_hour = 12
cars_per_minute = cars_per_hour/ 60   # 0.2 cars per minute. Therefore will use a 0.2(20%) chance that a car arrives every minute

 
"""
This marks the end of the analysis section of the program.
The third part(simulation) consist of pseudo code and python code for producing a simulation using the information obtained upto this point.
"""

# Part A

# The pseudo code for creating the simulation of drive through is given below:

"""
Pseudo code

algorithm: design a simulation of a drive through for 8 hours that determines average wait time for each car

# design a function that runs a simulation of the drive through for 8 hours 
def simulate(cooknumber):
    current_line_wait_time = 0                                                          # is the time that a car must wait in line before they order, set to 0 in the beginning
    total_wait_times = []                                                               # the list will store wait times of all the cars, will be used to determine the average
    for i in range(480):                                                                # running the simulation minute by minute (8 hours = 480 minutes)

        # invoke a 20% chance, because this is the chance that a car comes in a minute
        i = randint(1, 5)                                                               # generates a random integer from 1 to 5

        if (i == 2):                                                                    # the chance of i being 3 is 1/5 = 20%

            # a car has come
            car_line_wait_time = current_line_wait_time                                 # has to wait in queue if there is one before they can order
            car_order_size = randint(3, 15)                                            # from the analysis, the car orders can be of size 3 to 15 with equal probability
            car_order_preparation_time = car_order_size * the_time_taken_for_1_item     # the time to prepare the car's order for that number of cooks
            car_total_wait_time = car_order_preparation_time + car_line_wait_time       #the time taken = time to prepare the order+ time waiting in line
            append car_total_wait_time to total_wait_times                              # to store the wait time for each car, will be used to calculate average wait time

        if (current_line_wait_time>= 1):                                                  # if there is a queue
            current_line_wait_time -= 1                                        # every passing minute reduces the wait time by a minute
        else if (0 <current_line_wait_time < 1)                                         # if the wait time is less than 1
            current_line_wait_time  = 0                                        # the order is given by the end of the minute

    average_wait_time_for_simulation = (sum of all items in total_wait_times)/length(total_wait_times)
    return average_wait_time_for_simulation

"""

# function to perform simulation
def simulation(number_of_cooks):
    line_wait_time = 0                          # a global line wait time counter, will be wait time for every car before they can order
    all_cars_wait_time = []                       # a list to store the wait time off all cars
    car_counter = 0                                # counts the number of cars in the simulation
    for i in range(480):                       # for every minute (8 hours = 480 minutes (8*60))

        j = randint(1, 5)                       
        if (j == 2):                            # 1/5 = 0.2 or 20%, derived from the csv, the chance that a car comes in a minute

            # use the function described immediately below to calculate the wait time for the car
            current_car_wait_time = determine_wait_time(number_of_cooks, line_wait_time)

            all_cars_wait_time.append(round(current_car_wait_time,2))     # round the value to 2 decimal place and add it to all waiting time list
            line_wait_time = all_cars_wait_time[-1]               # the global wait time is set to the total wait time of the most latest car
            car_counter += 1                                      # increase the car_counter by 1
        if (line_wait_time>=1):                                  # there is a queue
            line_wait_time -= 1                                 # every passing minute reduces the wait time by a minute
        elif (line_wait_time>0 and line_wait_time<1):
            line_wait_time = 0
    the_average_time = round(calcAverage(all_cars_wait_time),2)   # using the wait time of all cars, average wait time is calculated, rounded to 2 decimal place
    return [the_average_time, car_counter]                     # the average wait time and number of cars is returned by the function


# takes as inputs the number of cooks in the kitchen and the time that the car waits in the queue, determines the total waiting time
def determine_wait_time(num_cooks, linewaittime):

    order_size = randint(3, 15)     # refrenced in the analysis part, items ranging 3 to 15 with equal probability are used for orders in the simulation

    if (num_cooks == 4):
        individual_wait_time = order_size * time_for_1item_4cooks   # total_time = total orders * time taken for 1 order
    else:                                                           # 6 cooks
        individual_wait_time = order_size * time_for_1item_6cooks   # total_time = total orders * time taken for 1 order
    return individual_wait_time + linewaittime                      # total wait time = waiting on queue + waiting for own order


# Part B

"""
Pseudo code

algorithm: run multiple executions of simulation and extract the average wait time per car from the result of these simulation

# create a function to run simulation multiple times, the simulation itself will be done by simulation function defined above
def run_10_simulation(cooknumber):          # will take as input the number of cooks in the kitchen

    # create a list to store the results and use for average calculation
    list = []
    for i in range(10):
        instance average waiting time = simulation(cooknumber, 8 hours) # use the cooknumbers and the duration to calculate average wait time of 1 instance
        store this instance wait time in the list

    output the instance wait times
    average_val = calcAverage(wait_times)   # defined in the head section, the function calculate the average of a list
    output the average of the 10 values  


"""

# The function below takes number of cooks and an integer value as input, will run the simulation with that number of cooks for the given number and will output each simulation result as well as the average
def run_10_simulation(cooknumber):
    wait_times = []            # a list to store each instance result, will be used to calculate the average
    print("\nFor "+str(cooknumber)+" cooks, the result of the 10 simulations and their average is listed below:\n")
    for i in range(10):       # run simulation upto the input integer
        result_of_simulation = simulation(cooknumber)
        instance_average_wait_time = result_of_simulation[0]   # returns the average wait time of cars in 1 simulation
        number_of_cars = result_of_simulation[1]
        wait_times.append(instance_average_wait_time)            # the time is appended to the list, for calculating the average of all simulations
        print(" Instance: "+str(i)+", number of cars: "+str(number_of_cars)+", average wait time: "+str(round(instance_average_wait_time, 2))+" minutes.") #result is printed
    the_average_time = calcAverage(wait_times)       # the list is used to deduce the average wait times of all the simulations
    print("\nThe Average wait time: "+ str(round(the_average_time, 2))+" minutes.")     #the result is output

# output the simulation's results
print("\nThe section below contains the simulations and averages using 4 and 6 cooks respectively.\n")
# use the run_10_simulation function to output the results

# for 4 cooks
run_10_simulation(4)
# for 6 cooks
run_10_simulation(6)

# A small part of B and C and D are done in q2.docx in the same directory as this py file
