import zipfile as zip
file = "geschenk.zip" # Lad dir das bitte selber runter, findest du bei Florian aufm Channel
numofTrys= 0
maxNumofTrys = 4
with open("rockyou.txt", "rb") as f: # Lad dir das bitte selber runter, findest du bei Florian aufm Channel
    for word in f:
        if(len(word.strip()) == (24*4)): # weil ja gesagt wurde dass das passwort genau 4 mal so lang ist wie die tage im adventskalender
            try:
                zip.ZipFile('geschenk.zip').extractall(pwd=word.strip()) # versuchen ob es zu entpacken geht
            except:
                continue