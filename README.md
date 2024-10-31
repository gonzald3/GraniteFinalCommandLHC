# FinalCommandGenerator
# GraniteFinalCommandLHC
FYI:

you can no longer compile this program without specifying the relative path of the GraniteLogo
png

Step 1: clone the file from the git repo link
Step 2: cd into the new folder named GraniteFinalCommandLHC
Step 3: run the following command notice the second line showing what you will call the app in the example I use generatorV9

pyinstaller --onefile --add-data "Granite_Logo.png;." --name [name-of-exe] myapp.py
for Example: pyinstaller --onefile --add-data "Granite_Logo.png;." --name generatorV9 myapp.py
is the app named generatorV9

Finally you run the app from the new EXE named after you app in the dist . cd into the dist
