import threading
import time


def calc_square(numbers):
    for n in numbers:
        print(f'\n{n} ^ 2 = {n*n}')
        time.sleep(0.1)

def calc_cube(numbers):
    for n in numbers:
        print(f'\n{n} ^ 3 = {n*n*n}')
        time.sleep(0.1)

def main():
    numbers = [*range(2, 10, 1)]
    start = time.time()
    calc_square(numbers)
    calc_cube(numbers)
    end = time.time()

    print('Execution Time without Multi-threading: {}'.format(end-start))
    print("Starting Multi-Threading execution->")
    square_thread = threading.Thread(target=calc_square, args=(numbers,))
    cube_thread = threading.Thread(target=calc_cube, args=(numbers,))

    start = time.time()
    #print(start)

    # Invoke each function in multi-threading
    square_thread.start()
    cube_thread.start()

    # Thread Details and Stats:
    print ("No. of Active threads running:", threading.active_count())
    print("List of threads running:", threading.enumerate())

    # wait for last thread to finish
    square_thread.join()
    cube_thread.join()

    end = time.time()

    print('Execution Time with Multi-threading: {}'.format(end-start))

if __name__ == '__main__':
    try:
       main()
    except Exception as e:
       print("Error running threads:" + str(e))