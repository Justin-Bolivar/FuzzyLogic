import tkinter as tk
from tkinter import ttk

class SpiceToleranceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Spice Tolerance Calculator")

        self.scoville = tk.DoubleVar()
        self.tolerance = tk.DoubleVar()
        self.result = tk.StringVar()

        ttk.Label(root, text="Enter Dish Scoville Rating:").grid(row=0, column=0, padx=10, pady=10)
        self.scoville_entry = ttk.Entry(root, textvariable=self.scoville)
        self.scoville_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(root, text="Enter Your Spice Tolerance (1-10):").grid(row=1, column=0, padx=10, pady=10)
        self.tolerance_entry = ttk.Entry(root, textvariable=self.tolerance)
        self.tolerance_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(root, text="Calculate", command=self.calculate_spiciness).grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=10)
        ttk.Label(root, textvariable=self.result).grid(row=3, column=1, padx=10, pady=10)

    def calculate_spiciness(self):
        scoville_rating = self.scoville.get()
        tolerance_level = self.tolerance.get()

        adjusted_spiciness = scoville_rating / (tolerance_level * 1000)

        if adjusted_spiciness <= 0.1:
            result = "Not Spicy"
        elif 0.1 < adjusted_spiciness <= 1:
            result = "Mild"
        elif 1 < adjusted_spiciness <= 2:
            result = "Moderate"
        else:
            result = "Spicy"

        self.result.set(result)


if __name__ == "__main__":
    root = tk.Tk()
    app = SpiceToleranceCalculator(root)
    root.mainloop()
