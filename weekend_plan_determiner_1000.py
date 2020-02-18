# Random number generator to determine what to do

# Random library
import random as r 

# Options
option_list = ['Climb in Golden and Visit Ashley\'s family', 'Van camp and ski at Monarch', 'Climb at Shelf Road']

def randomly_select():
    '''
    Argument: List of options
    Returns: Tuple of option counts
    Description: Randomly chooses option 1-3 for 100 times. Returns sum of results
    '''
    i = 0
    j = 0
    k = 0
    counter = 0
    while counter < 100:
        result = r.randint(0, 2)
        if result == 0:
            i += 1
        elif result == 1:
            j += 1
        else:
           k += 1
        counter += 1
    return (i, j, k)

def display_results(option_results, option_list):
    '''
    Arguments: tuple of count of selections between 0 - 100. List of options 
    '''
    selection = ''
    if option_results[0] > option_results[1] and option_results[0] > option_results[2]:
        selection = option_list[0]
    elif option_results[1] > option_results[0] and option_results[1] > option_results[2]:
        selection = option_list[1]
    elif option_results[2] > option_results[0] and option_results[2] > option_results[1]:
        selection = option_list[2]
    else: 
        selection = 'Tie occurred. Rerun program'
    return selection

# Run
test = randomly_select()
print(test)
selection_result = (display_results(test, option_list))
print(selection_result)