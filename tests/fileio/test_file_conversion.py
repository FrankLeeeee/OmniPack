import pytest
import powerpack
import os
import os.path as osp

BASE_DIR = osp.dirname(osp.dirname(osp.abspath(__file__)))


def test_py2dict():
    sample_path = osp.join(BASE_DIR, 'data/fileio/sample.py')
    doc_load = powerpack.py2dict(sample_path)
    doc_gt = dict(
        a=1,
        b=2
    )
    assert doc_load == doc_gt


def test_yaml2dict():
    sample_path = osp.join(BASE_DIR, 'data/fileio/sample.yaml')
    doc_load = powerpack.yaml2dict(sample_path)
    doc_gt = dict(
        a=1,
        b=2
    )
    assert doc_load == doc_gt


def test_json2dict():
    sample_path = osp.join(BASE_DIR, 'data/fileio/sample.json')
    doc_load = powerpack.json2dict(sample_path)
    doc_gt = dict(
        a=1,
        b=2
    )
    assert doc_load == doc_gt


def test_csv2tsv():
    sample_path = osp.join(BASE_DIR, 'data/fileio/sample.csv')
    output_path = osp.join(BASE_DIR, 'data/fileio/test_output.tsv')
    expected_output_path = osp.join(BASE_DIR, 'data/fileio/sample.tsv')

    powerpack.csv2tsv(sample_path, output_path)

    output = powerpack.read_lines(output_path)
    expected = powerpack.read_lines(expected_output_path)

    assert len(output) == len(expected)

    for i in range(len(output)):
        assert output[i] == expected[i]

    os.remove(output_path)


def test_tsv2csv():
    sample_path = osp.join(BASE_DIR, 'data/fileio/sample.tsv')
    output_path = osp.join(BASE_DIR, 'data/fileio/test_output.csv')
    expected_output_path = osp.join(BASE_DIR, 'data/fileio/sample.csv')

    powerpack.tsv2csv(sample_path, output_path)

    output = powerpack.read_lines(output_path)
    expected = powerpack.read_lines(expected_output_path)

    assert len(output) == len(expected)

    for i in range(len(output)):
        assert output[i] == expected[i]

    os.remove(output_path)
