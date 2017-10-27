import sys

import os

sys.path.append(os.path.realpath('..'))

from conf.image_conf import image_width
from conf.image_conf import image_height

num_epoch = 500
input_shape = (image_height, image_width, 3)
batch_size = 32
patience = 10
output_dir = '../output'
model_h5_name = 'model.h5'
model_plot_name = 'model.png'
test_data_dir = '../data/test'
test_data_size = 10
