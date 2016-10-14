__author__ = 'A-mdx'

# 安装第三方库，使用。

# 图片压缩

from PIL import Image
im = Image.open('beauty.jpg')
print(im)
print('----------------------------------')
print(im.format,im.size,im.mode)

# 压缩了，10倍

im.thumbnail((204,136))
im.save('thumb.jpg','JPEG')
