# coding=utf-8
from wxpy import *
import math
from PIL import Image
import os


'''
pip install wxpy
pip install Pillow==4.2.1
'''


def creat_filepath():
    avatar_dir = os.getcwd() + "/wechat/"
    if not os.path.exists(avatar_dir):
        os.mkdir(avatar_dir)
    return avatar_dir


def save_avatar(avatar_dir):
    bot = Bot()
    friends = bot.friends(update=True)
    num = 0
    for friend in friends:
        friend.get_avatar('{}/{}.jpg'.format(avatar_dir, str(num)))
        print(u'好友昵称: %s' % friend.nick_name)
        num += 1


def joint_avatar(path):
    length = len(os.listdir(path))
    image_size = 2560
    each_size = int(math.ceil(2560 / math.floor(math.sqrt(length))))
    x_lines = int(math.ceil(math.sqrt(length)))
    y_lines = int(math.ceil(math.sqrt(length)))
    image = Image.new('RGB', (each_size * x_lines, each_size * y_lines))
    x = 0
    y = 0
    for (root, dirs, files) in os.walk(path):
        for pic_name in files:
                print(u"处理: %s" % pic_name)
                try:
                    with Image.open(path + pic_name) as img:
                        img = img.resize((each_size, each_size))
                        image.paste(img, (x * each_size, y * each_size))
                        x += 1
                        if x == x_lines:
                            x = 0
                            y += 1
                except IOError:
                    print("头像读取失败")

    img = image.save(os.getcwd() + "/wechat.png")
    print('微信好友头像拼接完成!')


if __name__ == '__main__':
    avatar_dir = creat_filepath()
    save_avatar(avatar_dir)
    joint_avatar(avatar_dir)
