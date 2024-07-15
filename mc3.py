import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def oneRun(distType, mau, subCost, subPercent, subStdDev, adProfit, servCost):
    if distType == 'normal':
        maus = np.random.normal(mau[0], mau[1])
    elif distType == 'uniform':
        maus = np.random.uniform(mau[0], mau[1])
    elif distType == 'triangular':
        maus = np.random.triangular(mau[0], mau[1], mau[2])

    percent = np.random.normal(subPercent, subStdDev) / 100
    
    #net profit = subscription earnings + ad revenue - server maintenance cost 
    return maus * (percent * subCost + adProfit) - servCost


def getMAUs(event):
    distType = distTypeVar.get()
    mauEntry1.grid(row=1, column=1)
    mauEntry2.grid(row=2, column=1)
    mauEntry3.grid_remove()
    mauLabel3.grid_remove()
    
    if distType == 'normal':
        mauLabel1.config(text="MAUs mean:")
        mauLabel2.config(text="MAUs std dev:")
    elif distType == 'uniform':
        mauLabel1.config(text="MAUs low:")
        mauLabel2.config(text="MAUs high:")
    elif distType == 'triangular':
        mauLabel1.config(text="MAUs left:")
        mauLabel2.config(text="MAUs mode:")
        mauLabel3.config(text="MAUs right:")
        mauLabel3.grid(row=3, column=0)
        mauEntry3.grid(row=3, column=1)
    mauLabel1.grid(row=1, column=0)
    mauLabel2.grid(row=2, column=0)


def main():
    global canvas
    try:
        distType = distTypeVar.get()
        mau = [float(mauEntry1.get()), float(mauEntry2.get())]
        if distType == 'triangular':
            mau.append(float(mauEntry3.get()))

        subCost = float(subCostEntry.get())
        subPercent = float(subPercentEntry.get())
        subStdDev = float(subStdDevEntry.get())
        adProfit = float(adProfitEntry.get())
        servCost = float(servCostEntry.get())
        numRuns = int(numRunsEntry.get())

    except ValueError:
        messagebox.showerror("input error", "only numbers accepted")

    runs = []
    for i in range(numRuns):
        runs.append(oneRun(distType, mau, subCost, subPercent, subStdDev, adProfit, servCost))

    messagebox.showinfo("simulation results", f"mean profit: ${np.mean(runs):.2f}\nmedian profit: ${np.median(runs):.2f}\nprofit std dev: ${np.std(runs):.2f}")

    fig, ax = plt.subplots(figsize=(8,4))
    ax.hist(runs, bins=75, color='yellow', edgecolor='black')
    ax.set_title('Simulation Results')
    ax.set_xlabel('Profit ($)')
    ax.set_ylabel('Frequency')

    if canvas:
        canvas.get_tk_widget().pack_forget()

    canvas = FigureCanvasTkAgg(fig, master=plotFrame)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both')


root = tk.Tk()
root.title("Monte Carlo Sim")

canvas = None

distTypeVar = tk.StringVar(root)
distTypeVar.set("normal")  
tk.Label(root, text="distribution type:").grid(row=0, column=0)
distOptions = ttk.Combobox(root, textvariable=distTypeVar, values=["normal", "uniform", "triangular"])
distOptions.grid(row=0, column=1)
distOptions.bind("<<ComboboxSelected>>", getMAUs)

mauLabel1 = tk.Label(root)
mauEntry1 = tk.Entry(root)
mauLabel2 = tk.Label(root)
mauEntry2 = tk.Entry(root)
mauLabel3 = tk.Label(root)
mauEntry3 = tk.Entry(root)
getMAUs(None)

tk.Label(root, text="subscription fee($):").grid(row=4, column=0)
subCostEntry = tk.Entry(root)
subCostEntry.grid(row=4, column=1)

tk.Label(root, text="subscription % mean:").grid(row=5, column=0)
subPercentEntry = tk.Entry(root)
subPercentEntry.grid(row=5, column=1)

tk.Label(root, text="subscription % std dev:").grid(row=6, column=0)
subStdDevEntry = tk.Entry(root)
subStdDevEntry.grid(row=6, column=1)

tk.Label(root, text="ad revenue per user($):").grid(row=7, column=0)
adProfitEntry = tk.Entry(root)
adProfitEntry.grid(row=7, column=1)

tk.Label(root, text="server costs($):").grid(row=8, column=0)
servCostEntry = tk.Entry(root)
servCostEntry.grid(row=8, column=1)

tk.Label(root, text="number of trials:").grid(row=9, column=0)
numRunsEntry = tk.Entry(root)
numRunsEntry.grid(row=9, column=1)

plotFrame = tk.Frame(root)
plotFrame.grid(row=10, columnspan=2)

runButton = tk.Button(root, text="run simulation", command=main)
runButton.grid(row=11, columnspan=2)

root.mainloop()
