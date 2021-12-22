with open("text.txt") as f:
    text = f.read()

binaryText = ""
for notAllowed in ",.!\n\r\"":
    text = text.replace(notAllowed, "")
for word in text.split(" "):
    if "cyber" in word.lower():
        if "cyber-" in word.lower():
            binaryText += "1"
        else:
            binaryText += "0"

print("Binary text:" + binaryText)

print("Entschlüsseltes PW:" + ''.join(chr(int(binaryText[i * 8:i * 8 + 8], 2)) for i in range(len(binaryText) // 8)))
