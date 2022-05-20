import imageio 
import glob
from pathlib import Path
from PIL import Image



def Reformat_Image(ImageFilePath):
    image = Image.open(ImageFilePath)
    image_size = image.size
    width = image_size[0]
    height = image_size[1]

    if(width != height):
        bigside = width if width > height else height

        background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

        background.paste(image, offset)
        final = background.resize((800,800))
        final.save(ImageFilePath,format='PNG', subsampling=0, quality=100)
        print("Image has been is squared and resized !")
    else:
        print("Image is already a square, it has not been resized !")


def v2_make_gif(args):

    images = list(glob.glob(f"./*.png"))
    [Reformat_Image(image) for image in images]
    print('Images have been reformated')
    image_list=[]
    total_duration = len(images)*150
    print(image_list)
    for file_name in images:
    	image_list.append(imageio.imread(file_name))
#    print(image_list) 
    imageio.mimwrite(args[0]+'.gif', image_list,duration=0.75)


if __name__ == "__main__":
         import sys
         v2_make_gif(sys.argv[1:])
