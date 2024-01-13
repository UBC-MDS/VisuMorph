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
    >>> import visumorph
    >>> from visumorph.rotate import rotate
    >>> img = visumorph.load_image("test.jpg")
    >>> rotated_45_img = rotate(img, 45.0)
    """
    pass
