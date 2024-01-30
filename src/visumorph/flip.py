from visumorph import Image


def flip(image, v=0):
    """Flip image vertically or horizontally.

    Parameters
    ----------
    image : visumorph.Image
        Image to be flipped.
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
    >>> flip("exampleimage.jpg", v=1)
    """

    if not isinstance(image, Image):
        raise TypeError("The image is not a valid VisuMorph Image object")

    if v not in (0, 1):
        raise TypeError(
            "Invalid value for 'v'. Use 0 for horizontal flip or 1 for vertical flip."
        )

    flipped = image.image.copy()

    if v == 0:
        flipped = flipped[:, ::-1, :]
    else:
        flipped = flipped[::-1, :, :]

    return Image(flipped)
