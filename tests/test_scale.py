import numpy as np
import visumorph as vm
import pytest
from PIL import Image


def test_scale_can_produce_a_larger_image():
    img = vm.load_image("tests/img/raw/meme.jpg")
    original_size = np.array(img.get_dimensions()[:2])
    resized = vm.scale(img, 2.0)
    new_size = resized.get_dimensions()[:2]
    assert np.array_equal(
        new_size, original_size * 2
    ), "The scaled image does not have the expected dimensions!"


def test_scale_can_produce_a_smaller_image():
    img = vm.load_image("tests/img/raw/meme.jpg")
    original_size = np.array(img.get_dimensions()[:2])
    resized = vm.scale(img, 0.01)
    new_size = resized.get_dimensions()[:2]
    assert np.array_equal(
        new_size, np.ceil(original_size * 0.01)
    ), "The scaled image does not have the expected dimensions!"


def test_zero_scale_should_return_error():
    img = vm.load_image("tests/img/raw/meme.jpg")
    with pytest.raises(ValueError):
        vm.scale(img, 0)


def test_negative_scale_should_return_error():
    img = vm.load_image("tests/img/raw/meme.jpg")
    with pytest.raises(ValueError):
        vm.scale(img, -1.0)


def test_pillow_image_should_return_error():
    img = Image.open("tests/img/raw/meme.jpg")
    with pytest.raises(TypeError):
        vm.scale(img, 1.0)


def test_image_as_scale_should_return_error():
    img = vm.load_image("tests/img/raw/meme.jpg")
    with pytest.raises(TypeError):
        vm.scale(img, img)


def test_string_as_scale_should_return_error():
    img = vm.load_image("tests/img/raw/meme.jpg")
    with pytest.raises(TypeError):
        vm.scale(img, "1.0")
