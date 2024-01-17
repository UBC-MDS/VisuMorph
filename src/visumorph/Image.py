from PIL import Image as PImage
import numpy as np


class Image:
    """The main class for VisuMorph Image objects."""
    def __init__(self, image):
        self.image = image
        self.dimensions = self.image.shape


def load_image(image_path):
    """Load an image from filesystem and return an Image object.

    Parameters
    ----------
    image_path : str
        The path to the image file to be read.

    Returns
    -------
    image
        The VisuMorph Image object with image data loaded in.
    """
    img = PImage.open(image_path)
    arr = np.array(img)
    return Image(arr)
