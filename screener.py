from clickListener import ClickListener
from PIL import Image
from PIL import ImageChops
import os

def are_images_identical(img_path1, img_path2):
    img1 = Image.open(img_path1)
    img2 = Image.open(img_path2)
    diff = ImageChops.difference(img1, img2)
    return diff.getbbox() == None

class Screener():
    def  __init__(self, folder_img_left, folder_img_substats) -> None:
        self.clickListener = ClickListener()
        self.index = 0
        self.folder_img_left = folder_img_left
        self.folder_img_substats = folder_img_substats
        
    def delete_screenshot_if_redonant(self):
        if self.index >= 1:
            if are_images_identical(f'{self.folder_img_left}/{self.index}.png', f'{self.folder_img_left}/{self.index-1}.png') or \
               are_images_identical(f'{self.folder_img_substats}/{self.index}.png', f'{self.folder_img_substats}/{self.index-1}.png'):
                os.remove(f'{self.folder_img_left}/{self.index}.png')
                os.remove(f'{self.folder_img_substats}/{self.index}.png')
                print("redondant screenshot. DELETED")
            else:
                self.index += 1
        else:
            self.index += 1
    
    def run_calibration_substats(self):
        self.clickListener.register_subspace_substats()
        
    def run_calibration_left(self):
        self.clickListener.register_subspace_left()

    def screenshot(self, filename="test.png"):
        print('Left screnshot')
        self.clickListener.take_screenshot_left(f"{self.folder_img_left}/{filename}")
        print('substats screenshot')
        self.clickListener.take_screenshot_substats(f"{self.folder_img_substats}/{filename}")