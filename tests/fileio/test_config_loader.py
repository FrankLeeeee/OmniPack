from omnipack import ConfigLoader
import pytest
import os.path as osp


BASE_DIR = osp.dirname(osp.dirname(osp.abspath(__file__)))


def test_configloader():
    py_sample_path = osp.join(BASE_DIR, 'data/fileio/sample.py')
    json_sample_path = osp.join(BASE_DIR, 'data/fileio/sample.json')
    yaml_sample_path = osp.join(BASE_DIR, 'data/fileio/sample.yaml')

    py_config = ConfigLoader.from_file(py_sample_path)
    assert py_config.a == 1 and py_config.b == 2

    json_config = ConfigLoader.from_file(json_sample_path)
    assert json_config.a == 1 and json_config.b == 2

    yaml_config = ConfigLoader.from_file(yaml_sample_path)
    assert yaml_config.a == 1 and yaml_config.b == 2

    dict_sample = dict(a=1, b=2)
    dict_config = ConfigLoader.from_dict(dict_sample)
    assert dict_config.a == 1 and dict_config.b == 2
