model_classes = {}


def register(c):
    model_classes[c.__name__] = c
    return c


class StructObj:
    def __init__(self, data):
        self._obj = self.__class__.__name__
        self.load_data(data)

    def load_data(self, data):
        for prop in data.keys():
            setattr(self, prop, make_obj_struct(data[prop]))

    def get_data(self):
        return _make_data_struct(self.__dict__)


def _make_object(data):
    objName = data['_obj']
    objClass = model_classes[objName]
    return objClass(data)


def make_obj_struct(d):
    if type(d) == dict:
        if '_obj' in d.keys():
            return _make_object(d)
        else:
            return {key: make_obj_struct(d[key]) for key in d}
    elif type(d) == list:
        return [make_obj_struct(elem) for elem in d]
    else:
        return d


def _make_data_struct(d):
    if isinstance(d, StructObj):
        return d.get_data()
    elif type(d) == dict:
        return {key: _make_data_struct(d[key]) for key in d}
    elif type(d) == list:
        return [_make_data_struct(elem) for elem in d]
    else:
        return d
