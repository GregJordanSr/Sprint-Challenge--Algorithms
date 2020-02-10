'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # This method finds the specified substring, If the specified string doesn't exist it returns a -1

    j = word.find("th")

    # Set a control statement so the if the substring isn't found then 0 is returned denoting that the string doesn't exist. 

    if j == -1:
        return 0 

    # Here is where the recursive call is made after finding the first instance of the substring and goes to the end of the input.
    
    return 1 + count_th(word[j + 1:]) 
