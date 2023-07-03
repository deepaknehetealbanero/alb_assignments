from dataclasses import dataclass
from dataclass_wizard import JSONSerializable, json_field, JSONWizard


@dataclass
class MyClass(JSONSerializable):
    my_str: str #= json_field('myString1', all=True)
    count: int
    ratio: float


def main():
    # De-serialize a dictionary object with the newly mapped JSON key.
    d = {'myStr': 'testing',
         'Count': '123',
         'Ratio': '0.33345'}
    c = MyClass.from_dict(d)

    # DataClass to mix case data camel case and Snake Case.
    #print(repr(c))
    print(c)

    # Access data from Json when the case is not matching with dataclass
    print(c.my_str)

    #convert dataclass object data to python dictionary object
    print(c.to_dict())

    #print python dictionary object.
    print(d)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error while processing Camel case to Snake case data" + str(e))