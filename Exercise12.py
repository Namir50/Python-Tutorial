list  = [1,2,3,4,5,6,7,8,9,10]

def even(li):
    for i in li:
        if i%2==0:
            print(i, end = " ")
print(even(list))    