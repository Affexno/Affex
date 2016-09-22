#! python

#    Affex Asset
#    Library tool
#    Author_Audun_Ase

###
#    IMPORT NEEDED MODULES
###

import sys
import os

###
#    Global Paths
###
drive = os.path.join('your','path','here')
hiplib = os.path.join(drive, 'lib')
hiplog = os.path.join(drive, 'log')
logfile = os.path.join(hiplib, 'lib')
hipfold = (os.listdir(hiplib))

###
#    ASSET HEADING
###

print('Initiate Affex Asset Library')
print('Input number for your chosen function:')

###
#    DEFINE FUNCTIONS
###

def importer(): #Define option 1 HIP Library
    exe = open(os.path.join(drive, 'importer.py'))
    exec(exe.read())
    
def upload(): #Define option 3 Content Upload
    exe = open(os.path.join(drive, 'exporter.py'))
    exec(exe.read())

def toolb(): #Define option 2 Tool box install
    print('Tool box Install')

def sizeof_fmt(num, suffix='B'):        #File size converter.
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def path():
    print(os.path.getsize(os.getcwd()))

###
#    ASSET OPTIONS LIST
###

print('Or press enter to exit.\n')
options = ['Import from Library', 'Export to Library',]
for i in range(len(options)):
    print(str(i) + ' - ' + options[i])


###
#    LAUNCH OPTION CALLS
###

while True:
    response = int(raw_input())
    if response == '':
        sys.exit()
        
    if response == 0:
        importer()
        
    if response == 1:
        upload()
        
    else:
        print('Invalid Option, Please try again.')
        continue
    
sys.exit()
