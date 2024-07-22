'''
Scenario:
Imagine you are working with a genealogical study to analyze family trees. Each family member (node) has a unique token number associated with them. You want to determine how many descendants of a given family member have prime token numbers. This analysis can help in understanding certain genetic traits or behaviors that might be represented by prime token numbers.

Objective:
Develop a program that can count the number of descendants with prime token numbers for any given family member in a family tree.
'''
import math

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def countPrimeChildren(node, tokens, adjList):
    count = 0
    if isPrime(tokens[node - 1]):
        count += 1
    for child in adjList[node]:
        count += countPrimeChildren(child, tokens, adjList)
    return count

def buildAdjList(parents):
    adjList = [[] for _ in range(len(parents) + 1)]
    for i in range(len(parents)):
        adjList[parents[i]].append(i + 2)
    return adjList

N = int(input())
tokens = list(map(int, input().split()))
parents = [int(x) for _ in range(N - 1) for x in input().split()]
Q = int(input())
queries = [int(input()) for _ in range(Q)]

adjList = buildAdjList(parents)

for query in queries:
    result = countPrimeChildren(query, tokens, adjList)
    print(result)
