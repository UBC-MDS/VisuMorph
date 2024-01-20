from visumorph.change_hue import change_hue
import pytest
from visumorph import Image as VImage
from visumorph import load_image
import numpy as np
from PIL import Image as PImage


TEST_IMAGE_PATH = "tests/img/raw/meme.jpg"

def test_valid_input():
    sample_image = load_image(TEST_IMAGE_PATH)
    result = change_hue(sample_image)
    assert isinstance(result, VImage), "Result should be a VImage object"

def test_type_error():
    with pytest.raises(TypeError):
        change_hue(np.array([1, 2, 3]))

def test_default_parameters():
    sample_image = load_image(TEST_IMAGE_PATH)
    result = change_hue(sample_image)
    assert result.image[(1,1,1)] == (np.ones((414,552,3)) * 255)[(1,1,1)], "Default values are not working"

def test_different_color():
    sample_image = load_image(TEST_IMAGE_PATH)
    result = change_hue(sample_image, color="black")
    assert result.image[(1,1,1)] == (np.zeros((414,552,3)) * 255)[(1,1,1)], "Different colors are not working"

