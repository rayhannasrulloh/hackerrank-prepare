import math
import os
import random
import re
import sys

def func(n):
    if n%2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
    
if __name__ == '__main__':
    n = int(input().strip())
    
    func(n)