import colorsys


def change_hue(image, delta_hue):
    """
    Adjusts the hue of a VisuMorph image.

    This function changes the hue of each pixel in the input VisuMorph image by a specified amount (delta_hue),
    altering the overall color composition without affecting luminance or saturation.

    Parameters
    ----------
    image : visumorph.Image
        The image to be processed. Must be a valid VisuMorph Image Object.
        The image should be in a color format recognizable by VisuMorph (e.g., RGB).
    delta_hue : float
        The degree by which to shift the hue component in the HSL color space. The value can be
        either positive or negative, representing clockwise or counterclockwise rotation of the hue, respectively.

    Returns
    -------
    image
        The VisuMorph Image with adjusted hue.

    Raises
    ------
    ValueError
        If delta_hue is not a float.
    TypeError
        If the input image is not a valid VisuMorph Image Object.
    InvalidColorFormatError
        If the input image is not in a color format recognized by VisuMorph.

    Examples
    --------
    >>> import visumorph
    >>> from visumorph.change_hue import change_hue
    >>> img = visumorph.load_image("example.jpg")
    >>> hue_changed_img = change_hue(img, 45.0)

    Notes
    -----
    The hue change wraps around the color wheel, meaning a delta_hue of 360 or -360 results in no change.
    """

    if not isinstance(image, Image):
        raise TypeError("Input must be a VisuMorph Image Object.")

    if not isinstance(delta_hue, float):
        raise ValueError("delta_hue must be a float.")

    try:
        rgb_image = image.image
    except AttributeError:
        raise InvalidColorFormatError("Image is not in a valid color format.")

    # Convert RGB to HSL, change hue, and convert back to RGB
    hsl_image = [[colorsys.rgb_to_hls(*pixel / 255.0)
                  for pixel in row] for row in rgb_image]
    adjusted_hsl_image = np.array(
        [[(h + delta_hue / 360.0) % 1.0, s, l] for h, l, s in row] for row in hsl_image)
    adjusted_rgb_image = np.array([[int(value * 255) for value in colorsys.hls_to_rgb(*pixel)]
                                  for pixel in row] for row in adjusted_hsl_image)

    return Image(adjusted_rgb_image)
