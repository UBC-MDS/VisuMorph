from visumorph.change_hue import change_hue
import pytest
from visumorph import Image as VImage
from visumorph import load_image
import numpy as np

TEST_IMAGE_PATH = "tests/img/raw/meme.jpg"


def test_change_hue_returns_Image_on_valid_input():
    sample_image = load_image(TEST_IMAGE_PATH)
    result = change_hue(sample_image)
    assert isinstance(result, VImage), "Result should be a VImage object"


def test_change_hue_raises_error_on_string_in_delta_hue():
    sample_image = load_image(TEST_IMAGE_PATH)
    with pytest.raises(ValueError):
        change_hue(sample_image, delta_hue="not a number")


def test_change_hue_raises_type_error_on_invalid_input():
    with pytest.raises(TypeError):
        change_hue(np.array([1, 2, 3]))


def test_change_hue_uses_default_values_correctly():
    sample_image = load_image(TEST_IMAGE_PATH)
    result = change_hue(sample_image)
    assert (
        result.image[(1, 1, 1)] == (np.ones((414, 552, 3)) * 255)[(1, 1, 1)]
    ), "Default values are not working"


def test_change_hue_applies_specified_color_correctly():
    sample_image = load_image(TEST_IMAGE_PATH)
    result = change_hue(sample_image, color="black")
    assert (
        result.image[(1, 1, 1)] == (np.zeros((414, 552, 3)) * 255)[(1, 1, 1)]
    ), "Different colors are not working"
