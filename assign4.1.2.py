def filter_long_words(list,n):
    newlist=[]
    for i in list:
        if len(i)>n:
            newlist.append(i)
    return newlist
list=['abc','add','snejkr']
n=int(input("enter n"))
list=filter_long_words(list,n)
print(list)