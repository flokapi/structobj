# About

This simple modules provides conversion between data structures and objects structures.



This is allows to get the advantage of both:

- data structures:
    - Convenient to save the state and share in an explicit format such as json format.
    - Convenient to generate.
- object structures:
    - Provide methods to the objects.  Convenient to perform operations relative to an object.



# How to use

Objects are represented by a dictionary containing the special `_obj` key and the associated string corresponds to the name of the object that has to be created. The other attributes of the dictionary will be set as object attributes, wich can also contain lists, dictionaries and other objects.

```python
{
    '_obj': 'Boat',
    'country_flag': 'NZ',
    'passengers': 3
}
```



The set of objects which can be created

- must be registered using the `@structobj.register` decorator.
- must inherit the `structobj.StructObj` class



The object structure can be created using the `structobj.make_obj_struct(data)` function.



The data structure of an object structure can be accessed using the  `obj.get_data()` method.



# Installation

```
pip3 install objstruct
```



# Example

```python
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

obj_struct = so.make_obj_struct(data_struct)
print(obj_struct)
print(obj_struct.color)
print(obj_struct.oceans)
print(obj_struct.oceans[0].name)
print(obj_struct.oceans[0].boats)
print(obj_struct.oceans[0].boats[1].passengers)

print(obj_struct.get_data() == data_struct)
```



This will give:

```
New boat
New boat
New ocean
New earth
<__main__.Earth object at 0x7f311930e590>
blue
[<__main__.Ocean object at 0x7f311930f0d0>]
pacific
[<__main__.Boat object at 0x7f311930f090>, <__main__.Boat object at 0x7f31194c2950>]
20
True
```