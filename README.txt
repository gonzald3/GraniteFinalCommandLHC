FYI:

you can no longer compile this program without specifying the relative path of the GraniteLogo
png



pyinstaller --onefile --add-data "Granite_Logo.png;." --name generatorV9 myapp.py


pyinstaller --onefile --add-data "Granite_Logo.png;." --name [name-of-exe] myapp.py
