'''
This script allows you to open your favorite sites instantly from a menu.

To use this, you will need to create a second file named 'fav_sites_vars'
(I did not wish to share my personal links)
Create string variables to hold links to websites you regularly visit
Edit functions and variables names in this file accordingly

To run, using terminal navigate to directory file exists in
Type py fav_sites.py
Use Program

Last edited February 1st 2019
'''

# Modules
import webbrowser

# Import site link variables
from fav_sites_vars import *

# Global Variables
option = 0
EXIT = 7

# Functions to open sites from selected category

# Google sites suite function
def googleSites():
  # Local variables
  url = ''
  userChoice = 0
  EXIT_GOOGLE_SUITE = 7

  # Continue to gather user input until user elects to exit
  while(True):
    # Show menu
    print('\n\n\tSelect Google Site To Visit')
    print('1.) Google Search')
    print('2.) Main Gmail')
    print('3.) Junk Gmail')
    print('4.) Google Maps')
    print('5.) Personal Google Drive')
    print('6.) YouTube')
    print('7.) Exit to Main Menu')

    # Get user input
    print('\nEnter Input', end=': ')
    userChoice = int(input())

    # Assign local variable based upon user selection. Loop exits if user selects 6
    if userChoice != 1 and userChoice != 2 and userChoice != 3 and userChoice != 4 and userChoice != 5 and userChoice != 6 and userChoice != 7:
      print('Must only select options 1-6')
    elif userChoice == EXIT_GOOGLE_SUITE:
      break
    else:    
      if userChoice == 1:
        url = googleSearch
      elif userChoice == 2:
        url = personalEmail
      elif userChoice == 3: 
        url = junkEmail
      elif userChoice == 4:
        url = googleMaps
      elif userChoice == 5:
        url = personalDrive   
      elif userChoice == 6:
        url = YouTube

    # Send user to url they requested
    webbrowser.open(url)     

  # Return void
  return

# Professional sites function
def professionalSites():
  # Local variables
  url = ''
  userChoice = 0
  EXIT_PROFESSIONAL_OPTIONS = 10

  # Continue to gather user input until user elects to exit
  while(True):
    # Show menu
    print('\n\n\tSelect Education or Job Site to visit')
    print('1.) School Email')
    print('2.) School Google Drive')
    print('3.) Canvas')
    print('4.) LinkedIn')
    print('5.) Glassdoor')
    print('6.) Handshake')
    print('7.) Udemy')
    print('8.) edx')
    print('9.) Price C++ Resources')
    print('10.) Exit to Main Menu')

    # Get user input
    print('\nEnter Input', end=': ')
    userChoice = int(input())

    # Assign local variable based upon user selection. Loop exits if user selects 6
    if userChoice != 1 and userChoice != 2 and userChoice != 3 and userChoice != 4 and userChoice != 5 and userChoice != 6 and userChoice != 7 and userChoice != 8 and userChoice != 9 and userChoice != 10:
      print('Must only select options 1-10')
    elif userChoice == EXIT_PROFESSIONAL_OPTIONS:
      break
    else: 
      if userChoice == 1:
        url = schoolEmail
      elif userChoice == 2:
        url = schoolDrive
      elif userChoice == 3: 
        url = canvas
      elif userChoice == 4:
        url = linked
      elif userChoice == 5:
        url = glassdoor
      elif userChoice == 6:
        url = handshake
      elif userChoice == 7:
        url = udemy
      elif userChoice == 8:
        url = edx 
      elif userChoice == 9:
        url = priceCppResources

    print(userChoice)

    # Send user to url they requested
    webbrowser.open(url)     

  # Return void
  return

# fun sites function
def funSites():
  # Local variables
  url = ''
  userChoice = 0
  EXIT_FUN = 3

  # Continue to gather user input until user elects to exit
  while(True):
    # Show menu
    print('\n\n\tSelect Fun Site To Visit')
    print('1.) Project Mountain')
    print('2.) CoasterForce')
    print('3.) Exit to Main Menu')

    # Get user input
    print('\nEnter Input', end=': ')
    userChoice = int(input())

    # Assign local variable based upon user selection. Loop exits if user selects 6
    if userChoice != 1 and userChoice != 2 and userChoice != 3:
      print('Must only select options 1-3')
    elif userChoice == EXIT_FUN:
      break
    else:    
      if userChoice == 1:
        url = projectMountain
      elif userChoice == 2:
        url = coasterforce 

    # Send user to url they requested
    webbrowser.open(url)     

  # Return void
  return

