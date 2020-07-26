# @author Cam Lischke <lisccd18@wfu.edu>
# Program 2a
# CSC 222 Dr. Ballard
#
# You are given a knapsack of capacity W and n items with weights {wi} and values {vi}. The goal is to identify a subset
# of the items S with maximal value, equal toPi∈S vi, subject to the constraint thatPi∈S wi ≤ W. Each item may be included
# at most once.
#
# This problem will be solved using a dynamic programming algorithm
#


""" This function reads the input file and returns the array after the entire input file has been linearized and split
"""
def read(filename):
    input = ""
    with open(filename, 'r') as file:
        for line in file:
            input += line
    array = input.split()
    return array


'''This one is for a 2d table implemented using the dynamic programming algorithm.
'''
def main():
    weights = []
    weights.append(0)       #this allows for 1-indexing (which makes the for loops easier)
    values = []
    values.append(0)        #this allows for 1-indexing (which makes the for loops easier)
    temp = read("small.txt")

    #takes the input and appends values and weights to respective lists
    cap = int(temp[1])
    n = int(temp[3])
    for i in range(5, len(temp) - 2, 4):
        weights.append(int(temp[i]))
        values.append(int(temp[i+2]))

    #KNAPSACK OPTIMAL VALUE
    table = [[0 for x in range(cap+1)] for x in range(n+1)]     #[[cols]rows]
    for i in range(1, n+1):
        for b in range(1, cap+1):
            if weights[i] <= b:
                table[i][b] = max(values[i]+table[i-1][b-weights[i]], table[i-1][b])
            else:
                table[i][b] = table[i-1][b]

    bestVal = table[n][cap]
    print("Using a 2d table: " + str(bestVal))


''' This main method uses the same algorithm, except since the table lookups only involve the row
    row directly above the current row, it will only store that row, instead of an entire 2d array. It will make
    backtracing a little harder, but for this part of the program, it greatly improves the memory complexity.
'''
def main2():
    weights = []
    weights.append(0)       #this allows for 1-indexing (which makes the for loops easier)
    values = []
    values.append(0)        #this allows for 1-indexing (which makes the for loops easier)
    temp = read("small.txt")

    #takes the input and appends values and weights to respective lists
    cap = int(temp[1])
    n = int(temp[3])
    for i in range(5, len(temp) - 2, 4):
        weights.append(int(temp[i]))
        values.append(int(temp[i+2]))

    #KNAPSACK OPTIMAL VALUE STORING ONLY ONE FULL ROW AND THE CURRENT ROW
    above = [0 for x in range(cap+1)]       #this one stores the row above
    for i in range(1, n+1):
        current = [0 for x in range(cap+1)]               #this stores the current row
        for b in range(1, cap+1):
            if weights[i] <= b:
                current[b] = max(values[i]+above[b-weights[i]], above[b])
            else:
                current[b] = above[b]
        above = current             #above is overwritten at the end of filling up current

    bestVal = above[cap]
    print("Storing only one row: " + str(bestVal))




if __name__ == "__main__":
    main()
    main2()
