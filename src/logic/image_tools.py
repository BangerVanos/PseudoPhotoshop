from PIL import Image
from abc import ABC, abstractmethod
from ..data.image import AbstractImage
import numpy as np


class ITool(ABC):

    @abstractmethod
    def apply_tool(self, image: AbstractImage, **kwargs) -> AbstractImage:
        pass


class SizeTool(ITool):

    def apply_tool(self, image: AbstractImage, **kwargs) -> AbstractImage:
        new_size = (kwargs['size_x'], kwargs['size_y'])
        processed_raw_image = image.image.resize(new_size)
        image.set_image(processed_raw_image)
        return image


class WhiteBalanceTool(ITool):

    def apply_tool(self, image: AbstractImage, **kwargs):
        lab_img = image.image.convert('LAB')
        img_array = np.array(lab_img)
        avg_a = np.mean(img_array[:, :, 1])
        avg_b = np.mean(img_array[:, :, 2])
        img_array[:, :, 1] = img_array[:, :, 1] - ((avg_a - 128) * (img_array[:, :, 0] / 255.0) * kwargs['multiplier'])
        img_array[:, :, 2] = img_array[:, :, 2] - ((avg_b - 128) * (img_array[:, :, 0] / 255.0) * kwargs['multiplier'])
        processed_raw_image = Image.fromarray(img_array, 'LAB').convert('RGB')
        image.set_image(processed_raw_image)
        return image


class ColorSpaceTool(ITool):

    def apply_tool(self, image: AbstractImage, **kwargs) -> AbstractImage:
        processed_raw_image = image.image.convert(kwargs['color_space'])
        image.set_image(processed_raw_image)
        return image
