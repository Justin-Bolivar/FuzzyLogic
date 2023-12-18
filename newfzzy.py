import tkinter as tk
from tkinter import messagebox

def distance_membership(x):
    if x == 0 or x == 1:
        return [1, 0, 0, 0]
    elif x == 2:
        return [0.7, 0.4, 0.1, 0]
    elif x == 3:
        return [0.4, 0.7, 0.4, 0]
    elif x == 4:
        return [0, 1, 0.6, 0]
    elif x == 5:
        return [0, 0.7, 0.8, 0.2]
    elif x == 6:
        return [0, 0.4, 1, 0.4]
    elif x == 7:
        return [0, 0, 0.7, 0.6]
    elif x == 8:
        return [0, 0, 0.4, 0.8]
    else:
        return [0, 0, 0, 1]

def speed_membership(x):
    if x == 0:
        return [1, 0, 0, 0, 0]
    elif x == 10:
        return [1, 0.3, 0, 0, 0]
    elif x == 20:
        return [0.7, 0.6, 0.1, 0, 0]
    elif x == 30:
        return [0.4, 1, 0.3, 0, 0]
    elif x == 40:
        return [0.1, 0.6, 0.6, 0.3, 0]
    elif x == 50:
        return [0, 0.3, 1, 0.6, 0]
    elif x == 60:
        return [0, 0, 0.6, 1, 0.3]
    elif x == 70:
        return [0, 0, 0.3, 0.8, 0.6]
    elif x == 80:
        return [0, 0, 0.1, 0.4, 1]
    elif x == 90:
        return [0, 0, 0, 0.2, 1]
    else:
        return [0, 0, 0, 0.1, 1]


def calculate_brake_pressure():
    distance = int(distance_entry.get())
    speed = int(speed_entry.get())

    distance_fuzzy = distance_membership(distance)
    speed_fuzzy = speed_membership(speed)

    brake_pressure = [0, 0, 0, 0]

    for i in range(4):
        for j in range(5):
            if i == 0 and j == 0:
                brake_pressure[1] = max(brake_pressure[1], min(distance_fuzzy[i], speed_fuzzy[j]))
            elif i == 0 and j == 1:
                brake_pressure[1] = max(brake_pressure[1], max(distance_fuzzy[i], speed_fuzzy[j]))
            elif i == 1 and j == 0:
                brake_pressure[2] = max(brake_pressure[2], min(distance_fuzzy[i], speed_fuzzy[j]))
            elif i == 1 and j == 1:
                brake_pressure[2] = max(brake_pressure[2], max(distance_fuzzy[i], speed_fuzzy[j]))
            elif i == 2 and j == 2:
                brake_pressure[1] = max(brake_pressure[1], min(distance_fuzzy[i], speed_fuzzy[j]))
            elif i == 3 and j == 3:
                brake_pressure[3] = max(brake_pressure[3], min(distance_fuzzy[i], speed_fuzzy[j]))
            elif i == 3 and j == 4:
                brake_pressure[3] = max(brake_pressure[3], max(distance_fuzzy[i], speed_fuzzy[j]))
            elif i == 4 and j == 4:
                brake_pressure[2] = max(brake_pressure[2], min(distance_fuzzy[i], speed_fuzzy[j]))

    brake_pressure_level = brake_pressure.index(max(brake_pressure))

    if brake_pressure_level == 0:
        messagebox.showinfo("Result", "No Pressure")
    elif brake_pressure_level == 1:
        messagebox.showinfo("Result", "Slight Pressure")
    elif brake_pressure_level == 2:
        messagebox.showinfo("Result", "Normal Pressure")
    else:
        messagebox.showinfo("Result", "Heavy Pressure")


root = tk.Tk()
root.title("Brake Pressure Calculator")

root.geometry("500x300")

distance_label = tk.Label(root, text="Distance (0-10):")
distance_label.pack()

distance_entry = tk.Entry(root)
distance_entry.pack()

speed_label = tk.Label(root, text="Speed (0-100):")
speed_label.pack()

speed_entry = tk.Entry(root)
speed_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_brake_pressure)
calculate_button.pack()

root.mainloop()