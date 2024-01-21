# VisuMorph

VisuMorph is a powerful, user-friendly Python package designed for image manipulation. It simplifies image processing tasks, allowing users to effortlessly apply transformations and adjustments to their images. With its intuitive interface and a wide range of functionalities, VisuMorph is ideal for both hobbyists and professionals looking to enhance their digital imagery.

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

- **Flipping(`flip`)**: Empower your image manipulation endeavors by seamlessly flipping images either horizontally or vertically. This versatile tool serves a multitude of purposes, ranging from crafting captivating mirrored effects to rectifying image orientations with precision.

- **Rotating(`rotate`)**: Elevate your visual content with the ability to elegantly rotate images by precise angles, accommodating both clockwise and counterclockwise rotations. This feature adds a touch of sophistication to your image editing toolkit, allowing you to fine-tune the orientation of your visuals effortlessly.

- **Hue Change(`change_hue`)**: Harness the power of color transformation as you adjust the hue of your images. This functionality provides you with the creative freedom to shift and manipulate colors, enabling you to set distinct moods and evoke specific emotions within your visual compositions.

- **Flipping(`flip`)**: Unlock the potential to resize images in a highly customizable manner, ensuring that the essence and visual integrity remain intact. Whether you require uniform or non-uniform adjustments, this scaling feature empowers you to tailor your images to your exact specifications, preserving their core visual appeal.

## Run the Tests

```bash
pytest
```

## Position in the Python Ecosystem

VisuMorph, although a robust tool for image manipulation, primarily serves as an educational project within the context of the Master of Data Science program's 524 course. It functions as a foundational tool for individuals embarking on their journey in the fields of data science and image processing. While it provides a variety of capabilities, its scope is more limited in comparison to professional-grade libraries such as PIL (Python Imaging Library) and OpenCV. These larger libraries offer a broader range of intricate functionalities tailored for industrial applications. Nevertheless, VisuMorph distinguishes itself through its simplicity and user-friendliness, making it an exceptional starting point for students and enthusiasts seeking to grasp the fundamental concepts of image manipulation in the Python programming language.

For reference to more advanced libraries, you can visit:
- PIL (Python Imaging Library): [PIL](https://python-pillow.org/)
- OpenCV: [OpenCV](https://opencv.org/)

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a [Code of Conduct](CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`visumorph` was created by Orix Au Yeung, Marco Bravo, Atabak Alishiri, Shawn Hu. It is licensed under the terms of the MIT license.

## Credits

`visumorph` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
