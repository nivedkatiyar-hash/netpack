import tkinter as tk
from tkinter import ttk
import threading
import time
import random

class NetPack(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("NetPack - Network Inventory")
        self.geometry("950x600")

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        self.setup_page = ttk.Frame(notebook)
        self.results_page = ttk.Frame(notebook)

        notebook.add(self.setup_page, text="Setup")
        notebook.add(self.results_page, text="Results")

        self.build_setup()
        self.build_results()

    def build_setup(self):
        frame = self.setup_page

        ttk.Label(
            frame,
            text="NetPack",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=20)

        form = ttk.Frame(frame)
        form.pack()

        ttk.Label(form, text="Network Name").grid(row=0, column=0, sticky="w", pady=5)
        self.network_name = ttk.Entry(form, width=40)
        self.network_name.insert(0, "Home Network")
        self.network_name.grid(row=0, column=1)

        ttk.Label(form, text="Network Range").grid(row=1, column=0, sticky="w", pady=5)
        self.network_range = ttk.Entry(form, width=40)
        self.network_range.insert(0, "192.168.1.0/24")
        self.network_range.grid(row=1, column=1)

        self.resolve_names = tk.BooleanVar(value=True)

        ttk.Checkbutton(
            form,
            text="Resolve Hostnames",
            variable=self.resolve_names
        ).grid(row=2, column=1, sticky="w", pady=10)

        self.progress = ttk.Progressbar(
            frame,
            mode="determinate",
            length=500
        )
        self.progress.pack(pady=20)

        self.status = ttk.Label(frame, text="Ready")
        self.status.pack()

        ttk.Button(
            frame,
            text="Start Inventory",
            command=self.start_scan
        ).pack(pady=20)

    def build_results(self):
        columns = (
            "IP",
            "Hostname",
            "MAC",
            "Vendor",
            "Status"
        )

        self.tree = ttk.Treeview(
            self.results_page,
            columns=columns,
            show="headings"
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=170)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def start_scan(self):
        self.tree.delete(*self.tree.get_children())
        threading.Thread(target=self.fake_scan, daemon=True).start()

    def fake_scan(self):
        self.progress["value"] = 0

        sample = [
            ("192.168.1.1", "router", "AA:BB:CC:11:22:33", "Example Router", "Online"),
            ("192.168.1.10", "desktop", "00:11:22:33:44:55", "Dell", "Online"),
            ("192.168.1.15", "laptop", "11:22:33:44:55:66", "HP", "Online"),
            ("192.168.1.22", "phone", "22:33:44:55:66:77", "Samsung", "Online"),
            ("192.168.1.30", "printer", "33:44:55:66:77:88", "Brother", "Online"),
        ]

        total = len(sample)

        for i, device in enumerate(sample):
            time.sleep(random.uniform(0.4, 0.8))

            self.tree.insert("", "end", values=device)

            percent = ((i + 1) / total) * 100
            self.progress["value"] = percent
            self.status.config(
                text=f"Processing {device[0]}..."
            )

        self.status.config(text="Inventory Complete")

if __name__ == "__main__":
    app = NetPack()
    app.mainloop()
