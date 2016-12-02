from PIL import Image
im = Image.open('pic.jpg').convert('L')
im.save('graypic1.jpg')
from PIL import ImageDraw
draw = ImageDraw.Draw(im)
for x in range(1, 16):
    for i in range(0, list(im.size)[0]):
            for j in range(0, list(im.size)[1]):
                    color = im.getpixel((i, j))
                    # 改变灰度值
                    color = color + x
                    point = [i, j]
                    draw.point(point, color)
    # im.show('pic1.jpg')
    im.save('pic'+str(x)+'.jpg')
# 彩色封面图像转为灰度图像并显示出来：
# from PIL import Image
# pil_im = Image.open('cover.png').convert('L')
# pil_im.show()

# 灰度图片处理参考：按像素改变灰度值
# def addNoise(im, mode, value):
#     draw = ImageDraw.Draw(im)
#     for i in range(0, list(im.size)[0]):
#         for j in range(0, list(im.size)[1]):
#             if mode == "uniform": 　　　　　　　＃UNIFORM噪声
#             rnd = random.uniform(value[0], value[1])
#         elif mode == "normal":          ＃UNIFORM噪声
#         rnd = random.gauss(value[0], value[1])
#     elif mode == "lognormal":
#     rnd = random.lognormvariate(value[0], value[1])
#
# elif mode == "negexp":
# rnd = random.expovariate(value[0], value[1])
# elif mode == "gamma":
# rnd = random.gammavariate(value[0], value[1])
# elif mode == "beta":
# rnd = random.betavariate(value[0], value[1])
# elif mode == "pareto":
# rnd = random.paretovariate(value[0])
# elif mode == "weibull":
# rnd = random.weibullvariate(value[0], value[1])
#
# if im.mode == "RGB":
#     color = list(im.getpixel((i, j)))
#     color[0] = color[0] + rnd
#     color[1] = color[1] + rnd
#     color[2] = color[2] + rnd
#     point = [i, j]
#     draw.point(point, tuple(color))
# elif im.mode == "L":
#     color = im.getpixel((i, j))
#     color = color + rnd
#     point = [i, j]
#     draw.point(point, color)
# else:
#     print
#     "File type not supported!"
#     sys.exit(1)
# del draw
# return im