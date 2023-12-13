from abc import ABC, abstractmethod
from dataclasses import dataclass
import PIL.Image


class AbstractImage(ABC):

    @abstractmethod
    def set_image(self, image):
        pass


@dataclass
class Image(AbstractImage):
    image: PIL.Image.Image

    def set_image(self, image):
        self.image = image


class ILoadImage(ABC):

    @abstractmethod
    def load(self, path: str) -> Image:
        pass


class LoadImageFromFile(ILoadImage):

    def load(self, path: str) -> Image:
        image = Image(PIL.Image.open(path))
        return image


class ISaveImage(ABC):

    @abstractmethod
    def save_image(self, image: AbstractImage, path: str):
        pass


class SaveImagePNG(ISaveImage):

    def save_image(self, image: AbstractImage, path: str):
        image.image.save(path, format='png')


class SaveImageJPG(ISaveImage):

    def save_image(self, image: AbstractImage, path: str):
        image.image.save(path, format='jpg')
