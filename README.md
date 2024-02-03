# VisuMorph

![](https://raw.githubusercontent.com/UBC-MDS/VisuMorph/main/docs/logo.png)

[![GitHub Release](https://img.shields.io/github/release/ubc-mds/visumorph.svg?style=flat)]()
[![PyPI - Version](https://img.shields.io/pypi/v/visumorph)](https://pypi.org/project/visumorph/)
[![GitHub Activity](https://img.shields.io/github/last-commit/ubc-mds/visumorph/main.svg?style=flat)]()
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![Documentation Status](https://readthedocs.org/projects/visumorph/badge/?version=latest)](https://visumorph.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9.0+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![codecov](https://codecov.io/github/UBC-MDS/VisuMorph/graph/badge.svg?token=rnxgkcvwda)](https://codecov.io/github/UBC-MDS/VisuMorph)

VisuMorph is a powerful, user-friendly Python package designed for image manipulation. It simplifies image processing tasks, allowing users to effortlessly apply transformations and adjustments to their images. With its intuitive interface and a wide range of functionalities, VisuMorph is ideal for both hobbyists and professionals looking to enhance their digital imagery.

## Documentation

The full documentation including installation guides, example usages, and 
API references is hosted on ReadTheDocs and can be found here: 

https://visumorph.readthedocs.io/en/latest/


## Contributors
In alphabetical order:

- Atabak Alishiri (@atabak-alishiri)
- Orix Au Yeung (@SoloSynth1)
- Marco Bravo (@Marcony1)
- Shawn Hu (@shawnhu444)

## Installation

### For Regular Users

Currently, the package is published on PyPI. If you're looking to use VisuMorph without diving into the development, you can easily install it using pip:

```bash
pip install visumorph
```

### For Developers

For those interested in contributing or exploring the development version, please follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/UBC-MDS/VisuMorph.git
   ```

2. Navigate to the cloned directory and install the package in editable mode along with the development dependencies:
   ```bash
   pip install -e .
   ```


## Features

VisuMorph includes a variety of functions for image manipulation:

- **Flipping(`flip`)**: Horizontally or vertically flip images, useful for creating mirror effects or correcting orientation.
- **Rotating(`rotate`)**: Rotate images by a specified degree, supporting both clockwise and anticlockwise rotations.
- **Hue Change(`change_hue`)**: Adjust the hue of images, allowing for color shifting and mood setting in visuals.
- **Scaling(`scale`)**: Resize images, either uniformly or non-uniformly, without losing the essence of the visual content.

## Quick Start Examples

For a quick glimpse into what VisuMorph can do, here are a few simple examples:

### Flip an Image
Flip an image horizontally or vertically. This example flips an image horizontally.

```python
import visumorph as vm

# Load your image
img = vm.load_image("path/to/image.jpg")

# Flip the image horizontally
flipped_img = vm.flip(img, v=0)

# Save the flipped image
flipped_img.save("path/to/flipped_image.jpg")
```

### Rotate an Image
Rotate an image by a specified angle in degrees. This example rotates an image by 90 degrees.

```python
import visumorph as vm

# Load your image
img = vm.load_image("path/to/image.jpg")

# Rotate the image by 90 degrees
rotated_img = vm.rotate(img, rotation=90)

# Save the rotated image
rotated_img.save("path/to/rotated_image.jpg")
```

### Change Image Hue
Change the hue of an image. This example changes the hue by a delta value.

```python
import visumorph as vm

# Load your image
img = vm.load_image("path/to/image.jpg")

# Change the hue of the image
hue_changed_img = vm.change_hue(img, delta_hue=0.3)

# Save the hue-changed image
hue_changed_img.save("path/to/hue_changed_image.jpg")
```

### Scale an Image
Scale an image by a specified factor. This example enlarges the image by 20%.

```python
import visumorph as vm

# Load your image
img = vm.load_image("path/to/image.jpg")

# Scale the image by 1.2 times
scaled_img = vm.scale(img, scale=1.2)

# Save the scaled image
scaled_img.save("path/to/scaled_image.jpg")
```

Make sure to replace `"path/to/image.jpg"` and the save paths with the actual paths to your image files and desired output locations.


## Running Tests

To ensure VisuMorph works as expected, we've included a suite of tests. You can run these tests using pytest to verify the installation and functionality:

```bash
pytest --cov=visumorph
```

If a coverage report is desired, you can run the above command with an extra arugment:

```bash
pytest --cov=visumorph --cov-report=xml
```

## Position in the Python Ecosystem

VisuMorph, while a robust tool for image manipulation, is designed primarily as an educational project for the 524 course in the Master of Data Science program. It serves as an introductory tool for those beginning their journey in data science and image processing. While it offers a range of functionalities, it is more limited in scope compared to professional-grade packages like PIL (Python Imaging Library) and OpenCV. These larger libraries offer a wider range of complex functionalities and are suited for industrial applications. However, VisuMorph stands out for its simplicity and ease of use, making it an excellent starting point for students and hobbyists looking to understand the basics of image manipulation in Python.

For reference to more advanced libraries, you can visit:
- PIL (Python Imaging Library): [PIL](https://python-pillow.org/)
- OpenCV: [OpenCV](https://opencv.org/)

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a [Code of Conduct](./CONDUCT.md). 
By contributing to this project, you agree to abide by its terms.

## License

`visumorph` was created by Orix Au Yeung, Marco Bravo, Atabak Alishiri, Shawn Hu. It is licensed under the terms of the MIT license.

## Credits

`visumorph` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
