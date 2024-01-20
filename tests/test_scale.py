from visumorph import scale, load_image
import numpy as np
import pytest


def test_scale_enlarge_image():
    img = load_image('tests/img/raw/meme.jpg')
    scaled_img = scale(img, 1.5)
    assert scaled_img.get_dimensions() == (int(img.width * 1.5), int(img.height * 1.5))


def test_scale_shrink_image():
    img = load_image('tests/img/raw/meme.jpg')
    scaled_img = scale(img, 0.8)
    assert scaled_img.get_dimensions() == (int(img.width * 0.8), int(img.height * 0.8))


def test_scale_with_invalid_image_type_should_raise_error():
    img = np.array([[255, 255, 255], [0, 0, 0]])
    with pytest.raises(TypeError):
        scale(img, 1.2)


def test_scale_with_invalid_scale_type_should_raise_error():
    img = load_image('tests/img/raw/meme.jpg')
    with pytest.raises(TypeError):
        scale(img, 'invalid_scale')
        
