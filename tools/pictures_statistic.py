from scipy.stats import gaussian_kde
import os
import numpy as np
import pandas as pd
import cv2
from tqdm import tqdm
from PIL import Image
import pandas as pd

def pic_info(pic_file_path, pic_type, out_path):
    os.chdir(pic_file_path)
    os.listdir()

    df = pd.DataFrame()
    for fruit in tqdm(os.listdir()):  # 遍历每个类别
        os.chdir(fruit)
        for file in os.listdir():  # 遍历每张图像
            try:
                img = cv2.imread(file)
                df = df.append({'类别': fruit, '文件名': file, '图像宽': img.shape[1], '图像高': img.shape[0]}, ignore_index=True)
            except:
                print(os.path.join(fruit, file), '读取错误')
        os.chdir('../')
    os.chdir('../')

    file_list = []
    width_list = []
    height_list = []

    for dirpath, dirnames, files in os.walk(pic_file_path):
        for file in files:
            file_path = os.path.join(dirpath, file)
            for suf in pic_type:
                if file.endswith(suf):
                    img = Image.open(file_path)
                    file_list.append(file)
                    width_list.append(img.size[0])
                    height_list.append(img.size[1])

    content_dict = {
        'dir_name': file_list,
        'width': width_list,
        'height': height_list
    }

    df = pd.DataFrame(content_dict)
    csv_path = os.path.join(out_path, 'image_size.csv')
    df.to_csv(csv_path, encoding='utf_8_sig')




def pic_info_plot(csv_file, size, font_size, out_path, type ):
    df = pd.read_csv(csv_file)

    x = df['width']
    y = df['height']
    xy = np.vstack([x,y])
    z = gaussian_kde(xy)(xy)

    # Sort the points by density, so that the densest points are plotted last
    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]

    plt.figure(figsize=size)
    plt.scatter(x, y, c=z,  s=50, cmap='Spectral_r')
    plt.colorbar()

    plt.tick_params(labelsize=15)

    xy_max = max(max(df['width']), max(df['height']))
    plt.xlim(xmin=0, xmax=xy_max)
    plt.ylim(ymin=0, ymax=xy_max)

    plt.ylabel('height', fontsize=font_size)
    plt.xlabel('width', fontsize=font_size)

    plt.savefig(out_path + type, dpi=DPI, bbox_inches='tight')
    plt.show()