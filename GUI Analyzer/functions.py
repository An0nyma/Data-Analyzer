from math import ceil, sqrt
import json

with open("data.json", "r") as data_file:
    data = json.load(data_file)
function_names = data["function data"]["function names"].copy()
outliers_modes = data["function data"]["outlier(s) mode(s)"].copy()
del data

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
    org, unorg = [], []
    for i in nums:
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
                    unorg.append(nums.pop(nums.index(i)))
    while 0 in org:
        org.remove(0)
    for i in org:
        if (str(i)+' ')[-3:-1]=='.0':
            a = org.count(i)
            for ii in range(0, a):
                org[org.index(i)+ii]=int(i)
    return org, unorg

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

def correctSpacing(new_line, spacing):
    new_line = str(int(new_line))
    spacing = str(spacing+2)
    correctspacing = new_line + '.' + spacing
    return correctspacing

def newLine(nums, spacing, numsornot):
    iLen, position, numofreturns = 0, 0, 0
    nextspacing, spacing = 65, 66-spacing
    clean = nums.copy()
    for i in nums:
        if numsornot == 'not':
            iLen += len(str(i))+1
        else:
            iLen += len(str(i))+2
        if iLen > spacing:
            spacing += nextspacing
            clean[clean.index(i, position)] = f'\n {i}'
            iLen += len(str(i))
            numofreturns+=1
        position += 1
    if numsornot == 'nums':
        clean = ", ".join(str(num) for num in clean)
    elif numsornot == 'not':
        clean = " ".join(str(nan) for nan in clean)
    elif numsornot == 'outliers':
        clean = ", ".join(str(outlier) for outlier in clean)
        if len(clean.split())!=1 or clean=='None':
            function_names[10] = outliers_modes[0]
        else:
            function_names[10] = outliers_modes[1]
        return function_names[10]
    elif numsornot == 'modes':
        clean = ", ".join(str(mode) for mode in clean)
        if len(clean.split())!=1 or clean=='None':
            function_names[11] = outliers_modes[2]
        else:
            function_names[11] = outliers_modes[3]
        return function_names[11]
    return clean, numofreturns

def allOutputs(nums, notnums):
    l2g = newLine(nums, len(function_names[0]), 'nums')
    outliers = newLine(findOutliers(nums, findQuartiles(nums)), len(function_names[10]), 'outliers')
    outliers = newLine(findOutliers(nums, findQuartiles(nums)), len(function_names[10]), 'nums')
    modes = newLine(findMode(nums), len(function_names[11]), 'modes')
    modes = newLine(findMode(nums), len(function_names[11]), 'nums')
    if len(notnums) == 0:
        notnums = ['All are numbers', 0]
    else:
        notnums = newLine(notnums, len(function_names[1]), 'not')

    #debug menu, do not remove any of the '#'

    # print(f"L2g: {l2g[0]}")

    # print(f"nan: {notnums[0]}")
    
    # print(f"range: {nums[-1] - nums[0]}")

    # print(f"mean: {findMean(nums)}")
    
    # print(f"variance: {findVariance(nums, findMean(nums))}")
            
    # print(f"q1: {findQuartiles(nums)[0]}")        
            
    # print(f"med: {findQuartiles(nums)[1]}")        
    
    # print(f"q3: {findQuartiles(nums)[2]}")
    
    # print(f"iqr: {findQuartiles(nums)[3]}")

    # print(f"outliers: {outliers[0]}")

    # print(f"mode: {modes[0]}")

    # print(l2g[1], notnums[1], outliers[1], modes[1])

    return (l2g[0],
            notnums[0],
            nums[-1] - nums[0],
            findMean(nums),
            findVariance(nums, findMean(nums)),
            sqrt(findVariance(nums, findMean(nums))),
            findQuartiles(nums)[0],
            findQuartiles(nums)[1],
            findQuartiles(nums)[2],
            findQuartiles(nums)[3], 
            outliers[0],
            modes[0]
        ), l2g[1], notnums[1], outliers[1], modes[1]

new_lines=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]