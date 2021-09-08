from random import random

import lxml.etree
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.interpolate import interp2d
import numpy as np

from lib.constants import alphabet

KEYBOARD_BACKGROUND_JPG = '../data/keyboard.svg.jpg'
KEYBOARD_BACKGROUND_SVG = '../data/keyboard.svg'


# 创建一个半透明 colormap 并注册到 plt
def register_coolwarm_alpha_colormap(alpha: float) -> str:
    ncolors = 256
    color_array = plt.get_cmap('coolwarm')(range(ncolors))
    color_array[:,-1] = alpha
    map_object = LinearSegmentedColormap.from_list(name='coolwarm_alpha',colors=color_array)
    plt.register_cmap(cmap=map_object)
    return 'coolwarm_alpha'


register_coolwarm_alpha_colormap(0.5)


# 根据 xyz 坐标的散点图绘制热力图
def draw_heatmap_scatter(x: list, y: list, z: list):
    img = plt.imread(KEYBOARD_BACKGROUND_JPG)
    height, width = img.shape[0], img.shape[1]
    plt.imshow(img)

    ip = interp2d(x, y, z, kind='cubic')
    x1 = np.arange(0, width)
    y1 = np.arange(0, height)
    z2 = ip(x1, y1)

    plt.pcolormesh(x1, y1, z2, cmap='coolwarm_alpha')
    plt.scatter(x, y)
    plt.show()


# 获取字母的坐标
def get_alpha_position() -> dict:
    # doc = lxml.etree.parse(KEYBOARD_BACKGROUND_SVG)
    # for i in doc.getiterator():
    #     print(i)
    d = {}
    for i in alphabet:
        d[i] = [random()*1200, random()*300]
    return d


# 根据字母频度绘制热力图
def draw_heatmap(alpha_count: dict):
    alpha_position = get_alpha_position()
    x, y, z = [], [], []
    for alpha in alphabet:
        x.append(alpha_position[alpha][0])
        y.append(alpha_position[alpha][1])
        z.append(alpha_count[alpha])
    draw_heatmap_scatter(x, y, z)


if __name__ == '__main__':
    # n = 26
    # x, y, z = [163], [277], [100]
    # for i in range(n):
    #     x.append(random()*1200)
    #     y.append(random()*350)
    #     z.append(0)

    # x = [0, 100, 200, 0, 100, 200]
    # y = [0, 0, 0, 300, 300, 300]
    # z = [1, 2, 3, 4, 5, 6]

    # draw_heatmap_scatter(x, y, z)

    d = {}
    for i in range(len(alphabet)):
        d[alphabet[i]] = i
    draw_heatmap(d)

