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
    >>> from visumorph.flipping import flip
    >>> img = visumorph.load_image("exampleimage.jpg")
    >>> flip("exampleimage.jpg", v=1)
    """
    pass