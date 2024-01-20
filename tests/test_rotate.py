from visumorph import scale, load_image
import numpy as np
from PIL import Image as PImage
import pytest


def test_rotate_45_degrees_with_no_background():
    img = load_image('tests/img/raw/meme.jpg')
    rotated = rotate(img, 45)
    assert rotated.get_dimensions() == img.get_dimensions()
    # should have black pixel as background at all four corners
    assert np.array_equal(rotated.image[0, 0], np.array([0, 0, 0]))
    assert np.array_equal(rotated.image[-1, 0], np.array([0, 0, 0]))
    assert np.array_equal(rotated.image[0, -1], np.array([0, 0, 0]))
    assert np.array_equal(rotated.image[1, -1], np.array([0, 0, 0]))


def test_rotate_90_should_be_identical_to_neg_270():
    img = load_image('tests/img/raw/meme.jpg')
    r1 = rotate(img, 90)
    r2 = rotate(img, -270)
    assert np.array_equal(r1.image, r2.image)


def test_can_handle_float_rotations():
    img = load_image('tests/img/raw/meme.jpg')
    r1 = rotate(img, -120.5)
    r2 = rotate(img, 239.5)
    assert np.array_equal(r1.image, r2.image)


def test_can_handle_big_numbers():
    img = load_image('tests/img/raw/meme.jpg')
    r1 = rotate(img, 6046617600000.0)
    r2 = rotate(img, 0)
    assert np.array_equal(r1.image, r2.image)


def test_rotate_with_background_should_return_non_black_corner_pixels():
    img = load_image('tests/img/raw/meme.jpg')
    rotated = rotate(img, 20, background=img)
    assert rotated.get_dimensions() == img.get_dimensions()
    # should **not** have black pixel as background at all four corners
    assert not np.array_equal(rotated.image[0, 0], np.array([0, 0, 0]))
    assert not np.array_equal(rotated.image[-1, 0], np.array([0, 0, 0]))
    assert not np.array_equal(rotated.image[0, -1], np.array([0, 0, 0]))
    assert not np.array_equal(rotated.image[1, -1], np.array([0, 0, 0]))


def test_should_return_error_when_pillow_image_is_supplied():
    img = PImage.open('tests/img/raw/meme.jpg')
    with pytest.raises(TypeError):
        rotate(img, 1337)


def test_should_return_error_when_a_non_numeric_type_is_supplied():
    img = load_image('tests/img/raw/meme.jpg')
    with pytest.raises(TypeError):
        rotate(img, '25')


def test_should_return_error_when_background_is_not_an_image():
    img = load_image('tests/img/raw/meme.jpg')
    with pytest.raises(TypeError):
        rotate(img, 124, background=np.array([0, 0, 0]))

