#Adding Master Comments
import sys
import os
from PIL import Image
#import blob
from PIL import Image, ImageFilter
print(f"the name of the file is {sys.argv[0]}")
print(f"the number of arguments is {len(sys.argv)}")
print(f"the argumentsss is {str(sys.argv)}")


print(sys.argv[1])
print(sys.argv[2])

x = os.getcwd() + '\\' + sys.argv[1]
os.chdir(x)

for f in os.listdir():
    print(f)
    img1 = Image.open(f)
    #img2 = img1.convert('L')
    sav = ' C:\Users\Sakthi\Desktop\Python\Python Dev\mypyproject\Image Processing\PNG\'
    print(sav)
    #img1.save(sav,'png')




