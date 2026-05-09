"""from DynamicProgramming import DynamicProgramming
from Greedy import Greedy  
from BruteForce import BruteForce"""
import DynamicProgramming
import Greedy   
import BruteForce
print("Enter two strings to align:")
s1 = input("String 1: ")
s2 = input("String 2: ")

x=90
while(x!=4):
    print("Choose an algorithm to align the strings:")
    print("1. Brute Force")
    print("2. Greedy")
    print("3. Dynamic Programming")
    print("4. Exit")
    x = int(input())
    if x == 1:
        print("Brute Force:")
        BruteForce.Brute(s1,s2)
        print("-----------------")
    elif x == 2:
        print("Greedy:")
        Greedy.Greedy(s1,s2)
        print("-----------------")
    elif x == 3:
        print("Dynamic Programming:")
        DynamicProgramming.DynamicProgramming(s1,s2)
        print("-----------------")



