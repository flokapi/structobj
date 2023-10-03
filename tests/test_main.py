from src import structobj as so


@so.register
class Earth(so.StructObj):
    def __init__(self, data):
        super().__init__(data)
        print('New earth')


@so.register
class Ocean(so.StructObj):
    def __init__(self, data):
        super().__init__(data)
        print('New ocean')


@so.register
class Boat(so.StructObj):
    def __init__(self, data):
        super().__init__(data)
        print('New boat')


data_struct = {
    '_obj': 'Earth',
    'color': 'blue',
    'oceans': [
        {
            '_obj': 'Ocean',
            'name': 'pacific',
            'boats': [
                {
                    '_obj': 'Boat',
                    'country_flag': 'NZ',
                    'passengers': 3
                },
                {
                    '_obj': 'Boat',
                    'country_flag': 'IN',
                    'passengers': 20
                }
            ]
        }
    ]
}


def test_data_preservation():
    obj_struct = so.make_obj_struct(data_struct)
    assert obj_struct.get_data() == data_struct


def test_values():
    obj_struct = so.make_obj_struct(data_struct)
    assert type(obj_struct).__name__ == 'Earth'
    assert obj_struct.color == 'blue'
    assert len(obj_struct.oceans) == 1
    assert obj_struct.oceans[0].name == 'pacific'
    assert len(obj_struct.oceans[0].boats) == 2
    assert obj_struct.oceans[0].boats[1].passengers == 20
