
#1
l = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
l1 = []

def flatten(l):

 for i in l:
    if isinstance(i, list):
        flatten(i)
    else:
        l1.append(i)

flatten(l)
print(l1)


#2
mylist = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(inputlist: list):
 for i in inputlist:
        i.reverse()
 inputlist.reverse()    
 return(inputlist)

print(reverse_list(mylist))
