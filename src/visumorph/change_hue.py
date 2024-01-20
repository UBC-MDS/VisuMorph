from visumorph import Image as VImage
from visumorph import load_image
import numpy as np
from PIL import Image as PImage


def change_hue(image, color="white", delta_hue=0.5):

    if type(image) != VImage:
        raise TypeError("The image is not a valid VisuMorph Image object")
    
    im = PImage.fromarray(image)
    layer = PImage.new("RGB", im.size, color)
    adjusted_image = PImage.blend(im, layer, delta_hue)
    adjusted_image_np = np.array(adjusted_image)


    return VImage(adjusted_image_np)

my_image = load_image('tests/img/raw/meme.jpg')
changed_img = change_hue(my_image)
to_show = PImage.fromarray(changed_img)
to_show.save("tests/img/results/new_adjusted.png", "PNG")