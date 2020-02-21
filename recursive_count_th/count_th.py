'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = 0):
    
    # TBC
    # ? if word doesn't contain "th" return 0 base case
    th_index = word.find('th')

    if th_index < 0:
        return count
 
    # increment counter if there is an index
    count += 1

    # recurse with new string
    return count_th(word[th_index + 2 : ], count)
