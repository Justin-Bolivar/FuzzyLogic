import tkinter as tk

# Define the universe of discourse for each input and output
chili_level_range = (0, 10)  # scale from 0 (no chili) to 10 (extremely spicy)
tolerance_range = (0, 10)  # scale from 0 (highly intolerant) to 10 (very tolerant)
spiciness_range = (0, 10)  # scale from 0 (not spicy) to 10 (extremely spicy)

# Define membership functions for chili level
low_spiciness = lambda x: 1 if x <= 2 else 0.5 if 2 < x < 4 else 0
medium_spiciness = lambda x: 0 if x <= 2 or x >= 8 else 1 if 4 <= x <= 6 else 0.5
high_spiciness = lambda x: 0 if x <= 6 else 1 if 8 <= x <= 10 else 0.5

# Define membership functions for spice tolerance
low_tolerance = lambda x: 1 if x <= 2 else 0.5 if 2 < x < 4 else 0
medium_tolerance = lambda x: 0 if x <= 2 or x >= 8 else 1 if 4 <= x <= 6 else 0.5
high_tolerance = lambda x: 0 if x <= 6 else 1 if 8 <= x <= 10 else 0.5

# Define fuzzy rules
rules = [
    # Chili level & Tolerance -> Spiciness
    ((low_spiciness, low_tolerance), low_spiciness),
    ((low_spiciness, medium_tolerance), low_spiciness),
    ((low_spiciness, high_tolerance), medium_spiciness),

    ((medium_spiciness, low_tolerance), medium_spiciness),
    ((medium_spiciness, medium_tolerance), medium_spiciness),
    ((medium_spiciness, high_tolerance), high_spiciness),

    ((high_spiciness, low_tolerance), high_spiciness),
    ((high_spiciness, medium_tolerance), high_spiciness),
    ((high_spiciness, high_tolerance), high_spiciness),
]


def fuzzy_logic(chili_level, tolerance):
    # Calculate the firing strength of each rule
    firing_strengths = {}
    for (antecedents, consequent) in rules:
        low_antecedent, high_antecedent = antecedents
        firing_strength = min(low_antecedent(chili_level), high_antecedent(tolerance))
        firing_strengths[(antecedents, consequent)] = firing_strength

    # Calculate the aggregated output for each membership function of the output variable
    aggregated_outputs = {output: 0 for output in spiciness_range}
    for (antecedents, consequent), firing_strength in firing_strengths.items():
        if firing_strength > 0:
            low_antecedent, high_antecedent = antecedents
            aggregated_outputs[consequent] += firing_strength * (
                low_antecedent(chili_level) + high_antecedent(tolerance)
            ) / 2

    # Calculate the crisp output by defuzzifying the aggregated outputs
    spiciness = sum(
        firing_strength * output for output, firing_strength in aggregated_outputs.items()
    ) / sum(firing_strength for firing_strength in aggregated_outputs.values())

    return spiciness


def update_results():
    # Get user input
    chili_level = float(chili_entry.get())
    tolerance = float(tolerance_entry.get())

    # Calculate and display the result
    spiciness = fuzzy_logic(chili_level, tolerance)
    spiciness_label.config(text=f"Spiciness: {spiciness:.2f}")


# Initialize Tkinter window
root = tk.Tk()
root.geometry("300x200")
root.title("Fuzzy Logic for Cebuano Dish Spiciness")

# Create labels and entries for user input
chili_label = tk.Label(root, text="Chili Level (0-10):")
chili_label.pack()
chili_entry = tk.Entry(root)
chili_entry.pack()

tolerance_label = tk.Label(root, text="Tolerance Level (0-10):")
tolerance_label.pack()
tolerance_entry = tk.Entry(root)
tolerance_entry.pack()

# Create button to trigger calculation and display result
calculate_button = tk.Button(root, text="Calculate", command=update_results)
calculate_button.pack()
calculate_button


# Create label to display the spiciness result
spiciness_label = tk.Label(root, text="Spiciness:")
spiciness_label.pack()

# Start the main loop
root.mainloop()

