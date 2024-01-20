from visumorph.flip import flip
from visumorph.Image import load_image
import numpy as np
import pytest
import os


def test_flip_vertically_should_have_top_row_identical():
    """Test that flipping an image vertically results in the top row being identical."""

    img = load_image('tests/img/raw/meme.jpg')

    flipped_img = flip(img, v=1)

    assert flipped_img.get_dimensions() == img.get_dimensions()
    assert np.array_equal(flipped_img.image[0, :], img.image[-1, :])


def test_flip_horizontally_should_have_leftmost_column_identical():
    """Test that flipping an image horizontally results in the leftmost column being identical."""

    img = load_image('tests/img/raw/meme.jpg')

    flipped_img = flip(img, v=0)

    assert flipped_img.get_dimensions() == img.get_dimensions()
    assert np.array_equal(flipped_img.image[:, 0], img.image[:, -1])


def test_flip_with_invalid_v_value_should_raise_error():
    """Test that flipping an image with an invalid 'v' value raises a TypeError."""

    img = load_image('tests/img/raw/meme.jpg')

    with pytest.raises(TypeError):
        flip(img, v=2)


def test_flip_with_non_image_input_should_raise_error():
    """Test that flipping a non-image input raises a TypeError."""

    with pytest.raises(TypeError):
        flip('not_an_image', v=1)