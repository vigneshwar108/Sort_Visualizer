import time

def bubble_sort(data, drawrectangle, delay):
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                drawrectangle(data, ['yellow' if x == j or x == j+1 else 'lightblue' for x in range(len(data))] )
                data[j], data[j+1] = data[j+1], data[j]
                time.sleep(delay)
                drawrectangle(data, ['green' if x == j or x == j+1 else 'lightblue' for x in range(len(data))] )
                time.sleep(delay)
    drawrectangle(data, ['orange' for x in range(len(data))])

    