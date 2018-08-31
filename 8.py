num=int(input())
hold=num
sum=0
if num<=0:
 print("enter a whole positive number")
else:
 while num>0:
 	sum=sum+num
 	num=num-1
 print(sum)
