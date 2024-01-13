# read version from installed package
from importlib.metadata import version
__version__ = version("visumorph")

from .Image import load_image, Image