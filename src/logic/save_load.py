from abc import ABC, abstractmethod
from ..data.image import ILoadImage, ISaveImage, SaveImageJPG, SaveImagePNG, AbstractImage


class ISaveComponentConfigurator(ABC):

    @abstractmethod
    def add_jpg(self):
        pass

    @abstractmethod
    def add_png(self):
        pass

    @abstractmethod
    def get_extensions(self):
        pass


class SaveComponentConfigurator(ISaveComponentConfigurator):

    def __init__(self):
        self._available_extensions: dict[str, ISaveImage] = dict()

    def add_jpg(self):
        self._available_extensions['.jpg'] = SaveImageJPG()

    def add_png(self):
        self._available_extensions['png'] = SaveImagePNG()

    def get_extensions(self):
        return self._available_extensions


class ISaveComponent(ABC):

    @abstractmethod
    def save(self, image: AbstractImage, path: str, extension: str):
        pass


class SaveComponent(ISaveComponent):

    def __init__(self, configurator: ISaveComponentConfigurator):
        self._configurator = configurator

    def save(self, image: AbstractImage, path: str, extension: str):
        self._configurator.get_extensions()['extension'].save_image(image, path)


class ILoadComponent(ABC):

    @abstractmethod
    def load(self, path) -> AbstractImage:
        pass


class LoadComponent(ILoadComponent):

    def __init__(self, load_type: ILoadImage):
        self._load_type: ILoadImage = load_type

    def load(self, path) -> AbstractImage:
        image = self._load_type.load(path)
        return image
