# VisuMorph

![](https://raw.githubusercontent.com/UBC-MDS/VisuMorph/main/docs/logo.png)

[![GitHub Release](https://img.shields.io/github/release/ubc-mds/visumorph.svg?style=flat)]()
[![GitHub Activity](https://img.shields.io/github/last-commit/ubc-mds/visumorph/main.svg?style=flat)]()
[![Documentation Status](https://readthedocs.org/projects/visumorph/badge/?version=latest)](https://visumorph.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

VisuMorph is a powerful, user-friendly Python package designed for image manipulation. It simplifies image processing tasks, allowing users to effortlessly apply transformations and adjustments to their images. With its intuitive interface and a wide range of functionalities, VisuMorph is ideal for both hobbyists and professionals looking to enhance their digital imagery.

## Documentation

The full documentation including installation guides, example usages, and 
API references is hosted on ReadTheDocs and can be found here: 

https://visumorph.readthedocs.io/en/latest/


## Contributors
In alphabetical order:

- Atabak Alishiri
- Orix Au Yeung
- Marco Bravo
- Shawn Hu

## Installation

Currently, this package is not published on PyPI. Installation would be for 
development purposes only.

To install, we recommend to use conda to create a separate environment:

```bash
git clone https://github.com/UBC-MDS/VisuMorph.git && \
cd VisuMorph && \
conda env create -f environment.yml -y && \
conda activate visumorph && \
poetry install
```

## Features

VisuMorph includes a variety of functions for image manipulation:

- **Flipping(`flip`)**: Horizontally or vertically flip images, useful for creating mirror effects or correcting orientation.
- **Rotating(`rotate`)**: Rotate images by a specified degree, supporting both clockwise and anticlockwise rotations.
- **Hue Change(`change_hue`)**: Adjust the hue of images, allowing for color shifting and mood setting in visuals.
- **Scaling(`scale`)**: Resize images, either uniformly or non-uniformly, without losing the essence of the visual content.

## Run the Tests

```bash
pytest
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
