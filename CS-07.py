def calculate_largest_number(list): 
   largest = list[0]
   for i in list:
      if i>largest:
         largest = i
   print("Largest Number Among", list , "is" , largest)

calculate_largest_number([1,2,3,1,2, 200 , 2_99999999])