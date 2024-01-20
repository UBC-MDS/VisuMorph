def scale(image, scale):
    """Enlarge/Shrink an image with a given scale.

    This function will scale a VisuMorph image by a given scale with 1.0 as
    the original scale. The final transformed image would have a dimension of
    (scale * original_width, scale * original_height), rounded to the nearest
    integer.

    Parameters
    ----------
    image : visumorph.Image
        The original image to be scaled.
    scale : float
        The desired scale. The original scale of the image is 1.0.
        A scale larger than 1.0 will result in a final image having a larger
        dimension, and vice versa.

    Returns
    -------
    visumorph.Image
        The VisuMorph Image scaled.

    Raises
    ------
    TypeError
        If the image is not a valid VisuMorph Image and/or scale given is
        not a number.

    Examples
    --------
    >>> import visumorph
    >>> from visumorph.scale import scale
    >>> img = visumorph.load_image("test.jpg")
    >>> scaled_img = scale(img, 1.15)
    """
    if not isinstance(image, visumorph.Image):
        raise TypeError("Input 'image' must be a valid VisuMorph Image.")
    if not isinstance(scale, (int, float)):
        raise TypeError("Input 'scale' must be a number.")

    # Calculate new dimensions
    new_width = round(image.width * scale)
    new_height = round(image.height * scale)

    # Scale the image
    scaled_image = image.resize((new_width, new_height))

    return scaled_image
