import RPi.GPIO as GPIO  # Import GPIO library
import time  # Import time library
import threading
from multiprocessing.dummy import Pool as ThreadPool

GPIO.setmode(GPIO.BCM)  # Set GPIO pin numbering

TRIG = 14  # Associate pin 13 to TRIG
ECHO1 = 15  # Associate pin 14 to ECHO
ECHO2 = 18
ECHO3 = 23
ECHO4 = 24

CAL = 0  # Calibration (+- cm)

print("Measurement Started")

GPIO.setup(TRIG, GPIO.OUT)  # Set pin as GPIO out

GPIO.setup(ECHO1, GPIO.IN)  # Set pin as GPIO in
GPIO.setup(ECHO2, GPIO.IN)  # Set pin as GPIO in
GPIO.setup(ECHO3, GPIO.IN)  # Set pin as GPIO in
GPIO.setup(ECHO4, GPIO.IN)  # Set pin as GPIO in


def dist_calc(echo):
    GPIO.output(TRIG, True)  # Set TRIG as HIGH (start square wave)
    time.sleep(0.00001)  # Delay of 0.00001 seconds (10 uS pulse)
    GPIO.output(TRIG, False)  # Set TRIG as LOW (stop square wave)

    while GPIO.input(echo) == 0:  # Check whether the ECHO is LOW
        pulse_start = time.time()  # Saves the last known time of LOW pulse

    while GPIO.input(echo) == 1:  # Check whether the ECHO is HIGH

        pulse_end = time.time()  # Saves the last known time of HIGH pulse

    pulse_duration = pulse_end - pulse_start  # Get pulse duration to a variable
    distance = pulse_duration * 17150  # Multiply pulse duration by 17150 to get distance
    distance = round(distance, 4)  # Round to four decimal points
    return distance


def centroid(A, B, C):
    xco = float((1 - C ** 2 + A ** 2) / 2)
    yco = float((1 - B ** 2 + A ** 2) / 2)

    print(xco, yco)
    return xco, yco

    return xco, yco


while True:  # Continuous operation

    GPIO.output(TRIG, False)  # Set TRIG as LOW
    time.sleep(2)  # Delay of 2 seconds for easier readings
    array = []
    pool = ThreadPool(processes=4)
    results_task = [pool.apply_async(dist_calc, ()) for i in range(4)]

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



    # if distance > 2 and distance < 400:  # Check whether the distance is within range
    #  print
    # "Distance:", distance - CAL, "cm"  # Print distance with CAL adjustment
    # else:
    #   print
    #  "Out Of Range"  # display out of range
