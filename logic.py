player='x'

mylist=['x', ' ', 'x', ' ', 'o', 'o', ' ', 'x', ' ']

win=[[0,1,2],[2,5,8],[6,7,8],[0,3,6],[0,4,8],[2,4,6],[3,4,5],[1,4,7]]
indices = [i for i, x in enumerate(mylist) if x == player]
print(indices)
print(mylist.count(player))
def sublist(lst1,lst2):
    counter=0
    for item in lst2:
        try:
            lst1.index(item)
            counter+=1
        except ValueError:
            pass
    return counter==3
       
for n in win:    
    print(sublist(indices,n),n)

