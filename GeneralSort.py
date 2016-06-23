intArray = [4,2,7,8,3,1,9,0,6,5];

print("To be sorted = ", intArray);
print("To be sorted =",end="    ");

while(len(intArray)!=0):
    smallest = intArray[0];
    for i in range(len(intArray)):
        if intArray[i]<smallest:
            smallest = intArray[i];

    print(smallest,end="    ")
    intArray.remove(smallest);
