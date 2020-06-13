from PIL import Image
import random
import numpy as np


class Transformer(object):

    def __init__(self, img: Image.Image, **kwargs):
        raise Exception("Not implemented")


class RandomNoise(Transformer):

    def __init__(self, mean: tuple, std: tuple):
        if isinstance(mean, tuple) and len(mean) == 2:
            self.min_mean = mean[0]
            self.max_mean = mean[1]
        elif isinstance(mean, (int, float)):
            self.min_mean = mean
            self.max_mean = mean
        else:
            raise TypeError(
                "Argument mean is either a tuple of 2, int or float.")

        if isinstance(std, tuple) and len(std) == 2:
            self.min_std = std[0]
            self.max_std = std[1]
        elif isinstance(std, (int, float)):
            self.min_std = std
            self.max_std = std
        else:
            raise TypeError(
                "Argument std is either a tuple of 2, int or float.")

    def random_noise(self, img: Image.Image, **kwargs):
        """
        Add random Gaussian noise to image
        """

        mean = random.uniform(self.min_mean, self.max_mean)
        std = random.uniform(self.min_std, self.max_std)

        img = np.asarray(img)
        img = img + np.random.normal(mean, std, img.shape)
        img = Image.fromarray(np.uint8(img))
        return img

