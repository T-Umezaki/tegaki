import base64

file = open('ocr.jpg', 'rb').read()
string = base64.b64encode(file).decode("UTF-8")
# string = "b'qqq'"
# string = string[1:len(string)]
print(string)
'''
with open("ocr.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(str)
'''