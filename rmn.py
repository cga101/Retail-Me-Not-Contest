#imports (non-3rd Party)
import re
import csv 
from math import sqrt
from collections import defaultdict, Counter

#Data Structures
##Counter for Website Total Times
timeCounter = Counter()
minMaxCounter = Counter()

##Hashtables for Operations
hashMerchant = defaultdict(list) 
hashStore = defaultdict(list)
hashVisitors = defaultdict(list)

#Question 1 Functions
##Sort Array, Count Forward and Backwards to get Min/Max Occurances
def getMinMax(x):
	minMaxCounter.clear()
	for i in x:
		minMaxCounter[i] += 1
	lst = minMaxCounter.most_common()
	return lst[0]

##Add all elements in x and divide by n
def getMean(x):
	return float(sum(map(int,x))/len(x))

##Median - Sort the Array, Then Return x[n/2]
def getMedian(x):
	x = sorted(x)
	index = (len(x) - 1 ) // 2
	if len(x) == 1:
		return float(x[index])
	elif (len(x) % 2):
		return x[index]
	else:
		return (float(x[index]) + float(x[index+1]))/2.0

##Receive mean and array, subtract mean from each element, divide by n-1
def getDev(m, x):
	vals = 0
	if len(x) == 1:
		return 0.0
	else:
		for i in x:
			vals += pow((float(i)-m),2)
		vals = vals/len(x)
		return sqrt(vals)
	
#Open File for Reading
f = open('rmn.log', 'r')
print f

#Put Relevant Lines to Appropriate Tables
for line in f :
	if not line: 
		break
	if re.search("GET /out/\d*", line):
		coupon = re.search("/\w?\d* ", line)	
		time = re.search(":\d+:\d+:", line)
		retailer = re.search("/view/\w*\.", line)
		ip = re.search("\A.* -", line)
		if coupon and time:
			coupon = coupon.group(0)[1:]
			time = time.group(0)[4:-1]
			hashMerchant[coupon].append(time)
			timeCounter[time] += 1
			if retailer:
				retailer = retailer.group(0)[6:-1]
				hashVisitors[retailer].append(ip.group(0))
	elif re.search("GET /view\d*/", line):
		retailer = re.search("/view/\w*\.", line)
		ip = re.search("\A.* -", line)
		if retailer:
			retailer = retailer.group(0)[6:-1]
			hashStore[retailer].append(ip.group(0))

#Write to CSV 1 - Out Requests
with open('csvClicks.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['Coupon','Num. Of Clicks','Min/Max','Mean','Meadian','Std. Dev'])
	for key, value in hashMerchant.items():
		writer.writerow([key.strip(),len(value),getMinMax(value),getMean(value),getMedian(value),round(getDev(getMean(value), value),3)])

#Write to CSV 2 - Bounce Rate
with open('csvBounce.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['Name','Visitor Clicks','Total Clicks','Bounce Rate'])
	for key, value in hashStore.items():
		store = key
		visitors = 0
		total = len(value)
		visitLst = hashVisitors[store]
		for i in value:
			if i in visitLst:
				visitors += 1
		nonVisitors = total - visitors
		bounce = float(nonVisitors) / float(total)
		if store:
			writer.writerow([store.strip(),visitors,total,round(bounce,3)])

#timeCounter.most_common();

