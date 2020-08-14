list1=[12,-7,5,64,-14]
for i in list1:
    if i>0:
        print(i,end="  ")

list2=[12,14,-95,3]
list_pos=[]
for j in range(len(list2)):
    if list2[j]>0:
        list_pos.append(list2[j])
    else:
        continue
print(list_pos)


