import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp2d, griddata, RBFInterpolator

from lib.spelling_type import alphabet

KEYBOARD_BACKGROUND = '../data/keyboard.png'
# 采集到的 A - Z 的按键坐标
KEYBOARD_KEY_POSITIONS = [
    (207, 371), (600, 454), (428, 453), (381, 373), (362, 274),
    (468, 365), (550, 363), (642, 368), (774, 287), (728, 368),
    (813, 368), (903, 366), (776, 452), (686, 446), (878, 283),
    (966, 279), (182, 281), (445, 284), (302, 366), (524, 280),
    (708, 276), (508, 446), (274, 283), (335, 450), (623, 289),
    (259, 451)
]
ALPHA_POSITIONS = {alphabet[i]: KEYBOARD_KEY_POSITIONS[i] for i in range(len(alphabet))}
# 边界坐标
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


# 根据 xyz 坐标的散点图绘制热力图
def draw_heatmap_by_scatter(x: list, y: list, z: list):
    # 读图片的长宽
    img = plt.imread(KEYBOARD_BACKGROUND)
    height, width = img.shape[0:2]
    x = np.asarray(x)
    y = np.asarray(y)
    z = np.asarray(z)
    x1 = np.arange(100, 1050)
    y1 = np.arange(200, 500)
    x2, y2 = np.meshgrid(x1, y1)

    # 三种插值库
    def interpolate_interp2d():
        ip = interp2d(x, y, z, kind='linear')
        z2 = ip(x1, y1)
        return z2

    def interpolate_griddata():
        z2 = griddata((x, y), z, (x2, y2), method='linear')
        return z2

    def interpolate_rbf():
        xy = np.stack([x.ravel(), y.ravel()], -1)  # shape (N, 2) in 2d
        x2y2 = np.stack([x2.ravel(), y2.ravel()], -1)  # shape (N, 2) in 2d
        ip = RBFInterpolator(xy, z.ravel(), smoothing=0, kernel='cubic')  # explicit default smoothing=0 for interpolation
        z2 = ip(x2y2).reshape(x2.shape)  # not really a function, but a callable class instance
        return z2

    z2 = interpolate_rbf()

    # 绘制热力图
    def draw_heatmap():
        fig = plt.figure(dpi=300)
        ax = plt.axes()
        ax.imshow(img)
        im = ax.pcolormesh(x2, y2, z2, cmap='coolwarm', alpha=0.5)
        # im = ax.contourf(x2, y2, z2, np.arange(0, 3000, 100),cmap='coolwarm', alpha=0.5, vmax=3000, vmin=0)
        # ax.scatter(x[0:26], y[0:26])  # 绘制散点
        fig.colorbar(im, orientation='vertical')
        plt.show()

    # 也可以绘制 3d 图
    def draw_3d():
        fig = plt.figure(dpi=1000)
        ax = plt.axes(projection='3d')
        ax.plot_surface(x2, y2, z2, cmap='rainbow', vmax=2600, vmin=0)
        # ax.contour(X,Y,Z, zdim='z',offset=-2，cmap='rainbow)
        plt.show()

    draw_heatmap()


# 根据字母频度绘制热力图
def draw_heatmap_by_key_number_dict(key_number_dict: dict):
    x, y, z = [], [], []
    for alpha in alphabet:
        x.append(ALPHA_POSITIONS[alpha][0])
        y.append(ALPHA_POSITIONS[alpha][1])
        z.append(key_number_dict[alpha])
    for i in range(len(KEYBOARD_BOUNDARY_POSITIONS)):
        x.append(KEYBOARD_BOUNDARY_POSITIONS[i][0])
        y.append(KEYBOARD_BOUNDARY_POSITIONS[i][1])
        z.append(0)
    draw_heatmap_by_scatter(x, y, z)


if __name__ == '__main__':
    # 测试数据：{a: 100, b: 200, ... z: 2600}
    key_number_dict = {alphabet[i]: (i + 1) * 100 for i in range(len(alphabet))}
    draw_heatmap_by_key_number_dict(key_number_dict)
