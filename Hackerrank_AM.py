#Solution to Array Manipulation Problem on hackerrank
#Used Prefix sum array algorithm
#https://www.hackerrank.com/challenges/crush/problem

#code :


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.

#this is the method that worked for me, used a dictionary that keeps track of start value as key and the summant value as
#its value. The end + 1 value holds -ve summant for colateral when presum array is used
# Avoids the error due to massive memory usage of declaring arrays
def arrayManipulation(n,queries):
    A = {}
    res = []
    for x in queries:
        s = x[0]
        e = x[1] + 1
        ad = x[2]
        A.setdefault(s,0)
        A[s] += ad
        A.setdefault(e,0)
        A[e] -= ad
    srt = sorted(A)
    res.append(A[srt[0]])
    
    for z in range (1,len(srt)):
        res.append(A[srt[z]]+res[z-1])
        #print(res)
    #print(res)
    #print(A)
    return(max(res))

    ''' 
Test Case
5 3
1 2 100
2 5 100
3 4 100

we get the dictionary at the end as of first iteration as : 
{
    1 : 100
    3 : -100
}
2nd
{
    1 : 100
    3 : -100
    2 : 100
    6 : -100
}
3rd
{
    1 :100
    3 : 0
    2 : 100
    6 : -100
    5 : -100
}
resultant array is [100,200,200,200,100,0] (ignore 6th element)
and max is 200 
return max
Time Complexity : O(n) 
    '''

    


# this uses method uses only the prefix method, causes errors on very high number of inputs (Array Memory)

def arrayManipulation1(n, queries):
    A = [0]*(n+1)
    maxe = -9999
    
    for x in queries:
        s = x[0] - 1
        e = x[1]
        A[s] += x[2]
        if e != len(A):
            A[e] -= x[2]
    maxe = A[0]  
    print(A)  
    for azac in range(1,n+1):
        A[azac] = A[azac] + A[azac-1]
        maxe = A[azac] if A[azac] > maxe else maxe
    #return(maxe)
    print(A)
     

# IGNORE THIS , JUST TAKING INPUT FROM STD
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()



''' 
Sample Test Case
5 3
1 2 100
2 5 100
3 4 100

Code Written By Pruthvi Shetty
29-04-2020
'''