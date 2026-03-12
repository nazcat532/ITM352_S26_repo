# Retrieving elements from a list 

def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: Index out of range"
    
my_list = [1, 2, 3, 4, 5]

print(get_element(my_list, 2))  
print(get_element(my_list, 5))