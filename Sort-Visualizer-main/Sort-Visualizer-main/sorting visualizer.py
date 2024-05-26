from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg

import random
from bubblesort import bubble_sort
from selectionsort import selection_sort
from insertionsort import insertion_sort
from mergesort import merge_sort
from quicksort import quick_sort

root = Tk()
root.title('Sort Visualizer')
root.geometry("730x570")
root.config(bg='white')

var = IntVar()

select_algorithm = StringVar()
arr = []

#GENERATING THE ARRAY 
def Generate_array():
    global arr
    lowest = int(lowest_Entry.get())
    highest = int(highest_Entry.get())
    size = int(arrsize_Entry.get())

    arr = []
    for i in range(size):
        arr.append(random.randrange(lowest, highest+1))

    drawrectangle(arr, ['lightblue' for x in range(len(arr))]) 
    
    
#DRAWING THE ARRAY ELEMENTS AS RECTANGLES
def drawrectangle(arr, colorArray):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 600
    bar_width = canvas_width / (len(arr) + 1)
    border_offset = 30
    spacing = 10
    normalized_array = [ i / max(arr) for i in arr]
    for i, height in enumerate(normalized_array):
        #top left coordinates
        x0 = i * bar_width + border_offset + spacing
        y0 = canvas_height - height * 340
        #bottom right coordinates
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(arr[i]))
    
    root.update_idletasks()


def sorting():
    global arr
    
    if var.get() == 1:
        bubble_sort(arr, drawrectangle, sortingspeed.get())
    elif var.get() == 2:
        selection_sort(arr, drawrectangle, sortingspeed.get())
    elif var.get() == 3:
        insertion_sort(arr, drawrectangle, sortingspeed.get())
    elif var.get() == 4:
        merge_sort(arr, drawrectangle, sortingspeed.get(), 0, len(arr) - 1)    
    elif var.get() == 5:
        quick_sort(arr, drawrectangle, sortingspeed.get(), 0, len(arr) - 1)
    else:
        tmsg.showinfo("No Algorithm Selected!", f"Please select a sorting algorithm")

#GUI CODING PART
options_frame = Frame(root, width= 1000, height=300, bg='lightgreen')
options_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(root, width=700, height=377, bg='grey')
canvas.grid(row=1, column=0, padx=10, pady=5)


Label(options_frame, text="Select Algorithm: ",).grid(row=0, column=0, padx=10, pady=10)

Radiobutton(options_frame, text = "Bubble Sort", variable=var, value = 1).grid(row=0, column=1, padx=10, pady=10)
Radiobutton(options_frame, text = "Selection Sort", variable=var, value = 2).grid(row=0, column=2, padx=10, pady=10)
Radiobutton(options_frame, text = "Insertion Sort", variable=var, value = 3).grid(row=0, column=3, padx=10, pady=10)
Radiobutton(options_frame, text = "Merge Sort", variable=var, value = 4).grid(row=0, column=4, padx=10, pady=10)
Radiobutton(options_frame, text = "Quick Sort", variable=var, value = 5).grid(row=0, column=5, padx=10, pady=10)

# algomenu = ttk.Combobox(options_frame, textvariable=select_algorithm, values=['Bubble Sort','Insertion Sort','Merge Sort','Selection Sort','Quick Sort'],width=10)
# algomenu.grid(row=0, column=1, padx=5, pady=5)
# algomenu.current(0)

sortingspeed = Scale(options_frame, from_=0.1, to=5.0, length=100, digits=2, resolution=0.2, orient=VERTICAL, label="Set Delay Time")
sortingspeed.grid(row=1, column=4, padx=10, pady=10)

lowest_Entry = Scale(options_frame, from_=5, to=20, resolution=1, orient=HORIZONTAL, label="Set Lower Limit")
lowest_Entry.grid(row=1, column=0, padx=5, pady=5)

highest_Entry = Scale(options_frame, from_=20, to=100, resolution=1, orient=HORIZONTAL, label="Set Upper Limit")
highest_Entry.grid(row=1, column=1, padx=5, pady=5)

arrsize_Entry = Scale(options_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Set Array size")
arrsize_Entry.grid(row=1, column=2, padx=5, pady=5)

Button(options_frame, text="Generate Array", command=Generate_array, bg='yellow',height=5).grid(row=1, column = 3, padx=5, pady=5)

Button(options_frame, text="Start Sorting", command=sorting, bg='orange',height=5).grid(row=1, column=5, padx=5, pady=5)
root.mainloop()