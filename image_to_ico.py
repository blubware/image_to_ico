import os
from PIL import Image
from clear_screen import clear

options = r'''[1] Convert all files in directory'''

def nitrogen():
    try:
        clear()
        print(options)
        conversion_type = int(input('Conversion type: '))

        match conversion_type:
            case 1:
                path = 'ico'
                if not os.path.exists(path):
                    os.makedirs(path)

                files = os.listdir()
                image_extensions = ('.jpg', '.jpeg', '.png')
                image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]
                image_files.sort()

                if not image_files:
                    print('No image files found')
                
                else:
                    for image in image_files:

                        print('Converting image:', ''.join(image))
                        process_image = Image.open(image)
                        save_path = os.path.join(path, os.path.splitext(image)[0] + '.ico')
                        process_image.save(save_path)
                        print(f'Converted file: {image} to an ICO')     

        input('Press enter to return to main menu')
        nitrogen()
    except KeyboardInterrupt:
        nitrogen()

if __name__ == '__main__':
    nitrogen()