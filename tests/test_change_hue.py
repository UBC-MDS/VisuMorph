from visumorph.change_hue import change_hue
import pytest
from click.testing import CliRunner
import os


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture(scope="session")
def test_image_path():
    return "tests/img/raw/meme.jpg"


@pytest.fixture(scope="session")
def output_directory():
    return "tests/img/results/"


def test_default_parameters(runner, test_image_path, output_directory):
    """
    Test the change_hue function with its default parameters.

    This test checks if the change_hue function runs successfully with the default parameters and creates the expected output file in the output directory with the default name.

    Parameters
    ----------
    runner : CliRunner
        A fixture from Click's testing module that isolates command-line tests.
    test_image_path : str
        A fixture providing the path to the test image file.
    output_directory : str
        A fixture providing the path to the output directory where the image will be saved.

    Asserts
    -------
    The test asserts that the command exits with a status code of 0 (success) and that the output file exists at the specified location with the default output name.
    """
    result = runner.invoke(change_hue, [test_image_path])
    assert result.exit_code == 0
    assert os.path.exists(os.path.join(
        output_directory, "hue_adjusted_image.png"))


def test_custom_parameters(runner, test_image_path, output_directory):
    """
    Test the change_hue function with custom parameters.

    This test checks if the change_hue function runs successfully when provided with custom parameters and whether it creates an output file with a custom name.

    Parameters
    ----------
    runner : CliRunner
        A fixture from Click's testing module that isolates command-line tests.
    test_image_path : str
        A fixture providing the path to the test image file.
    output_directory : str
        A fixture providing the path to the output directory where the image will be saved.

    Asserts
    -------
    The test asserts that the command exits with a status code of 0 (success) and that the output file exists at the specified location with the custom output name.
    """
    custom_output_name = "custom_output"
    result = runner.invoke(
        change_hue, [test_image_path, "blue", "0.3", custom_output_name])
    assert result.exit_code == 0
    assert os.path.exists(os.path.join(
        output_directory, custom_output_name + ".png"))


def test_output_file_creation(runner, test_image_path, output_directory):
    """
    Test the change_hue function for output file creation.

    This test verifies that the change_hue function creates an output file with a specified name. It does not check the content of the file, only its existence.

    Parameters
    ----------
    runner : CliRunner
        A fixture from Click's testing module that isolates command-line tests.
    test_image_path : str
        A fixture providing the path to the test image file.
    output_directory : str
        A fixture providing the path to the output directory where the image will be saved.

    Asserts
    -------
    The test asserts that the output file with the specified name exists in the output directory after the function is invoked.
    """
    output_name = "test_output"
    runner.invoke(change_hue, [test_image_path, "green", "0.7", output_name])
    assert os.path.exists(os.path.join(output_directory, output_name + ".png"))
