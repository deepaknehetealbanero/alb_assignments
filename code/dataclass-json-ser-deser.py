from dataclasses_serialization.json import JSONSerializer
from dataclasses import dataclass

@dataclass
class StructData:
    id: int
    empl_name: str
    company: str

def main():
    # Serialize data using JSONSerializer
    e = JSONSerializer.serialize(StructData(123, "deepak", "albanero"))
    print("Serialized data:", e)

    #deserialize data using JSONSerializer
    f = JSONSerializer.deserialize(StructData, {'id': 123, 'empl_name': 'deepak', 'company': 'albanero'})
    print("De-Serialized data:", f)

    # Change the id in the de-serialized data
    f.id = 456
    print("Changed column in the de-serialized data:", f.id)

    # # g = JSONSerializer.serialize(f)
    # # print(g)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error while serializing data:" + str(e))
