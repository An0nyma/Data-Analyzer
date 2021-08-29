#!usr/bin/env python

import sys
from math import sqrt, ceil
from colorama import Fore, Style, init
init(autoreset=True)

def findMean(nums):
    mean = 0
    for num in nums:
        mean += float(num)
    return mean/len(nums)

def findVariance(nums, mean):
    variance = 0
    for num in nums:
        variance += (float(num)-mean)**2
    return variance/len(nums)

def findOutliers(nums, quartiles):
    minimum, maximum, outliers = quartiles[0]-quartiles[3], quartiles[2]+quartiles[3], []
    for i in nums:
        if i>maximum or i<minimum:
            outliers.append(i)
    if len(outliers)==0:
        outliers=['None']
    return outliers

def findMode(nums):
    mode = [0]
    for i in nums:
        if nums.count(i)==mode[0]:
            mode.append(' ')
            if i in mode[1:-1]:
                mode.remove(' ')
                continue
            else:
                mode.append(i)
                mode.remove(' ')
        elif nums.count(i)>mode[0]:
            mode = [nums.count(i), i]
    mode.remove(mode[0])
    if len(nums) == len(mode):
        mode = ['None']
    return mode

def organiseList(nums):
    org = []
    for i in nums:
        if i in ['break', 'exit']:
            sys.exit(0)
        try:
            nums[nums.index(i)] = float(i)
        except:
            continue
    while True:
        try:
            for i in range(0, len(nums)):
                org.append((nums.pop(nums.index(min(nums)))))
            break
        except:
            for i in nums:
                if type(i)==str:
                    del nums[nums.index(i)]
    while 0 in org:
        org.remove(0)
    for i in org:
        if (str(i)+' ')[-3:-1]=='.0':
            a = org.count(i)
            for ii in range(0, a):
                org[org.index(i)+ii]=int(i)
    return org

def findQuartiles(nums):
    if len(nums)%2==0:
        medianA, medianB = int(len(nums)/2-1), int(len(nums)/2)
        median = (nums[medianA] + nums[medianB])/2
        if (medianA+1)%2==0:
            quartileA, quartileB = int((medianA+1)/2), int((medianA-1)/2)
            quartile1 = (nums[quartileA] + nums[quartileB])/2
            quartileA, quartileB = quartileA + medianB, quartileB + medianB
            quartile3 = (nums[quartileA] + nums[quartileB])/2
        else:
            quartile1 = nums[int((medianA)/2)]
            quartile3 = nums[int(medianA/2+medianB)]
    else:
        median = int(round((len(nums)-1)/2))
        if median%2==0:
            quartileA, quartileB = int(median/2), int(median/2-1)
            quartile1 = (nums[quartileA] + nums[quartileB])/2
            quartileA, quartileB = int(1.5*median), int(1.5*median+1)
            quartile3 = (nums[quartileA] + nums[quartileB])/2
        else:
            quartile1 = nums[int(round((median-1)/2))]
            quartile3 = nums[ceil(1.5*median)]
        median = nums[median]
    return quartile1, median, quartile3, quartile3-quartile1

print(f'{Style.BRIGHT}{Fore.RED}You can write \'break\' or \'exit\' to stop the app. The terminal version of this app does not include a NaN section and has not been updated after having made the MacOS-only GUI version.')

while True:
    nums = organiseList(" ".join(input(f"{Style.BRIGHT}{Fore.WHITE}               Data:{Style.NORMAL} ").split(",")).split())
    if len(nums)<2:
        print(f'{Style.BRIGHT}{Fore.WHITE}               Have at least two numbers, please try again.\n')
        continue
    print(f'{Style.BRIGHT}{Fore.WHITE}  Least to Greatest:{Style.NORMAL} {", ".join(str(num) for num in nums)}')
    print(f'{Style.BRIGHT}{Fore.RED}               Mean:{Style.NORMAL} {findMean(nums)}')
    print(f'{Style.BRIGHT}{Fore.RED}           Variance:{Style.NORMAL} {findVariance(nums, findMean(nums))}')
    print(f'{Style.BRIGHT}{Fore.RED} Standard Deviation:{Style.NORMAL} {sqrt(findVariance(nums, findMean(nums)))}')
    print(f'{Style.BRIGHT}{Fore.GREEN}         Quartile 1:{Style.NORMAL} {findQuartiles(nums)[0]}')
    print(f'{Style.BRIGHT}{Fore.GREEN}             Median:{Style.NORMAL} {findQuartiles(nums)[1]}')
    print(f'{Style.BRIGHT}{Fore.GREEN}         Quartile 3:{Style.NORMAL} {findQuartiles(nums)[2]}')
    print(f'{Style.BRIGHT}{Fore.GREEN}Interquartile Range:{Style.NORMAL} {findQuartiles(nums)[3]}')
    print(f'{Style.BRIGHT}{Fore.BLUE}           Outliers:{Style.NORMAL} {", ".join(str(outlier) for outlier in findOutliers(nums, findQuartiles(nums)))}')
    print(f'{Style.BRIGHT}{Fore.BLUE}               Mode:{Style.NORMAL} {", ".join(str(mode) for mode in findMode(nums))}')
    print()