from visumorph import Image

import numpy as np
from PIL import Image as PImage


def rotate(image, rotation, background=None):
    """Rotate an image with a given rotation.

    This function will rotate a VisuMorph image by a given degree of rotation.
    A background image can be specified for filling any empty spaces which
    are not covered by the image after rotation.

    Parameters
    ----------
    image : visumorph.Image
        The original image to be rotated.
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
    >>> rotated_45_img = vm.rotate(img, 45.0)
    """

    if not isinstance(image, Image):
        raise TypeError("The image is not a valid VisuMorph Image object")

    if background is not None and not isinstance(background, Image):
        raise TypeError("The background image is not a valid VisuMorph Image object")

    if not type(rotation) in (float, int):
        raise TypeError("The rotation degree must be a float or an integer")

    # minimum size of the pre-rotation image to cover
    min_len = np.ceil(np.hypot(*image.image.shape[0:2])).astype(int)

    min_dim_rgb = (min_len, min_len, 3)

    if background is None:
        bg_arr = np.zeros(min_dim_rgb)
    else:
        # calculate the number of times the bg image to be repeated (tiled)
        num_tiles = np.max(np.ceil(min_len / background.image.shape[0:2])).astype(int)
        # tile it!
        bg_arr = np.tile(background.image, (num_tiles, num_tiles, 1))
        # crop it back to min_dim_rgb
        bg_arr = bg_arr[:min_len, :min_len]

    bg_img = PImage.fromarray(bg_arr.astype(np.uint8), mode="RGB")

    # putting the image at the center of the prepared background image
    x_start = (min_len - image.image.shape[1]) // 2
    y_start = (min_len - image.image.shape[0]) // 2
    bg_img.paste(PImage.fromarray(image.image, mode="RGB"), box=(x_start, y_start))

    rotated = np.array(bg_img.rotate(-rotation))

    # crop image back to its original size
    rotated = rotated[
        y_start : y_start + image.image.shape[0],
        x_start : x_start + image.image.shape[1],
    ]

    return Image(rotated)
