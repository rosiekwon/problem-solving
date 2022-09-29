import math
import os
import random
import re
import sys

name = []
if __name__ == '__main__':
    N = int(input().strip())

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1].split('@')[1]
        if emailID == 'gmail.com':
            name.append(firstName)

#Print an alphabetically-ordered list of first names for every user with a gmail account. 
# Each name must be printed on a new line.            
for item in sorted(name):
    print(item)
