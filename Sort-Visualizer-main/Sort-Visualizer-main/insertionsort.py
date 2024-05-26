import time

def insertion_sort(data, drawrectangle, delay):
    for i in range(1,len(data)):
        
        curr = data[i]
        j = i - 1
        
        drawrectangle(data, ['yellow' if x == i else 'lightblue' for x in range(len(data))] )
        time.sleep(delay)

        while data[j] > data[j+1] and j >= 0:
            drawrectangle(data, ['yellow' if x == j or x == j+1 else 'lightblue' for x in range(len(data))] )
            time.sleep(delay)
            data[j], data[j+1] = data[j+1], data[j]
            drawrectangle(data, ['green' if x == j or x == j + 1 else 'lightblue' for x in range(len(data))] )
            time.sleep(delay)
            j -= 1
            # drawrectangle(data, ['yellow' if x == i else 'lightblue' for x in range(len(data))] )
            # time.sleep(delay)   
        # data[j+1] = curr
    drawrectangle(data, ['orange' for x in range(len(data))])

    