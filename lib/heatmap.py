from random import random

import lxml.etree
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.interpolate import interp2d
import numpy as np

from lib.constants import alphabet

KEYBOARD_BACKGROUND = '../data/keyboard2.png'
KEYBOARD_KEY_POSITIONS = [
    (207, 371), (600, 454), (428, 453), (381, 373), (362, 274),
    (468, 365), (550, 363), (642, 368), (774, 287), (728, 368),
    (813, 368), (903, 366), (776, 452), (686, 446), (878, 283),
    (966, 279), (182, 281), (445, 284), (302, 366), (524, 280),
    (708, 276), (508, 446), (274, 283), (335, 450), (623, 289),
    (259, 451)
]
ALPHA_POSITION = {}
for i in range(len(alphabet)):
    ALPHA_POSITION[alphabet[i]] = KEYBOARD_KEY_POSITIONS[i]


# 创建一个半透明 colormap 并注册到 plt
def register_coolwarm_alpha_colormap(alpha: float) -> str:
    ncolors = 256
    color_array = plt.get_cmap('coolwarm')(range(ncolors))
    color_array[:, -1] = alpha
    map_object = LinearSegmentedColormap.from_list(name='coolwarm_alpha', colors=color_array)
    plt.register_cmap(cmap=map_object)
    return 'coolwarm_alpha'


register_coolwarm_alpha_colormap(0.5)


# 根据 xyz 坐标的散点图绘制热力图
def draw_heatmap_scatter(x: list, y: list, z: list):
    # 读图片的长宽
    img = plt.imread(KEYBOARD_BACKGROUND)
    height, width = img.shape[0:2]

    ip = interp2d(x, y, z, kind='cubic')
    x1 = np.arange(0, width)
    y1 = np.arange(0, height)
    z2 = ip(x1, y1)
    x2, y2 = np.meshgrid(x1, y1)
    fig, ax = plt.subplots()
    ax.imshow(img)
    im = ax.pcolormesh(x2, y2, z2, cmap='coolwarm_alpha')
    ax.scatter(x, y)
    fig.colorbar(im, orientation='vertical')
    plt.show()
    print(1)


# 根据字母频度绘制热力图
def draw_heatmap(alpha_count: dict):
    x, y, z = [], [], []
    for alpha in alphabet:
        x.append(ALPHA_POSITION[alpha][0])
        y.append(ALPHA_POSITION[alpha][1])
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
        d[alphabet[i]] = (i+1)*100
    draw_heatmap(d)
