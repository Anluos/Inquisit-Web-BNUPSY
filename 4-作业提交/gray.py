work_dir="D:/Iquisit/class/gray/"

from PIL import Image
im = Image.open('Manakin.jpg').convert('L')
#im = Image.open('blank.bmp').convert('L')
from PIL import ImageDraw
draw = ImageDraw.Draw(im)
for x in range(1, 17):
    for i in range(0, list(im.size)[0]):
            for j in range(0, list(im.size)[1]):
                    color = im.getpixel((i, j))
                    #改变灰度值
                    color = color - 2
                    point = [i, j]
                    draw.point(point, color)
                    #在每个点画出来~~
    im.save('pic'+str(x-1)+'.jpg')