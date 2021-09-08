import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.interpolate import interp2d

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
KEYBOARD_BOUNDARY_POSITIONS = [
    (57, 201), (88, 201), (139, 203), (191, 203), (252, 203), (351, 212), (395, 206), (450, 207), (510, 206),
    (565, 204), (595, 204), (665, 202), (710, 200), (749, 200), (803, 201), (843, 206), (909, 204), (956, 199),
    (980, 196), (1005, 196), (1041, 228), (1046, 263), (1025, 307), (995, 352), (975, 379), (945, 435), (920, 468),
    (869, 464), (847, 459), (837, 505), (789, 545), (723, 555), (644, 555), (569, 555), (507, 555), (440, 542),
    (385, 534), (331, 537), (238, 537), (200, 539), (154, 538), (123, 491), (123, 473), (119, 442), (111, 396),
    (99, 367), (91, 311), (87, 279), (111, 264), (137, 354), (149, 406), (180, 487), (174, 455), (441, 512), (601, 521),
    (694, 516), (790, 512), (1028, 425), (973, 458), (924, 494), (895, 550), (951, 490), (1068, 300), (1072, 252),
    (1073, 190), (989, 170), (950, 169), (821, 188), (680, 185), (594, 180), (502, 179), (447, 179), (347, 179),
    (247, 179), (154, 176), (109, 185), (63, 179)
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
def draw_heatmap_by_scatter(x: list, y: list, z: list):
    # 读图片的长宽
    img = plt.imread(KEYBOARD_BACKGROUND)
    height, width = img.shape[0:2]

    ip = interp2d(x, y, z, kind='linear')
    x1 = np.arange(145, 1000)
    y1 = np.arange(250, 500)
    z2 = ip(x1, y1)
    x2, y2 = np.meshgrid(x1, y1)

    def draw_heatmap():
        fig, ax = plt.subplots()
        fig.set_dpi(1000)
        ax.imshow(img)
        im = ax.pcolormesh(x2, y2, z2, cmap='coolwarm_alpha', vmax=3000, vmin=0)
        ax.scatter(x[0:26], y[0:26])
        fig.colorbar(im, orientation='vertical')
        plt.show()

    def draw_3d():
        fig = plt.figure(dpi=1000)  # 定义新的三维坐标轴
        ax3 = plt.axes(projection='3d')

        # 作图
        ax3.plot_surface(x2, y2, z2, cmap='rainbow', vmax=2600, vmin=0)
        # ax3.contour(X,Y,Z, zdim='z',offset=-2，cmap='rainbow)   #等高线图，要设置offset，为Z的最小值
        plt.show()

    draw_heatmap()


# 根据字母频度绘制热力图
def draw_heatmap_by_alpha_count(alpha_count: dict):
    x, y, z = [], [], []
    for alpha in alphabet:
        x.append(ALPHA_POSITION[alpha][0])
        y.append(ALPHA_POSITION[alpha][1])
        z.append(alpha_count[alpha])
    # for i in range(len(KEYBOARD_BOUNDARY_POSITIONS)):
    #     x.append(KEYBOARD_BOUNDARY_POSITIONS[i][0])
    #     y.append(KEYBOARD_BOUNDARY_POSITIONS[i][1])
    #     z.append(0)
    draw_heatmap_by_scatter(x, y, z)


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
        d[alphabet[i]] = (i + 1) * 100
    draw_heatmap_by_alpha_count(d)
