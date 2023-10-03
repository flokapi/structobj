import structobj as so


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

obj_struct = so.make_obj_struct(data_struct)
print(obj_struct)
print(obj_struct.color)
print(obj_struct.oceans)
print(obj_struct.oceans[0].name)
print(obj_struct.oceans[0].boats)
print(obj_struct.oceans[0].boats[1].passengers)

print(obj_struct.get_data() == data_struct)
