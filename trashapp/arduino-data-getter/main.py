import serial
import time
import requests

URL = "http://127.0.0.1:8000/api/receive-distance/"

ser = serial.Serial('/dev/tty.usbmodem2101', 9600, timeout=0.1)


def read_distance():
    distance_value = None
    try:
        ser.write(b'M')
        ser.reset_input_buffer()
        ser.readline()

        distance_str = ser.readline().decode('utf-8').strip()
        words = distance_str.split(" ")
        if len(words) > 1:
            distance_value = float(words[1])
            print("Distance: " + str(distance_value) + " cm")
    except serial.SerialException as e:
        print("Error reading distance: " + str(e))

    return distance_value

if __name__ == "__main__":
    try:
        while True:
            serial_data = read_distance()
            time.sleep(1)
            if serial_data is not None:
                response = requests.post(URL, data={'serial_data' : serial_data, 'trash_can': 'Trash Can 3'})

    except KeyboardInterrupt:
        print("Exiting...")
        ser.close()