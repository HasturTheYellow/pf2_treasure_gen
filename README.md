
# Pathfinder 2nd NPC Generator using Paizo's Deck of Endless NPC images

### Description
This simple script takes random images from the faces and attributes images folder and create a full image of npc.
You will need the digital version of the [Deck of Endless NPC from Paizo](https://paizo.com/products/btq02d82)


### Requirements
Tested with [Python 3.7](https://www.python.org/downloads/)

The script needs the Pillow package.
With pip:
```
pip install Pillow
```
With conda:
```
conda install Pillow
```

### SETUP

You need to change the value of data_root variable in the code to your own path to the root of the images
```
data_root = r'F:\PATH\TO\IMAGES\ROOT'
```

You have to put all the face images in the folder 'Faces'  
You have to put all the attributes images in a folder 'Attributes'  
You need to create an output folder 'NPC'  

The result should be like this:

face images in F:\PATH\TO\IMAGES\ROOT\Faces  
attributes images in F:\PATH\TO\IMAGES\ROOT\Attributes  
output images will go in F:\PATH\TO\IMAGES\ROOT\NPC  

You can change the name of these folders in the script if you want

### USAGE
Just open a command window and change folder to where the script is and type
```
python npc_generator.py
```

A new image formated as this npc_YYYYMMDD_HHMMSS.jpg will be created.

## Authors
* Akarius

## Changelog 
| Author         | Date          | Version | What                                       |
| -------------  |:------------- |:--------|:-------------------------------------------|
| Akarius        | 2022-09-08    |  0.1.0  | Initial version                            |


