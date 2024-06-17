'''You are given a list of integers, and your task is to write a function that finds the two 
numbers in the list that add up to a specific target sum. You need to retum the indices 
of these two numbers.
Write a function that takes a list of Integers and a target sum as input and returns a 
list of two indices (0-based) of the numbers that add up to the target sum. Assume 
that there is exactly one solution, and you cannot use the same element twice
Sample Input:
2 7 11 15
9
Sample Output:
[0, 1]'''
'''list1=list(map(int,input("enter the list values: ").split()))
sum1=int(input("enter the sum value: "))
n=len(list1)
for i in range(0,n):
    if list1[i]+list1[i+1]==sum1:
        print([list1.index(list1[i]),list1.index(list1[i+1])])
        break
'''
'''--------------------------------------or-----------------------------------------------------------'''
def arr( nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]

list1=list(map(int,input("enter the list values: ").split()))
sum1=int(input("enter the sum value: "))
print(arr(list1,sum1))
