from visumorph import Image as VImage
from PIL import Image as PImage
import numpy as np


def change_hue(image, color="white", delta_hue=1):
    """
    Change the hue of a VisuMorph Image object by blending it with a layer of specified color.

    Parameters
    ----------
    image : visumorph.Image
        A VisuMorph Image object whose hue is to be changed.
    color : str, optional
        The color used for the blending layer (default is "white").
    delta_hue : float or int, optional
        The degree of blending with the color layer. A value of 0 means no change,
        and 1 means complete replacement with the color layer (default is 1).

    Returns
    -------
    VImage : visumorph.Image
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
    >>> hue_changed = vm.change_hue(img)
    """

    if not isinstance(image, VImage):
        raise TypeError("The image is not a valid VisuMorph Image object")

    if not isinstance(delta_hue, (int, float)):
        raise ValueError("delta_hue must be a numeric value")

    # Convert the VisuMorph Image to a PIL Image for processing
    im = PImage.fromarray(image.image, mode="RGB")

    # Create a solid color layer for blending
    layer = PImage.new("RGB", im.size, color)

    # Blend the original image with the color layer
    adjusted_image = PImage.blend(im, layer, delta_hue)

    # Convert the adjusted PIL Image back to a NumPy array
    adjusted_image_np = np.array(adjusted_image)

    # Return a new VisuMorph Image object
    return VImage(adjusted_image_np)
