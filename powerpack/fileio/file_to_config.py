class DictWrapper(dict):
    """
    Wrap a dictionary object so that we can access
    values as attributes
    """

    def __missing__(self, name):
        raise KeyError(name)

    def __getattr__(self, name):
        value = super(DictWrapper, self).__getitem__(name)
        return value

    def __setattr__(self, name, value):
        super(DictWrapper, self).__setitem__(name, value)


class ConfigLoader(object):
    """
    Load config from files in python/yaml/json format
    """

    @staticmethod
    def from_file(file_path: str):
        pass

    @staticmethod
    def _from_yaml(file_path: str):
        pass

    @staticmethod
    def _from_json(file_path: str):
        pass

    @staticmethod
    def _from_python(file_path: str):
        pass

    @staticmethod
    def from_dict(dictionary: dict):
        return DictWrapper(dictionary)
