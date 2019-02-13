# unchanging variables
mph_to_fts_conversion = .681818
sec_to_min = 60.00
mph_to_kmph = 1.60934
kmph_to_mps = .277778
close = 'n'

# Welcome message and instruction
print("\n\tWelcome to the Pace Me Script, Enter the following arguments below:")

user_choice = ''

run_again = True

# Do until user quits
while(run_again):

    # Gather User Input
    print('Distance Traveled in Miles', end=': ')
    distance = float(input())
    print('Time Elapsed in Hours', end=': ')
    time = float(input())

    # Calculate

    # American
    mph = distance / time
    fps = mph * mph_to_fts_conversion
    fpm = fps * sec_to_min

    # Metric
    kmph = mph * mph_to_kmph
    mps = kmph * kmph_to_mps
    mpm = mps * sec_to_min

    # Show results
    print('\nPerforming Calculations...')

    # American 
    print('\nAmerican System:')
    print('%.2f' % round(mph, 2) + ' miles per hour')
    print('%.2f' % round(fpm, 2) + ' feet per minute')
    print('%.2f' % round(fps, 2) + ' feet per second')

    # Metric
    print('\nMetric System:')
    print('%.2f' % round(kmph, 2) + ' kilometers per hour')
    print('%.2f' % round(mpm, 2) + ' meters per minute')
    print('%.2f' % round(mps, 2) + ' meters per second')

    # Check if user wants to do again
    user_input = ""
    while(True):
        print('\nWould you like to run again? (y/n)', end=': ')
        user_input = input()
        user_input.lower()
        
        # Exit if user requests and get out of this loop
        if(user_input == close):
            run_again = False
            print('Bye')
            break
        # Ask again if they enter invalid argument
        elif(user_input != 'n' and user_input != 'y'):
            print('Error. Enter y or n')
        # Exit Loop
        else:
            print()
            break




