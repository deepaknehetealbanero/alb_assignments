import time

# Generator Function 1
def calc_square(numbers):
    arr = []
    for n in numbers:
        #print(f'\n{n} ^ 2 = {n*n}')
        time.sleep(0.1)
        yield {n*n}

# Generator Function 2
def calc_cube(numbers):
    arr_c = []
    for n in numbers:
        #print(f'\n{n} ^ 3 = {n*n*n}')
        time.sleep(0.1)
        yield {n*n*n}

def main():
    numbers = [*range(2, 10, 1)]
    start = time.time()

    # Invoke each generator function in for loop to get yielded values
    for value in calc_square(numbers,):
        print("Square Values: ", value)
    for value in calc_cube(numbers,):
        print("Cube Values: ", value)

    end = time.time()

    print('Execution Time with Generator Functions: {}'.format(end-start))

if __name__ == '__main__':
    try:
       main()
    except Exception as e:
       print("Error running generators:" + str(e))