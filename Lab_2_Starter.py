# Name: Carson Lemon
# KUID: 3231409
# LAB Session (Day/Time): Wednesday / 8-10 am
# LAB Assignment: EECS 210 Lab 2
# Description:
# Function identification for a given mapping of numbers to letters.
# The program will determine if the mapping is a function, and if so, whether it is one-to-one and onto.
#
# Collaborators/Sources:


def get_mapping_pairs() -> str:
    x = input("Enter your mapping pairs: ")
    items = x.replace("(","").replace(" ","").strip(")").split(")")
    pairs = []
    for item in items:
        pairs.append(item.split(","))
    return pairs

def main():
    used_letters = []
    used_numbers = []
    onto = True
    oto = True
    notfunction = False
    #define all variables above, including the lists for used values and the boolean values for onto and one-to-one and function value.
    pair_list = get_mapping_pairs() #get list
    for pair in pair_list: #loops through each pair
        number = pair[0] 
        letter = pair[1] #sets the number and letter of current pair in loop
        if number in used_numbers: #if number has already been used, then it is not a function
            notfunction = True #sets function truth value to false
            break
        elif int(number) >= len(pair_list): #if number is greater than or equal to the length of the list, then the function is missing a number.
            notfunction = True #sets function truth value to false
            break
        elif letter in used_letters: #if letter has already been used, then it is not one-to-one
            oto = False
            used_numbers.append(number) #add the number to the used numbers list
        else:
            used_letters.append(letter) #add the letter to the used letters list
            used_numbers.append(number) #add the number to the used numbers list
    if len(used_letters) < len(pair_list): #if the length of the used letters list is less than the length of the pair list, then it could not have used all letters.
        onto = False
    if notfunction: #if function truth value is false, then it prints not function
        print("Not Function")
    else: #otherwise print function and information about one-to-one and onto
        print(f"function, one-to-one: {oto}, onto: {onto}")


main()
