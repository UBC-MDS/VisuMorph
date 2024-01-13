def flip(input_file, v=0):
    """Load image from an image file and return as an image numpy array.

    Parameters
    ----------
    input_file : str
        Path to image file.
    v : int, optional
        Flip vertically if v=1, horizontally if v=0. By default, v=0.

    Returns
    -------
    df
        Flipped image numpy array.

    Examples
    --------
    >>> flip("exampleimage.jpg", v=1)
    """