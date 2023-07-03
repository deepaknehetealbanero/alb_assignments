import threading
import time
import multiprocessing


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

    print('Execution Time without Multi-processing: {}'.format(end-start))
    print("Starting Multi-processing execution->")
    # creating processes
    p1 = multiprocessing.Process(target=calc_square, args=(numbers,))
    p2 = multiprocessing.Process(target=calc_cube, args=(numbers,))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # Thread Details and Stats:
    print ("Active children processes running:", multiprocessing.active_children())
    print("PID of process p1:", p1.pid)
    print("PID of process p1:", p2.pid)

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print("All processes finished the job")

    start = time.time()
    #print(start)

    end = time.time()

    print('Execution Time with Multi-processing: {}'.format(end-start))

if __name__ == '__main__':
    try:
       main()
    except Exception as e:
       print("Error running threads:" + str(e))