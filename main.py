import os
from PIL import Image

def processDirectory(path):
    fileStructure = {}
    for filename in os.listdir(path):
        name, extension = os.path.splitext(filename)
        if name in fileStructure:
            alpha = 255
            fileStructure[name].append(extension)

            if '.cr2' in fileStructure[name]:
                processRaw(path+name+'.cr2')

            if '.png' in fileStructure[name]:
                alpha = getAlphaChannelFromPixel(path+name+'.png')
            elif '.tif' in fileStructure[name]:
                alpha = getAlphaChannelFromPixel(path+name+'.tif')
        else:
            fileStructure[name] = [extension]

    return fileStructure

def processRaw(file):
    print('process raw '+file)

def getAlphaChannelFromPixel(file):
    img = Image.open(file, 'r')
    if img.mode == 'RGBA':
        red, green, blue, alpha = img.split()
        return alpha
    else:
        # TODO: How to handle images without no alpha channel?
        return 255

if __name__ == '__main__':
    files = processDirectory('c:\\temp\\workflow\\in\\')
    print(files)
