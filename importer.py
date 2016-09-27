#! python

#    Affex Asset
#    Importer tool
#    Author_Audun_Ase

###
#    Import modules
###

import os
import datetime
import sys

###
#    Global definitions
###

now = datetime.datetime.now()
timewrite = now.strftime('%d-%m-%Y')

###
#    File paths
###

drive = os.path.join('your','path','here','hiplib')
hiplib = os.path.join(drive, 'lib')
hiplog = os.path.join(drive, 'log')
logfile = os.path.join(hiplib, 'lib')
hipfold = (os.listdir(hiplib))


###
#    Definitions.
###

def category():
    global category
    global impresp
    global chop
    chop = hipfold[impresp]
    category = chop + ('.txt') 
    print('\nYou have selected ' + category)
    
def imported():
    cmd = spSel + '.cmd'
    importpath = os.path.join(hiplib,chop,cmd)
    if '\\' in importpath: #Check if path is valid.
        impreform = importpath.split('\\')
        impformed = '/'.join(impreform)    
    else:
        impformed = importpath
    hou.hscript("cmdread " + impformed)
    print('Successfully imported: ' + spSel)
    sys.exit()
    

# Start Functions.

print('Library opened. Please select your category:')

# Checking folder and assigning one to category.
options = hipfold
for i in range(len(options)):
    print(str(i) + ' - ' + options[i])

while True: #Check users response
    impresp = int(input())
    if 0 <= impresp <= (len(options)-1): #Only accept valid values.
        category()
        break
    
    if impresp == '':
        sys.exit()

    else:
        print('Invalid Option, Please try again.')
        continue

# Create required paths for list.
listed = open(os.path.join(hiplog, category)).read().splitlines()
tlist = open(os.path.join(hiplog, category)).read()
filecheck = os.path.join(hiplog, category)


# If category is empty, let user know.
if os.path.getsize(filecheck) == 0:
        print('This category is empty.')
        sys.exit()
else:
    print('Please choose an item for import:\n')



# Lists logged items from category selection.
options = listed
for i in range(len(options)):
    name = (options)[i].split( )[0]
    date = (options)[i].split( )[1]
    print(str(i) + ' - ' + name + ' - created: ' + date)


while True: #Check users response
    response = int(input())
    if 0 <= response <= (len(options)-1): #Only accept valid values.
        global spSel
        spSel = (listed)[response].split( )[0]
        imported()
        break

    if response == '':
        sys.exit()

    else:
        print('Invalid Option, Please try again.')
        break

sys.exit()
