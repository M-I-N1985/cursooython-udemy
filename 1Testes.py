def func(*args):
    print(args)

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10]
#a, b, *args = list
#print(a, b, args)

#func(a, b, args)
func(*list1)
func(list1,list2)
func(*list1,*list2)