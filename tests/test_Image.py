from visumorph import load_image, scale, rotate, flip, change_hue
from PIL import Image as PImage
import numpy as np


def test_it_loads_jpeg():
    img = load_image("tests/img/raw/jt.jpeg")
    assert img.get_dimensions() == (480, 900, 3)


def test_it_loads_png():
    img = load_image("tests/img/raw/jt.png")
    # png has 4 layers (last one is alpha)
    assert img.get_dimensions() == (480, 640, 4)


def test_it_can_save_image(tmp_path):
    temp_img_name = tmp_path / "pytest_image.jpg"
    img = load_image("tests/img/raw/jt.png")
    img = img.rotate(45).scale(0.4).flip(1).change_hue("white", 0.1)
    img.save(temp_img_name)
    assert np.array_equal(
        img.get_dimensions(),
        load_image(temp_img_name).get_dimensions()
    )

def test_loaded_image_should_have_same_matrix_as_pillow_images():
    image_path = "tests/img/raw/meme.jpg"
    vm_img = load_image(image_path)
    pil_image = PImage.open(image_path)
    assert (np.array(pil_image) == vm_img.image).all()


def test_image_can_print_out_repr_correctly():
    img = load_image("tests/img/raw/meme.jpg")
    msg = str(img)
    assert msg == "VisuMorph Image, dimensions: (414, 552, 3)"


def test_scale_wrapper_should_function_the_same_as_original_func():
    img = load_image("tests/img/raw/meme.jpg")
    assert np.array_equal(scale(img, 0.5).image, img.scale(0.5).image)


def test_rotate_wrapper_should_function_the_same_as_original_func():
    img = load_image("tests/img/raw/meme.jpg")
    assert np.array_equal(rotate(img, 2348.5).image, img.rotate(2348.5).image)


def test_flip_wrapper_should_function_the_same_as_original_func():
    img = load_image("tests/img/raw/meme.jpg")
    assert np.array_equal(flip(img, 1).image, img.flip(1).image)


def test_change_hue_wrapper_should_function_the_same_as_original_func():
    img = load_image("tests/img/raw/meme.jpg")
    assert np.array_equal(
        change_hue(img, color="blue", delta_hue=0.5).image,
        img.change_hue(color="blue", delta_hue=0.5).image,
    )
