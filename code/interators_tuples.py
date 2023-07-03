import time

# Iterator Function 1
def calc_square(numbers):
    sqr_tup = ()
    for n in numbers:
        #print(f'\n{n} ^ 2 = {n*n}')
        time.sleep(0.1)
        sqr_tup = sqr_tup + (n*n,)
    return sqr_tup;
# Iterator Function 2
def calc_cube(numbers):
    cube_tup = ()
    for n in numbers:
        #print(f'\n{n} ^ 3 = {n*n*n}')
        time.sleep(0.1)
        cube_tup = cube_tup + (n*n*n,)
    return cube_tup
def main():
    numbers = [*range(2, 10, 1)]
    start = time.time()

    # create Iterator of returned dictionary of each function
    sqr_itr = iter(calc_square(numbers,))
    cube_itr = iter(calc_cube(numbers,))

    # Print values of each iterator
    print(next(sqr_itr))
    print(next(cube_itr))

    # print all the values in iterators
    for val in sqr_itr:
        print("Squares:", val)
    for val in cube_itr:
        print("Cubes", val)
    end = time.time()

    print('Execution Time with Generator Functions: {}'.format(end-start))

if __name__ == '__main__':
    try:
       main()
    except Exception as e:
       print("Error running generators:" + str(e))