import csv
import math

with open ('data.csv',newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
data = filedata[0]
def mean(data):
    n=len(data)
    total=0
    for x in data :
        total = total+int(x)
    mean=total/n
    return mean 
squarredlist=[]
for num in data:
    a=int(num)-mean(data)
    a=a**2
    squarredlist.append(a)
sum=0
for i in squarredlist :
    sum=sum+i
result = sum/(len(data)-1)
standarddeviation=math.sqrt(result)
print(standarddeviation)
