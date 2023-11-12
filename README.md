# TrashApp

**2nd Place Finisher at a Fall 2023 J.B. Hunt Hackathon.** This project involves a smart trash can. The Django web server accepts incoming serial data from an Arduino (my team used an Uno) with an HC-SR04 Ultrasonic Sensor ([something like this](https://www.amazon.com/WWZMDiB-HC-SR04-Ultrasonic-Distance-Measuring/dp/B0B1MJJLJP?keywords=hc+sr04&qid=1699813868&sr=8-5)) and displays the data as a progress bar, indicating how full the trash can is. The functionality is beneficial for homeowners, particularly those with large homes and/or many children. Additionally, it proves useful for businesses such as restaurants, allowing bussers to check a computer screen and see the fill levels of all the trash cans in the restaurant.

## Building
To build this web server locally, follow these instructions:


1. Ensure that Python and pip are installed on your system.

2. Inside the project's root, install the dependencies using:
    ```
    pip install -r requirements.txt
    ```

3. Change into the `trashapp` directory: 
    ```
    cd trashapp
    ```
4. Run the migrate command of the `manage.py` program to create the database file:
    ```
    python manage.py migrate
    ```
5. Now that the database has been generated, start up the web server:
    ```
    python manage.py runserver
    ```

If you wish to send serial data to the server, use the program located at `/trashapp/arduino-data-getter/main.py.` Ensure that you change the name of the trash can in the HTTP post to one that exists in your database. Also, confirm that the `Serial` object `ser` is configured with the correct baud rate and port corresponding to your Arduino.

While the server might accept properly formatted posts directly from your board if your Arduino has Wi-Fi capabilities, this feature has not been thoroughly tested.

## Shoutouts
Thanks to team members [Mason](https://github.com/masoncary26), [Baker](https://github.com/baker0204), and Daniel Powell