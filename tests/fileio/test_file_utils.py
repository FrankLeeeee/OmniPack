import pytest
import omnipack
import os
import os.path as osp

BASE_DIR = osp.dirname(osp.dirname(osp.abspath(__file__)))


def test_read_lines():
    sample_path = osp.join(BASE_DIR, 'data/fileio/sample.txt')
    lines = omnipack.read_lines(sample_path)

    assert len(lines) == 2
    assert lines[0] == 'a=1'
    assert lines[1] == 'b=2'


def test_mkdir():
    sample_path = osp.join(BASE_DIR, 'data/fileio/temp')
    omnipack.mkdir(sample_path)

    assert osp.exists(sample_path)

    os.removedirs(sample_path)


def test_find_files():
    res1 = omnipack.find_files(BASE_DIR, '.py$')
    assert len(res1) == 0

    res2 = omnipack.find_files(BASE_DIR, '.py$', 2)
    assert len(res2) == 7

    res3 = omnipack.find_files(BASE_DIR, '.py$', 3)
    assert len(res3) == 8


def test_write_lines():
    sample_path = osp.join(BASE_DIR, 'data/fileio/sample.txt')
    output_path = osp.join(BASE_DIR, 'data/fileio/temp.txt')

    lines = ['a=1', 'b=2']

    omnipack.write_lines(lines, output_path)

    sample_lines = omnipack.read_lines(sample_path)
    output_lines = omnipack.read_lines(output_path)

    assert len(sample_lines) == len(output_lines)

    for i in range(len(sample_lines)):
        assert sample_lines[i] == output_lines[i]

    os.remove(output_path)
