import time  # Import time library
import threading
from random import randint
from multiprocessing.dummy import Pool as ThreadPool

CAL = 0  # Calibration (+- cm)

print("Measurement Started")


def dist_calc():
    number = (randint(1, 9))

    return number


def centroid(A, B, C):
    xco = float((1 - C ** 2 + A ** 2) / 2)
    yco = float((1 - B ** 2 + A ** 2) / 2)

    print (xco, yco)
    return xco, yco


while True:  # Continuous operation


    time.sleep(2)  # Delay of 2 seconds for easier readings
    array = []
    pool = ThreadPool(processes=4)
    results_task = [pool.apply_async(dist_calc,()) for i in range(4)]

    t1 = threading.Thread(target=dist_calc)
    t2 = threading.Thread(target=dist_calc)
    t3 = threading.Thread(target=dist_calc)
    t4 = threading.Thread(target=dist_calc)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    results = list(map(lambda r: r.get(), results_task))




    results.sort()
    print(results)

    xco, yco = centroid(results[0], results[1], results[2])
