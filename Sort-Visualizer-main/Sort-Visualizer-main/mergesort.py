import time

def merge(data, drawrectangle, delay, l, m, r):
    
    n1 = m - l + 1
    n2 = r - m

    left = []

    for i in range(l,m + 1):
        left.append(data[i])

    right = []

    for i in range(m + 1, r + 1):
        right.append(data[i])
         
         
    p1 = 0
    p2 = 0
    p3 = l
         
    while p1 < n1 and p2 < n2:
        if left[p1] < right[p2]:
            data[p3] = left[p1]
            p1 += 1     
        else:
            data[p3] = right[p2]
            p2 += 1
        p3 += 1
    
    while p1 < n1:
        data[p3] = left[p1]
        p1+=1
        p3+=1
    
    while p2 < n2:
        data[p3] = right[p2]
        p2+=1
        p3+=1

    drawrectangle(data, ['blue' if x >= l and x <= r else 'lightblue' for x in range(len(data))])
    time.sleep(delay)

def merge_sort(data, drawrectangle, delay, l, r):
    
    if l >= r:
        return
    
    mid = (l + r)//2

    drawrectangle(data, ['yellow' if x >= l and x <= mid else 'lightblue' for x in range(len(data))])
    time.sleep(delay)
    merge_sort(data, drawrectangle, delay, l, mid)

    drawrectangle(data, ['yellow' if x >= mid + 1 and x <= r else 'lightblue' for x in range(len(data))])
    time.sleep(delay)
    merge_sort(data, drawrectangle, delay, mid+1, r)

    drawrectangle(data, ['green' if x >= l and x <= r else 'lightblue' for x in range(len(data))])
    time.sleep(delay)
    merge(data, drawrectangle, delay, l, mid, r)

    drawrectangle(data, ['orange' for x in range(len(data))])