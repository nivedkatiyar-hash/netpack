import tkinter as tk
from tkinter import ttk

class NetPackWizard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("NetPack - Setup Wizard")
        self.geometry("700x450")
        self.resizable(False, False)

        self.pages = []
        self.current = 0

        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_pages()

        nav = ttk.Frame(self)
        nav.pack(fill="x", padx=20, pady=10)

        self.back_btn = ttk.Button(nav, text="◀ Back", command=self.back)
        self.back_btn.pack(side="left")

        self.next_btn = ttk.Button(nav, text="Next ▶", command=self.next)
        self.next_btn.pack(side="right")

        self.show_page(0)

    def page(self, title, builder):
        frame = ttk.Frame(self.container)

        ttk.Label(
            frame,
            text=title,
            font=("Segoe UI", 20, "bold")
        ).pack(anchor="w", pady=(0,15))

        builder(frame)

        self.pages.append(frame)

    def create_pages(self):

        self.page("Welcome", lambda f:
            ttk.Label(
                f,
                text="Welcome to NetPack.\n\nThis wizard will help configure your network discovery scan."
            ).pack(anchor="w")
        )

        def interface_page(frame):
            ttk.Label(frame,text="Network Interface").pack(anchor="w")

            self.interface = ttk.Combobox(frame)
            self.interface["values"] = (
                "Ethernet",
                "Wi-Fi",
                "VPN",
                "Virtual Adapter"
            )
            self.interface.current(1)
            self.interface.pack(fill="x", pady=5)

        self.page("Choose Interface", interface_page)

        def options(frame):
            self.ping = tk.BooleanVar(value=True)
            self.ports = tk.BooleanVar()
            self.host = tk.BooleanVar(value=True)

            ttk.Checkbutton(
                frame,
                text="Discover Live Hosts",
                variable=self.host
            ).pack(anchor="w")

            ttk.Checkbutton(
                frame,
                text="Ping Sweep",
                variable=self.ping
            ).pack(anchor="w")

            ttk.Checkbutton(
                frame,
                text="Basic Port Scan",
                variable=self.ports
            ).pack(anchor="w")

        self.page("Scan Options", options)

        def summary(frame):
            ttk.Label(
                frame,
                text="Click Finish to begin scanning."
            ).pack(anchor="w")

        self.page("Summary", summary)

    def show_page(self, i):

        for p in self.pages:
            p.pack_forget()

        self.pages[i].pack(fill="both", expand=True)

        self.back_btn["state"] = "disabled" if i == 0 else "normal"

        self.next_btn["text"] = "Finish" if i == len(self.pages)-1 else "Next ▶"

    def next(self):
        if self.current < len(self.pages)-1:
            self.current += 1
            self.show_page(self.current)
        else:
            print("Starting scan...")
            self.destroy()

    def back(self):
        if self.current > 0:
            self.current -= 1
            self.show_page(self.current)

app = NetPackWizard()
app.mainloop()
