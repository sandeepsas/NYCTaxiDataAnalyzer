myList=[1,2,3,4,5,6]
print ("Before Reverse = ",myList,end=' ')

length = len(myList)//2
for i in range(length):
    temp = myList[len(myList) - 1 - i];
    myList[len(myList) - 1 - i] = myList[i];
    myList[i] = temp;

print ("\nAfter Reverse = ",myList,end=' ')