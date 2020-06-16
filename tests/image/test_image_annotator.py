import pytest
import powerpack
import os
import os.path as osp
from PIL import Image

BASE_DIR = osp.dirname(osp.dirname(osp.abspath(__file__)))


def test_image_annotator():
    sample_path = osp.join(BASE_DIR, 'data/image/sample.jpg')
    output_path = osp.join(BASE_DIR, 'data/image/annotated_sample.jpg')
    annotator = powerpack.ImageAnnotator(img_path=sample_path)
    annotator.draw_text(points=(10, 10), text='This is a cat', fill='red')
    annotator.draw_line(points=((30, 30), (30, 100)), fill='green', width=3)
    annotator.draw_rectangle(points=((200, 200), (300, 300)), outline='blue',
                             width=3, text='rectangle', text_fill='blue')
    annotator.draw_polygon(points=((200, 100), (100, 150), (300, 150)),
                           outline='black', width=5, text='polygon',
                           text_fill='yellow'
                           )
    annotator.save(output_path)
    assert isinstance(annotator.image(), Image.Image)

    assert osp.exists(output_path)

    os.remove(output_path)
