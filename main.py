from queue import Full
from PIL import Image
from PIL import ImageFilter
import os


def main():
    # Here's given the path of the folder with images that you want to change
    startfolder = 'C:\\Users\\User\\Desktop\\pillow\\IMAGE'
    # Here's is the path to folder with changed images
    endfolder = 'C:\\Users\\User\\Desktop\\pillow\\INSTVERSION'

    # A loop, to create a list of all image names
    for imagePath in os.listdir(startfolder):
        # Full directory name of the image
        inputPath = os.path.join(startfolder, imagePath)

        img = Image.open(inputPath)

        # Path of the edited image
        fullOutPath = os.path.join(endfolder, 'inst_'+imagePath)
        img.save(fullOutPath, 'PNG')

        # Editing Magic
        watermark = Image.open('C:\\Users\\User\\Desktop\\pillow\\watermark.png')

        img = img.resize((1080, 1080)).convert('L')
        img.paste(watermark, (580, 720), watermark)
        img.save(fullOutPath)

        # Optional
        print(fullOutPath)


if __name__ == '__main__':
    main()
