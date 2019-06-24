''' 
Code adapted from https://github.com/datitran/raccoon_dataset/blob/master/xml_to_csv.py 
The following block of code is used to convert image annotation data from labelImg tool (https://github.com/tzutalin/labelImg) to a .csv format.
Usage: python xml_to_csv.py DIRECTORY_PATH
'''
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import sys


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height',
                   'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for image_path in sys.argv[1:]:
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(os.path.join(image_path, 'labels.csv'), index=None)
        print(f"Successfully converted the xml files found in {image_path} to csv.")


if __name__ == "__main__":
    main()
