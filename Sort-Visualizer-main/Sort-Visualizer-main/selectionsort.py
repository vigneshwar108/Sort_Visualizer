import time

def selection_sort(data, drawrectangle, delay):
    for i in range(len(data)-1):
        drawrectangle(data, ['green' if x == i else 'lightblue' for x in range(len(data))] )
        ele = data[i]
        index = i
        for j in range(i + 1,len(data)):
            if data[j] < ele:
                ele = data[j]
                index = j
        # print(index)
        if index != i:
            drawrectangle(data, ['yellow' if x == i or x == index else 'lightblue' for x in range(len(data))] )
            time.sleep(delay)
            data[i], data[index] = data[index], data[i]
            drawrectangle(data, ['green' if x == i or x == index else 'lightblue' for x in range(len(data))] )
            time.sleep(delay)
    drawrectangle(data, ['orange' for x in range(len(data))])