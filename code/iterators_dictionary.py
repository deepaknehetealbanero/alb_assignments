import time

# Iterator Function 1
def calc_square(numbers):
    sqr_dict = {}
    for n in numbers:
        #print(f'\n{n} ^ 2 = {n*n}')
        time.sleep(0.1)
        tmp = 'Square_Val_Of ' + str(n)
        sqr_dict[tmp] = {n*n}
    return sqr_dict
# Iterator Function 2
def calc_cube(numbers):
    cube_dict = {}
    for n in numbers:
        #print(f'\n{n} ^ 3 = {n*n*n}')
        time.sleep(0.1)
        tmp = 'Cube_Val_Of ' + str(n)
        cube_dict[tmp] = {n*n*n}
    return cube_dict
def main():
    numbers = [*range(2, 10, 1)]
    start = time.time()

    # create Iterator of returned dictionary of each function
    sqr_itr = iter(calc_square(numbers,))
    cube_itr = iter(calc_cube(numbers,))

    print(type(sqr_itr))
    # Print keys of each iterator
    for val in sqr_itr:
        print(val)

    end = time.time()

    print('Execution Time with Generator Functions: {}'.format(end-start))

if __name__ == '__main__':
    try:
       main()
    except Exception as e:
       print("Error running generators:" + str(e))