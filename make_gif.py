import glob

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
        final.save(ImageFilePath)
        print("Image has been is squared and resized !")

    else:
        print("Image is already a square, it has not been resized !")



def make_gif(args):
    [Reformat_Image(image) for image in glob.glob(f"./*.png")]
    print('Images have been reformated')
    frames = [Image.open(image) for image in glob.glob(f"./*.png")]
    frame_one = frames[0]
    total_duration = len(frames)*150
    frame_one.save(args[0]+'.gif', format="GIF", append_images=frames,
               save_all=True, duration=total_duration,disposal=2, loop=0)



if __name__ == "__main__":
    import sys
    make_gif(sys.argv[1:])  
