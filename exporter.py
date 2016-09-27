#! python

#    Affex Asset
#    Exporter tool
#    Author_Audun_Ase

#Import used modules.
import os
import datetime



# Initiate Global functions.
drive = os.path.join('your','path','here','hiplib')
hiplib = os.path.join(drive, 'lib')
hiplog = os.path.join(drive, 'log')
logfile = os.path.join(hiplib, 'lib')
hipfold = (os.listdir(hiplib))



hip = str(hou.hipFile.basename())
global hipname
hipname = os.path.splitext(hip)[0]

# Time features.
now = datetime.datetime.now()
timewrite = ''
timewrite = now.strftime('%d-%m-%Y')

# Initial message.
print('\nAffex Exporter v001')
print('Choose your item category:')




##### DEFINITIONS #####

# Build the options list.
def category():
    options = hipfold
    for i in range(len(options)):
            print(str(i) + ' - ' + options[i])

# Builds the option to keep or rename the hip file.
def keepRename():
    kerename = ['keep','rename']
    for i in range(len(kerename)):
            print(str(i) + ' - ' + kerename[i])


def existed():
    print('\nExisting Items:')
    logtxt = category + ('.txt')
    listed = open(os.path.join(hiplog, logtxt)).read().splitlines()

    # Lists logged items from category selection.
    options = listed
    for i in range(len(options)):
	name = (options)[i].split( )[0]
	date = (options)[i].split( )[1]
	print(str(i) + ' - ' + name + ' - created: ' + date)


# Grab path and lets asks user to keep or rename.
def exppath():
    global category
    category = hipfold[resp1]
    print('\nYou have selected ' + category)
    global expath
    expath = os.path.join(hiplib, category)
    print('Your file will be exported to: ' + expath)
    


def keep(): #Let the user keep the filename of the current hip file.
    print('Keeping filename...')
    global newname
    newname = hipname

def rename(): #Let the user input a desired name for the hip file..
    print('Rename file to:')
    global newname
    newname = raw_input()
    print('File has been renamed to ' + newname)

# Gather paths and export.
def export():
    cmdadd = newname + ('.cmd')
    cmdpath = os.path.join(expath, cmdadd)
    if '\\' in cmdpath: #Check if path is valid.
        reform = cmdpath.split('\\')
        formed = '/'.join(reform)

    else:
        formed = cmdpath

    print('Export started...')

    print(cmdpath)
    hou.hscript("opscript -G -r / > " + formed)
    print('Successfully exported')

def loglib():
    global timewrite
    global logtxt
    logtxt = category + ('.txt')
    logfile = os.path.join(hiplog, logtxt)
    logopen = open(logfile, 'a')
    logopen.write(newname+(' '))
    logopen.write(timewrite + '\n')
    print('\nItem logged!')


##### END OF DEFINITIONS #####




# Checking folder and assigning one to category.
options = hipfold
for i in range(len(options)):
    print(str(i) + ' - ' + options[i])

while True: #Check users response
    global resp1
    resp1 = int(raw_input())
    if 0 <= resp1 <= (len(options)-1): #Only accept valid values.	
        exppath()
        break

    if resp1 == '':
	sys.exit()

    else:
        print('Invalid Option, Please try again.')


existed() #Display list of items already in chosen category.


print('\nDo you wish to keep or rename your file?')

#Check users response to the rename function.
while True:
    keepRename()
    resp2 = int(raw_input())
    if resp2 == 0:
        keep()
        break

    if resp2 == 1:
        rename()
        break

    if resp2 == '':
	sys.exit()

    else:
        print('Invalid Option, Please try again.')
        break

export()
loglib()
sys.exit()
