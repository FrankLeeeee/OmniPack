import os
import os.path as osp


def read_all_lines(file_path: str):
    """
    Read the file line by line
    """
    assert isinstance(file_path, str), 'file path must be a string'

    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines


def create_workspace(workspace_path: str):
    """
    Create workspace
    """
    assert isinstance(workspace_path, str), 'workspace path must be a string'
    os.makedirs(workspace_path, exist_ok=True)


def read_folder_content(folder_path: str):
    """
    Read the absolute path of files under a folder
    """
    assert isinstance(folder_path, str), 'folder path must be a string'

    res = []
    for file_name in os.listdir(folder_path):
        file_abs_path = osp.join(folder_path, file_name)
        res.append(file_abs_path)
    return res


def write_lines_into_file(lines, file_path: str):
    """
    Write lines into a file
    """
    assert isinstance(lines, (tuple, list))
    assert isinstance(file_path, str)

    with open(file_path, 'w') as f:
        for line in lines:
            f.write('{}\n'.format(line))

