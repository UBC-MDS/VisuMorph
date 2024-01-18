from PIL import Image as PImage
import click


@click.command()
@click.argument(
    "image_path", type=click.Path(exists=True), default="tests/img/raw/meme.jpg"
)
@click.argument("color", type=str, default="red")
@click.argument("delta_hue", type=float, default=0.5)
@click.argument("output_name", type=str, default="hue_adjusted_image")
def change_hue(
    image_path, color="white", delta_hue=0.5, output_name="hue_adjusted_image"
):
    """
    Applies a color hue filter to an image and saves the result.

    This function opens an image from the specified path, applies a color layer with a specified transparency,
    and saves the resulting image. The color layer's hue and transparency can be adjusted.

    Parameters
    ----------
    image_path : str
        The file path to the image to which the hue change will be applied. The path should point to a valid image file.
    color : str, optional
        The color to be used for the hue filter. Default is 'white'.
    delta_hue : float, optional
        The transparency level for the hue filter layer. Values should be between 0 and 1, with 0 being fully transparent and 1 fully opaque. Default is 0.5.
    output_name : str, optional
        The name for the output file. The resulting image will be saved in the 'tests/img/results/' directory with this name and a '.png' extension. Default is 'adjusted_image'.

    Returns
    -------
    None
        This function does not return a value but saves the adjusted image to a file and prints the file path.
    """
    im = PImage.open(image_path)
    layer = PImage.new("RGB", im.size, color)
    adjusted_image = PImage.blend(im, layer, delta_hue)
    output_dir = "tests/img/results/" + output_name + ".png"
    adjusted_image.save(output_dir, "PNG")
    click.echo(f"Image saved to {output_dir}")


if __name__ == "__main__":
    change_hue()
