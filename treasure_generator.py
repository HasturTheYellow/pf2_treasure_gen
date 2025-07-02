#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
"""
Project Generator from Deck of Endless Treasure
Description:
This script create a random treasure piece from the Deck of Endless Treasure cards in image format.
The image have to be separate in two seperate folders: faces and attributes
A third folder will have the saved treasure

This script uses Pillow

@author: Akarius - Original Script | Edited by HasturtheYellow
@version: 0.1.1
@filename: treasure_generator.py
@change:
2022-09-08 0.1.0 Creation
2025-07-02 Forked by HasturtheYellow

"""
# ---------------------------------------------------------------------------------------
# IMPORTS
# ---------------------------------------------------------------------------------------
import os
import random
from datetime import datetime
from PIL import Image

# ---------------------------------------------------------------------------------------
# VARIABLES
# ---------------------------------------------------------------------------------------
# x and y length of the faces and attributes cards
card_x = 744
card_y = 1039

# x and y length of the resulting card
out_x = 976
out_y = 1924

# path root
data_root = r'F:\REFERENCE\PRPG2\Pregenerated\Deck of Endless Treasure'
# folders
fldr_face = 'Faces'
fldr_attr = 'Attributes'
fldr_out = 'Treasure'

path_face = os.path.join(data_root, fldr_face)
path_attr = os.path.join(data_root, fldr_attr)
path_out = os.path.join(data_root, fldr_out)

# ---------------------------------------------------------------------------------------
# RUN
# ---------------------------------------------------------------------------------------
def run():
    print('Starting Treasure Generator script')
    print(f'Root is {data_root}')
    print(f'Faces folder: {path_face}')
    print(f'Atributes folder: {path_attr}')
    
    lst_faces = os.listdir(path_face)
    nb_faces = len(lst_faces)
    print(f'{nb_faces} images in Faces folder')

    lst_attr = os.listdir(path_attr)
    nb_attr = len(lst_attr)
    print(f'{nb_attr} images in Atributes folder')
    
    print('Chosing randomly face and attributes')
    path_rnd_face = os.path.join(path_face, random.choice(lst_faces))
    path_rnd_attr_left = os.path.join(path_attr, random.choice(lst_attr))
    path_rnd_attr_top = os.path.join(path_attr, random.choice(lst_attr))
    path_rnd_attr_bottom = os.path.join(path_attr, random.choice(lst_attr))
    
    print(f'Face: {path_rnd_face}')
    print(f'Left Attr: {path_rnd_attr_left}')
    print(f'Top Attr: {path_rnd_attr_top}')
    print(f'Bottom Attr: {path_rnd_attr_bottom}')
    
    print('Creating Treasure blank image')
    img = Image.new('RGB', (out_x, out_y), color=(255,255,255))
    print('Opening random images')
    img_face = Image.open(path_rnd_face) 
    img_attr_left = Image.open(path_rnd_attr_left) 
    img_attr_top = Image.open(path_rnd_attr_top) 
    img_attr_bottom = Image.open(path_rnd_attr_bottom) 
    
    img.paste(img_attr_left, (0, 143))
    img.paste(img_attr_top, (231, 0))
    img.paste(img_attr_bottom, (232, 604))
    img.paste(img_face, (232, 143))

    area = (245, 278, 719, 560)
    img_secret = img_attr_top.crop(area)
    
    img.paste(img_secret, (0, 1646))

    area_2 = (245, 278, 719, 560)
    img_secret_2 = img_attr_bottom.crop(area_2)
    
    img.paste(img_secret_2, (524, 1646))
    
    run_time = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    fname = f'treasure_{run_time}.jpg'
    
    out_name = os.path.join(path_out, fname)
    print(f'Writing {out_name}')
    img.save(out_name)
    print('Script ends')
    
if __name__ == "__main__":
    run()
