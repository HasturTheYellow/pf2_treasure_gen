
# Pathfinder 2nd Treasure Generator using Paizo's Deck of Endless Treasure images

### Description
This simple script takes random images from the faces and attributes images folder and create a full image of a treasure.
You will need the digital version of the [Deck of Endless Treasure from Paizo](https://paizo.com/products/btq0bszz?Pathfinder-Deck-of-Endless-Treasure)
If the images are not 744x1039, you will need to either change it to this format or change the vars in the script.

This is a Fork of the Random NPC Generator, using Paizo's Deck of Endless NPCs, from Akarius. Variables have been edited, all other work is theirs.


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
You need to create an output folder 'Treasure'  

The result should be like this:

face images in F:\PATH\TO\IMAGES\ROOT\Faces  
attributes images in F:\PATH\TO\IMAGES\ROOT\Attributes  
output images will go in F:\PATH\TO\IMAGES\ROOT\Treasure  

You can change the name of these folders in the script if you want

### USAGE
Just open a command window and change folder to where the script is and type
```
python Treasure_generator.py
```

A new image formated as this Treasure_YYYYMMDD_HHMMSS.jpg will be created.  
[Example of random output](https://imgur.com/5nWAMfI)

With the base script, you can add a few things, including:
* Loop to create a high numbers of Treasure at once.
* Add img.show() at the end to see the image immediately
* Add a boolean to save the file or not (with img.show())

## Authors
* Akarius
* HasturtheYellow - Fork and Variable Edits only

## Changelog 
| Author         | Date          | Version | What                                       |
| -------------  |:------------- |:--------|:-------------------------------------------|
| Akarius        | 2022-09-08    |  0.1.0  | Initial version                            |
| HasturtheYellow| 2025-07-02    |  0.1.1  | Forked version                             |

