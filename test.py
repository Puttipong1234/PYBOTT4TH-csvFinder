List = [1,2,3,4]

new_List = []
for i in List:
    new_List.append(i+2)

new_List = [i+2 for i in List]

print(new_List)
