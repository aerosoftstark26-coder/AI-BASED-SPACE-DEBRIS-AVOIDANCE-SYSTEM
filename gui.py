import tkinter as tk

def launch_gui():
    root = tk.Tk()
    root.title("ORBITAI – Space Debris Avoidance System")
    root.geometry("420x260")

    status = tk.Label(root, text="INITIALIZING", font=("Arial", 16))
    status.pack(pady=10)

    info = tk.Label(root, text="", font=("Arial", 12))
    info.pack(pady=10)

    return root, status, info