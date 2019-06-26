'''
This python script will take a csv file and a destination directory as inputs.
It will parse the .csv file and cropped each image into the destination folder (creating the folder if it does not exist)

Author: Daniel Chang

Usage: python crop-images.py --csv_input=LABELLED_IMAGE_CSV --image_dir=IMAGE_DIR --output_dir=DEST_DIR [--train_test_ratio=i]


'''
import sys
import os
import tensorflow as tf
from PIL import Image
import pandas as pd
from collections import defaultdict

flags = tf.app.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
flags.DEFINE_string('output_dir', '', 'Path to output')
flags.DEFINE_string('image_dir', '', 'Path to images')
flags.DEFINE_integer('train_test_ratio', 5,
                     'Number of training data per test data')
FLAGS = flags.FLAGS


def main():
    csv_path = FLAGS.csv_input
    scr_path = FLAGS.image_dir
    dest_path = FLAGS.output_dir
    train_test_ratio = FLAGS.train_test_ratio
    label_table = pd.read_csv(csv_path)
    # Since there can be multiple images in a file, we adopt a new image naming schema
    image_class_name = defaultdict(int)
    for _, row in label_table.iterrows():
        image = Image.open(os.path.join(scr_path, row['filename']))
        area = (row['xmin'], row['ymin'],
                row['xmax'], row['ymax'])
        image = image.crop(area)
        image_class_name[row['class']] += 1
        if(image_class_name[row['class']] % train_test_ratio == 0):
            test_path = os.path.join(dest_path, "Test-Data", row['class'])
            if(not os.path.exists(test_path)):
                os.makedirs(test_path)
            image.save(os.path.join(test_path, str(
                image_class_name[row['class']]) + '.jpg'))
        else:
            train_path = os.path.join(dest_path, "Training-Data", row['class'])
            if(not os.path.exists(train_path)):
                os.makedirs(train_path)
            image.save(os.path.join(train_path, str(
                image_class_name[row['class']]) + '.jpg'))

    print(f"Cropped all images found in {csv_path}.")


if __name__ == "__main__":
    main()
