import tkinter as tk

total = 26000
expenses = []
remaining_cash = 0

with open(r"C:\Users\salam\OneDrive\Desktop\expenses.txt") as f:
    lines = f.readlines()
    for line in lines:
        if "total" in line:
            continue
        elif line.startswith("-"):
            continue
        elif line.strip().isdigit():
            continue
        elif any(month in line for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]):
            continue
        else:
            expense = line.strip().split()
            expenses.append(int(expense[-1]))

    # calculate the remaining cash
    remaining_cash = total - sum(expenses)

reimbursement = total - sum(expenses)
# create the GUI window
window = tk.Tk()
window.title("Expense Calculator")

# create the frames
total_frame = tk.Frame(window, bd=2, relief=tk.GROOVE, padx=20, pady=20)
total_frame.pack(side=tk.LEFT)

remaining_cash_frame = tk.Frame(window, bd=2, relief=tk.GROOVE, padx=20, pady=20)
remaining_cash_frame.pack(side=tk.RIGHT)

# create the labels
total_label = tk.Label(total_frame, text="Total expenses: " + str(sum(expenses)), width=20, height=3, font=("Arial", 16))
total_label.pack()

remaining_cash_label = tk.Label(remaining_cash_frame, text="Remaining cash: " + str(remaining_cash), width=20, height=3, font=("Arial", 16))
remaining_cash_label.pack()

# run the main event loop
window.mainloop()