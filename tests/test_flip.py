from visumorph.flip import flip
from visumorph.Image import load_image
import numpy as np
import pytest
import os

# Create a directory to store the test results
RESULTS_DIR = 'tests/img/results/flip_results'
os.makedirs(RESULTS_DIR, exist_ok=True)


def test_flip_vertically():
    img = load_image('tests/img/raw/meme.jpg')
    flipped_img = flip(img, v=1)

    assert flipped_img.get_dimensions() == img.get_dimensions()

    # Check if the top row of pixels is the same in both images (since it's flipped vertically)
    assert np.array_equal(flipped_img.image[0, :], img.image[-1, :])

    # Save the flipped image to the results directory
    flipped_img.save(os.path.join(RESULTS_DIR, 'flipped_vertically.jpg'))


def test_flip_horizontally():
    img = load_image('tests/img/raw/meme.jpg')
    flipped_img = flip(img, v=0)

    assert flipped_img.get_dimensions() == img.get_dimensions()

    # Check if the leftmost column of pixels is the same in both images (since it's flipped horizontally)
    assert np.array_equal(flipped_img.image[:, 0], img.image[:, -1])

    # Save the flipped image to the results directory
    flipped_img.save(os.path.join(RESULTS_DIR, 'flipped_horizontally.jpg'))


def test_flip_with_invalid_v_value():
    img = load_image('tests/img/raw/meme.jpg')

    with pytest.raises(TypeError):
        flip(img, v=2)


def test_flip_with_non_image_input():
    with pytest.raises(TypeError):
        flip('not_an_image', v=1)


def test_flip_with_background():
    img = load_image('tests/img/raw/meme.jpg')
    background_img = load_image('tests/img/raw/background.jpg')

    flipped_with_bg = flip(img, v=1)

    assert flipped_with_bg.get_dimensions() == img.get_dimensions()

    # Check if the top row of pixels is the same in both images (since it's flipped vertically)
    assert np.array_equal(flipped_with_bg.image[0, :], img.image[-1, :])

    # Check if the background is present in the bottom row of pixels
    assert np.array_equal(flipped_with_bg.image[-1, :], background_img.image[0, :])

    # Save the flipped image with background to the results directory
    flipped_with_bg.save(os.path.join(RESULTS_DIR, 'flipped_with_background.jpg'))
