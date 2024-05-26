import time


def partition(data, drawrectangle, delay, low, high):
    
    i = (low-1)         # index of smaller element
    pivot = data[high]     # pivot
 
    for j in range(low, high):
        drawrectangle(data, ['yellow' if x == j else 'pink' if x == high else 'lightblue' for x in range(len(data))])
        time.sleep(delay) 
        if data[j] <= pivot:
            i = i+1
            drawrectangle(data, ['pink' if x == high else 'green' if x == i or x == j else 'lightblue' for x in range(len(data))])
            time.sleep(delay) 
            data[i], data[j] = data[j], data[i]
            drawrectangle(data, ['pink' if x == high else 'blue' if x == i or x == j else 'lightblue' for x in range(len(data))])
            time.sleep(delay) 
    
    drawrectangle(data, ['pink' if x == high else 'green' if x == i + 1 else 'lightblue' for x in range(len(data))])
    data[i+1], data[high] = data[high], data[i+1]
    drawrectangle(data, ['green' if x == high else 'pink' if x == i + 1 else 'lightblue' for x in range(len(data))])
    return (i+1)

def quick_sort(data, drawrectangle, delay, low, high):
    
    if len(data) == 1:
        return data
    if low < high:
        pivot = partition(data, drawrectangle, delay, low, high)
        drawrectangle(data, ['yellow' if x >= low and x <= pivot - 1 else 'lightblue' for x in range(len(data))])
        time.sleep(delay)
        quick_sort(data, drawrectangle, delay, low, pivot-1)
        drawrectangle(data, ['yellow' if x >= pivot + 1 and x <= high else 'lightblue' for x in range(len(data))])
        time.sleep(delay)
        quick_sort(data, drawrectangle, delay, pivot+1, high)
    drawrectangle(data, ['orange' for x in range(len(data))])