import time

import matplotlib.pyplot as plt
import psutil

# pip install matplotlib psutil

plt.ion()
x = []
y = []


def graph(temp):
    y.append(temp)
    x.append(time.time())
    plt.clf()
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.draw()


def get_cpu_temp():
    temp = psutil.sensors_temperatures()["cpu_thermal"][0].current
    return temp


def main():
    while True:
        temp = get_cpu_temp()
        graph(temp)
        plt.pause(1)


if __name__ == "__main__":
    raise SystemExit(main())
