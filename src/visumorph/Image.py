from PIL import Image as PImage
import numpy as np


class Image:
    """The main class for VisuMorph Image objects."""

    def __init__(self, image):
        self.image = image

    def get_dimensions(self):
        return self.image.shape

    def save(self, file_path):
        """Saves the image to a file.

        Parameters
        ----------
        file_path : str
            The path where the image should be saved.
        """
        # Convert the image data to a Pillow Image and save it to the specified path
        pil_image = PImage.fromarray(self.image)
        pil_image.save(file_path)

    def __repr__(self):
        return f"VisuMorph Image, dimensions: {self.dimensions}"


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
