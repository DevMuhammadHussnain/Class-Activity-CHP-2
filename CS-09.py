List = [10, 20 , 30 , 40 , 50 ,60, 70, 80]
Tuples = ("Math" , "Science" , "English" , "History" ,"Geography")
String = "Python Programming"

third_element_of_list = List[-3]
third_element_of_tuples = Tuples[-3]
third_element_of_string = String[-3]


print("Third element of List is : ", third_element_of_list)
print("Third element of Tuples is : ", third_element_of_tuples)
print("Third element of String is : ", third_element_of_string)


slice_list = List[2:5]
slice_tuple = Tuples[2:5]

print("Slice of List from index 2 to 5 is : ", slice_list)
print("Slice of Tuples from index 2 to 5 is : ", slice_tuple)

print("Last two element of list : " , List[-1] , List[-2])
print("Last two element of tuples : " , Tuples[-1] , Tuples[-2])

print("Last two element of string : " , String[-1], String[-2])

