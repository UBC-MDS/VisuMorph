def change_hue(image, delta_hue):
    """Adjusts the hue of the given image.

    This function modifies the hue of each pixel in the input image by the specified amount (delta_hue),
    changing the overall color composition without altering luminance or saturation.

    Parameters
    ----------
    image (Image Object): The image to be processed. Must be a valid Image Object as defined in the VisuMorph package.
                          The image should be in a color format recognizable by VisuMorph (e.g., RGB).
    delta_hue (float): The amount by which to shift the hue component in the HSL color space. The value can be either
                       positive or negative, representing a clockwise or counterclockwise rotation of the hue, respectively.

    Returns
    -------
    Image Object: A new Image Object with the hue adjusted as per the delta_hue parameter. The returned image has the same
                  dimensions and format as the input image.

    Raises:
    ValueError: If delta_hue is not a float.
    TypeError: If the input image is not a valid Image Object.
    InvalidColorFormatError: If the input image is not in a color format recognized by the VisuMorph package.

    Example:
    >>> from VisuMorph import change_hue, load_image
    >>> original_image = load_image('path/to/image.jpg')
    >>> modified_image = change_hue(original_image, 45.0)
    >>> modified_image.save('path/to/modified_image.jpg')

    Note:
    The hue change wraps around the color wheel, meaning a delta_hue of 360 or -360 results in no change.
    """
    pass
