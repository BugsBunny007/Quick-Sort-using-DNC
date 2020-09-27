def partition(array,f,l):
    #index of smaller element
    i=f-1
    # pivot element
    pivot= array[l]
    for j in range(f,l):
        if array[j]<= pivot:
            # increment index of smaller element
            i = i+1
            array[i],array[j] = array[j],array[i] 
    array[i+1],array[l] = array[l],array[i+1]
    return i+1
def QuickSort(arr,f,l):
    if f < l:
        p = partition(array,f,l)
        QuickSort(array,f, p-1)
        QuickSort(array, p+1,l)
# Driver code to test above 
array=[]
n= int(input("Enter quantity :"))
for i in range(n): 
    print("Enter value ",i+1)        
    array.append(int(input()))

QuickSort(array,0,n-1) 

print ("Sorted array is:") 

for i in range(n):
    print ("%d" %array[i]),


#OUTPUT:-
#python QSR.py 
#Enter quantity :5
#('Enter value ', 1)
#1
#('Enter value ', 2)
#3
#('Enter value ', 3)
#4
#('Enter value ', 4)
#58
#('Enter value ', 5)
#6
#Sorted array is:
#1 3 4 6 58

