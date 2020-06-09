import pandas as pd
import yaml
import json
from importlib.machinery import SourceFileLoader
import sys
import os.path as osp


def tsv2csv(src_tsv_path: str, dst_csv_path: str):
    """
    Convert tsv file to csv file
    """
    csv_table = pd.read_table(src_tsv_path, sep='\t')
    csv_table.to_csv(dst_csv_path, index=False)


def csv2tsv(src_csv_path: str, dst_tsv_path: str):
    """
    Convert csv file to tsv file
    """
    csv_table = pd.read_csv(dst_tsv_path)
    csv_table.to_csv(dst_tsv_path, index=False, sep='\t')


def yaml2dict(yaml_path: str):
    """
    Read yaml file as python dictionary
    """
    with open(yaml_path) as f:
        doc = yaml.full_load(f)
    return doc


def py2dict(py_path: str):
    # pylint: disable=no-value-for-parameter
    """
    Read python file as python dictionary
    """
    parent_dir = osp.dirname(py_path)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

    module_name = osp.splitext(osp.basename(py_path))[0]
    source_file = SourceFileLoader(fullname=module_name,
                                   path=py_path)
    module = source_file.load_module()
    sys.path.pop(0)
    doc = {
        k: v
        for k, v in module.__dict__.items()
        if not k.startswith('__')
    }
    del sys.modules[module_name]
    return doc


def json2dict(json_path: str):
    """
    Read json file as python dictionary
    """
    with open(json_path, 'r') as f:
        doc = json.load(f)
    return doc
