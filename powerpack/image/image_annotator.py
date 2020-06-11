from PIL import Image


class ImageAnnotator(object):

    def __init__(self, img_path: str):
        assert isinstance(img_path, str)
        self.img = Image.open(img_path)
