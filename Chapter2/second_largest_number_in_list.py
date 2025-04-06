number_list = [30,40,70,40,1000,1000,400,200,5]
def second_largest_number(list_array):
    #  First sort array in descending order
   list_array.sort(reverse=True)
#    Add them into set to remove duplicate
   set_list = set(list_array)
#    Return them to lis now
   list_no_duplicates = list(set_list)
   
#    sort them
   list_no_duplicates.sort(reverse=True)
   print(list_no_duplicates)
   print(f"The second largest element of the list is {list_no_duplicates[1]}")

second_largest_number(number_list)