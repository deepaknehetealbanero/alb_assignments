from io import BytesIO
from io import StringIO

def create_file():
    with open("../data/test_file.txt", "wb") as f:
        f.write(b"test string 1\n")
        f.write(b"test string 2\n")
        f.write(b"test string 3\n")
    print("File test_file.txt created")
# Load data into buffer in Bytes format
def load_data_buffer_bytesio():
    with BytesIO() as f:
        f.write(b"test string buffer 1")
        f.write(b"test string buffer 2")
        f.write(b"test string buffer 3")
        print("Output buffer from BytesIO: ")
        print(f.getvalue())
# similar can be achieved using bytes append but above is faster
def load_data_buffer():
    buffer = b""
    buffer += b"test string 1"
    buffer += b"test string 2"
    buffer += b"test string 3"
    print("Output from append Buffer: ")
    print(buffer)

def load_data_stringio():
    with StringIO() as s:
        s.write("test string StringIO 1")
        s.write("test string StringIO 2")
        s.write("test string StringIO 3")
        print("Output from StringIO: ")
        print(s.getvalue())

def main():

    test_string = "Test string data to load into StringIO object"
    #open create a file and write data to it
    create_file()

    # Instead of writing data to file, load it in buffer as bytes format using bytesio
    load_data_buffer_bytesio()

    # similar can be achieved using bytes append but above is faster
    load_data_buffer()

    # StringIO
    load_data_stringio()

    # Use StringIO object to use as a file
    in_file = StringIO(test_string)

    # Set the cursor at index 0
    in_file.seek(0)

    out_file = BytesIO(b"test_string 1")
    out_file.seek(0)
    print("byteio", out_file.read())
    print ("Writing data from StringIO file object:", in_file.read())

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error while loading data to buffer: " + str(e))
