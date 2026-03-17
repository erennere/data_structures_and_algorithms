"""
List operations and exercises module.

This module demonstrates basic Python list operations and practical exercises
including average calculation, temperature analysis, and list manipulation.

Key Demonstrations:
    - List methods: insert, pop, remove, append
    - List queries: min, max, len
    - List statistics: sum, average
    - Temperature analysis: Calculate mean and days above average

This module includes practical examples showing how to use lists effectively
in real-world scenarios involving data collection and analysis.

Usage:
    Run this module to see interactive examples that accept user input
    for temperature analysis and statistical calculations.
"""
myList.insert(4,4)
print(myList)

print(myList.pop())
print(myList)

del myList[1]
print(myList)

myList.remove(4)
print(myList)

secondList = ['fvcdb', 'addsf', 'sdfsc']
print(min(secondList))
print(max(secondList))

i = 0
myList = []
while i < 5:
    myList.append(float(input('Input number:')))
    i += 1
print(f'average: {sum(myList)/len(myList)}')


################Project 1#########################3
import numpy as np

dayNumber = int(input('number of days:'))

i = 0
temperatures = []
while i < dayNumber:
    temperatures.append(float(input('temperature of the day:')))
    i += 1

meanTemperature = round(sum(temperatures)/len(temperatures),2)

higherDays = [t for t in temperatures if t > meanTemperature]

print(f'average temperature: {meanTemperature}')
print(f'number of days with above average temperature: {len(higherDays)}')


