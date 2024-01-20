from visumorph import scale, load_image
import numpy as np
import pytest


def test_scale_with_invalid_scale_type_should_raise_error():
    img = load_image('tests/img/raw/meme.jpg')
    with pytest.raises(TypeError):
        scale(img, 'invalid_scale')
        
def test_scale_with_valid_image_should_not_raise_error():
    img = load_image("tests/img/raw/meme.jpg")
    try:
        scale(img, 1.5)
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")

def test_scale_with_large_scale_should_not_raise_error():
    img = load_image("tests/img/raw/meme.jpg")
    try:
        scale(img, 5.0)
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")
        
def test_scale_with_shrink_scale_should_not_raise_error():
    img = load_image("tests/img/raw/meme.jpg")
    try:
        scale(img, 0.5)
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")