from PIL import Image as PImage
import visumorph as vm
import numpy as np
from functools import partial


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
        return f"VisuMorph Image, dimensions: {self.get_dimensions()}"

    def __self_inject(self, func):
        """Wrapper method to self-inject into visumorph functions."""
        return partial(func, self)

    def flip(self, *args, **kwargs):
        """Flip image vertically or horizontally.

        Parameters
        ----------
        v : int, optional
            Flip vertically if v=1, horizontally if v=0. By default, v=0.

        Returns
        -------
        image
            Flipped VisuMorph image.

        Raises
        ------
        TypeError
            If the image is not a valid VisuMorph Image and/or v is not 0 or 1.

        Examples
        --------
        >>> import visumorph
        >>> from visumorph.flip import flip
        >>> img = visumorph.load_image("exampleimage.jpg")
        >>> img.flip(v=1)
        """
        return self.__self_inject(vm.flip)(*args, **kwargs)

    def rotate(self, *args, **kwargs):
        """Rotate an image with a given rotation.

        This method will rotate a VisuMorph image by a given degree of rotation.
        A background image can be specified for filling any empty spaces which
        are not covered by the image after rotation.

        Parameters
        ----------
        rotation : float
            The desired rotation angle in degrees.
            +ve means clockwise while -ve means counter-clockwise.
        background : visumorph.Image, optional
            The background image to be filled in where the rotated image is not
            covered. Default is None, which a black background image would be used.

        Returns
        -------
        image
            The VisuMorph Image after rotation.

        Raises
        ------
        TypeError
            If the image is not a valid VisuMorph Image and/or rotation given is
            not a number.

        Examples
        --------
        >>> import visumorph as vm
        >>> img = vm.load_image("test.jpg")
        >>> rotated_45_img = img.rotate(img, 45.0)
        """
        return self.__self_inject(vm.rotate)(*args, **kwargs)

    def scale(self, *args, **kwargs):
        """Enlarge/Shrink an image with a given scale.

        This method will scale a VisuMorph image by a given scale with 1.0 as
        the original scale. The final transformed image would have a dimension of
        (scale * original_width, scale * original_height), rounded top to the
        nearest integer.

        Parameters
        ----------
        scale : float or int
            The desired scale. The original scale of the image is 1.0.
            A scale larger than 1.0 will result in a final image having a larger
            dimension, and vice versa. Cannot be equal or smaller than 0.0.

        Returns
        -------
        image
            The VisuMorph Image scaled.

        Raises
        ------
        TypeError
            If the image is not a valid VisuMorph Image and/or scale given is
            not a number.
        ValueError
            If the scale provided is equal 0 or is a negative number.

        Examples
        --------
        >>> import visumorph as vm
        >>> img = vm.load_image("test.jpg")
        >>> scaled_img = img.scale(img, 1.15)
        """
        return self.__self_inject(vm.scale)(*args, **kwargs)

    def change_hue(self, *args, **kwargs):
        """Change the hue of a VisuMorph Image object by blending it with a layer of specified color.

        Parameters
        ----------
        color : str, optional
            The color used for the blending layer (default is "white").
        delta_hue : float or int, optional
            The degree of blending with the color layer. A value of 0 means no change,
            and 1 means complete replacement with the color layer (default is 1).

        Returns
        -------
        Image : visumorph.Image
            A new VisuMorph Image object with the modified hue.

        Raises
        ------
        TypeError
            If the input is not a valid VisuMorph Image object.
        ValueError
            If 'delta_hue' is not a number.

        Examples
        --------
        >>> import visumorph as vm
        >>> img = vm.load_image("test.jpg")
        >>> hue_changed = img.change_hue(img)
        """
        return self.__self_inject(vm.change_hue)(*args, **kwargs)


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
