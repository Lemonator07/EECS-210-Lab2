# Name: 
# KUID: 
# LAB Session (Day/Time): 
# LAB Assignment: 
# Description:
#
#
#
# Collaborators/Sources:

#   Note: if you are working in python, you are  
#   REQUIRED to call this function to get your
#   input, so all assignments are consistant 

#   Returns a list of number,letter pairs
def get_mapping_pairs() -> str:
    x = input("Enter your mapping pairs: ")
    items = x.replace("(","").replace(" ","").strip(")").split(")")
    pairs = []
    for item in items:
        pairs.append(item.split(","))
    return pairs

# Your Code Here

#Sample code
#With the following input: (3, A) (2, D) (3, C)
pair_list = get_mapping_pairs()
#The first element of the list is ["3","A"]
print(pair_list[0])
#The first element of the first pair is 3:
print(pair_list[0][0])
#or more clearly:
first_pair = pair_list[0]
print(first_pair[0])