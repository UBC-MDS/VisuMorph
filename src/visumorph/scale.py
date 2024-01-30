import numpy as np
from visumorph import Image
from PIL import Image as PImage


def scale(image, scale):
    """Enlarge/Shrink an image with a given scale.

    This function will scale a VisuMorph image by a given scale with 1.0 as
    the original scale. The final transformed image would have a dimension of
    (scale * original_width, scale * original_height), rounded top to the
    nearest integer.

    Parameters
    ----------
    image : visumorph.Image
        The original image to be scaled.
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
    >>> scaled_img = vm.scale(img, 1.15)
    """

    if not isinstance(image, Image):
        raise TypeError("The provided image must be a valid VisuMorph Image object.")

    if not type(scale) in (float, int):
        raise TypeError("The scale provided must be a number.")

    if scale <= 0:
        raise ValueError("The scale provided must be a positive, non-zero number.")

    img = PImage.fromarray(image.image)
    new_h, new_w = np.ceil(np.array(image.get_dimensions()[:2]) * scale).astype(int)
    resized = img.resize((new_w, new_h))

    return Image(np.array(resized))
