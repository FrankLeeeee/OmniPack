from PIL import Image


class ImageAugmentor(object):

    def __init__(self, img):
        if isinstance(img, str):
            self.imgs = [img]
        elif isinstance(img, (tuple, list)):
            self.imgs = img
        else:
            raise TypeError(
                'Argument img must be a string or a tuple/list of string')