# shopping sites function
def shoppingSites():
  # Local variables
  url = ''
  userChoice = 0
  EXIT_SHOPPING_SITES = 6

  # Continue to gather user input until user elects to exit
  while(True):
    # Show menu
    print('\n\n\tSelect Shopping Site To Visit')
    print('1.) Amazon')
    print('2.) Patagonia')
    print('3.) REI')
    print('4.) Black Diamond')
    print('5.) La Sportiva')
    print('6.) Exit to Main Menu')

    # Get user input
    print('\nEnter Input', end=': ')
    userChoice = int(input())

    # Assign local variable based upon user selection. Loop exits if user selects 6
    if userChoice != 1 and userChoice != 2 and userChoice != 3 and userChoice != 4 and userChoice != 5 and userChoice != 6:
      print('Must only select options 1-6')
    elif userChoice == EXIT_SHOPPING_SITES:
      break
    else:    
      if userChoice == 1:
        url = amazon
      elif userChoice == 2:
        url = patagonia
      elif userChoice == 3: 
        url = rei
      elif userChoice == 4:
        url = blackDiamond
      elif userChoice == 5:
        url = laSportiva   

    # Send user to url they requested
    webbrowser.open(url)     

  # Return void
  return

# Climbing gym function
def gymSites():
  # Local variables
  url = ''
  userChoice = 0
  EXIT_GYM_SITES = 6

  # Continue to gather user input until user elects to exit
  while(True):
    # Show menu
    print('\n\n\tSelect Climbing Gym Site To Visit')
    print('1.) Upper Limits Maryland Heights')
    print('2.) Upper Limits Bloomington')
    print('3.) Climb SO ILL')
    print('4.) Stone Gardens Bellevue')
    print('5.) Stone Gardens Seattle')
    print('6.) Exit to Main Menu')

    # Get user input
    print('\nEnter Input', end=': ')
    userChoice = int(input())

    # Assign local variable based upon user selection. Loop exits if user selects 6
    if userChoice != 1 and userChoice != 2 and userChoice != 3 and userChoice != 4 and userChoice != 5 and userChoice != 6:
      print('Must only select options 1-6')
    elif userChoice == EXIT_GYM_SITES:
      break
    else:    
      if userChoice == 1:
        url = uliMaryland
      elif userChoice == 2:
        url = uliBloomington
      elif userChoice == 3: 
        url = climbSoIll
      elif userChoice == 4:
        url = stoneGardensBellevue
      elif userChoice == 5:
        url = stoneGardensSeattle   

    # Send user to url they requested
    webbrowser.open(url)     

  # Return void
  return

# Climbing gym function
def travelSites():
  # Local variables
  url = ''
  userChoice = 0
  EXIT_TRAVEL_SITES = 5

  # Continue to gather user input until user elects to exit
  while(True):
    # Show menu
    print('\n\n\tSelect Travel Site To Visit')
    print('1.) Alpine Ascents')
    print('2.) Alpine Institute')
    print('3.) Swoop Patagonia')
    print('4.) Devil\'s Lake Climbing')
    print('5.) Exit to Main Menu')

    # Get user input
    print('\nEnter Input', end=': ')
    userChoice = int(input())

    # Assign local variable based upon user selection. Loop exits if user selects 6
    if userChoice != 1 and userChoice != 2 and userChoice != 3 and userChoice != 4 and userChoice != 5: 
      print('Must only select options 1-6')
    elif userChoice == EXIT_TRAVEL_SITES:
      break
    else:    
      if userChoice == 1:
        url = alpineAscents
      elif userChoice == 2:
        url = alpineInstitute
      elif userChoice == 3: 
        url = swoopPatagonia
      elif userChoice == 4:
        url = devilsLakeTrad

    # Send user to url they requested
    webbrowser.open(url)     

  # Return void
  return

# Show main menu
while option != EXIT:
  # Welcome statement
  print('\n\tSelect which category of site you would like to visit')

  # Menu options
  print('1.) Google Suite')
  print('2.) Education and Career')
  print('3.) Fun')
  print('4.) Shopping')
  print('5.) Climbing Gyms')
  print('6.) Travel and Adventure')
  print('7.) Exit')

  # Gather user input
  print('\nEnter Selection', end=': ')
  option = int(input())
  
  # Handle user input by displaying info or calling function. Loop ends if user enters 4
  if option != 1 and option != 2 and option !=3 and option != 4 and option != 5 and option != 6 and option != 7:
    print('Error: Must only choose options 1-4')
  elif option == EXIT:
    break
  else:
    if option == 1:
      googleSites()
    elif option == 2:
      professionalSites()
    elif option == 3:
      funSites()
    elif option == 4:
      shoppingSites()
    elif option == 5:
      gymSites()
    elif option == 6:
      travelSites()
  

# Exit message
print('\nSite selector exited')