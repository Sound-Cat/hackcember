import zipfile as zip
file_name = "geschenk.zip" # Lad dir das bitte selber runter, findest du bei Florian aufm Channel
file = None
numZipped = 2021
x = 0
while x < numZipped:
    with zip.ZipFile(file_name, 'r') as file:
        file_name = file.namelist().pop() # finds all the zipfiles and puts them into "file_name"
        file.extractall() # extracts them all
        x += 1