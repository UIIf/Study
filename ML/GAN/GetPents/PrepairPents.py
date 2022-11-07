import imageio.v2 as iio
import numpy as np

from os import listdir

import matplotlib.pyplot as plt

new_path = '/home/uiif/GitRepos/Study/ML/GAN/GetPents/Processed/'
picks_folder = "/home/uiif/GitRepos/Study/ML/GAN/GetPents/Pics/"
all_picks = listdir(picks_folder)

for pick in all_picks:
	img = iio.imread(picks_folder + pick)
	n = np.array(img)[:,:,0]
	np.save(new_path + pick[:-4] + ".npy",n)
# img = iio.imread("/home/uiif/GitRepos/Study/ML/GAN/GetPents/Pics/images0000263259.jpg")
# img2 = iio.imread("/home/uiif/GitRepos/Study/ML/GAN/GetPents/Pics/images0000767056.jpg")
# n = np.array(img)[:,:,0]