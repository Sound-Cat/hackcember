from PIL import Image, ImageChops
firstImg = Image.open(r"2.png").convert("1") # opens first image and converts into only black and white
secondIMG = Image.open(r"1.png").convert("1") # the same with the 2nd img
im3 = ImageChops.logical_xor(firstImg, secondIMG) # makes a xor comparison between the too imgs
im3.save("3.png") # saves the output