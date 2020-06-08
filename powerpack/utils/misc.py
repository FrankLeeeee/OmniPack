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

