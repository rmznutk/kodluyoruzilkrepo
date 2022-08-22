
list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
list2 = [[1, 2], [3, 4], [5, 6, 7]]

l1 = []
def flatten(n):
    for i in n: 
        if isinstance(i, list):
            flatten(i)
        else:
            l1.append(i)
flatten(list1)
print(l1)

"""
-------------------------------------
"""

list2.reverse()
for list2for in list2:
    list2for.reverse()
print(list2)
print("hassczx")