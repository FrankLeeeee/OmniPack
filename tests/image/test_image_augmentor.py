import pytest
import omnipack
import os
import os.path as osp
from PIL import Image

BASE_DIR = osp.dirname(osp.dirname(osp.abspath(__file__)))


def test_image_annotator():
    sample_path = osp.join(BASE_DIR, 'data/image/sample.jpg')
    output_path = osp.join(BASE_DIR, 'data/image')
    augmentor = omnipack.ImageAugmentor(img=sample_path)

    augmentor.add(omnipack.RandomNoise(mean=0, std=1))
    augmentor.add(omnipack.RandomBlur(min_radius=0.5, max_radius=1.5))
    augmentor.add(omnipack.RandomBrightness(min_factor=0.7, max_factor=1.3))
    augmentor.add(omnipack.RandomColor(min_factor=0.7, max_factor=1.3))
    augmentor.add(omnipack.RandomContrast(min_factor=0.7, max_factor=1.3))
    augmentor.add(omnipack.RandomRotate(min_degree=-5, max_degree=5))

    augmentor.run(times=2, output_path=output_path)

    output_sample_1 = osp.join(BASE_DIR, 'data/image/0_0_sample.jpg')
    output_sample_2 = osp.join(BASE_DIR, 'data/image/0_1_sample.jpg')

    assert osp.exists(output_sample_1) and osp.exists(output_sample_2)
    os.remove(output_sample_1)
    os.remove(output_sample_2)
