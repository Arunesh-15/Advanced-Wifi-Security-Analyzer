import customtkinter as ctk

from gui.sidebar import Sidebar
from gui.cards import StatCard
from gui.network_table import NetworkTable

from core.scanner import WiFiScanner


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class Dashboard(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Advanced WiFi Security Analyzer")
        self.geometry("1400x800")

        self.scanner = WiFiScanner()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        sidebar = Sidebar(self)
        sidebar.grid(row=0, column=0, sticky="ns")

        content = ctk.CTkFrame(self)
        content.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

        title = ctk.CTkLabel(
            content,
            text="Dashboard",
            font=("Segoe UI", 30, "bold")
        )

        title.pack(anchor="w", padx=20, pady=20)

        cards = ctk.CTkFrame(content, fg_color="transparent")
        cards.pack(fill="x", padx=20)

        self.network_card = StatCard(cards, "Networks", "0")
        self.network_card.pack(side="left", padx=10)

        self.secure_card = StatCard(cards, "Secure", "0")
        self.secure_card.pack(side="left", padx=10)

        self.open_card = StatCard(cards, "Open", "0")
        self.open_card.pack(side="left", padx=10)

        self.risk_card = StatCard(cards, "High Risk", "0")
        self.risk_card.pack(side="left", padx=10)

        scan_button = ctk.CTkButton(
            content,
            text="🔄 Scan Networks",
            command=self.scan_networks,
            width=220,
            height=40
        )

        scan_button.pack(anchor="e", padx=20, pady=15)

        self.table = NetworkTable(content)
        self.table.pack(fill="both", expand=True, padx=20, pady=10)

    def scan_networks(self):

        networks = self.scanner.scan()

        self.table.load_networks(networks)

        total = len(networks)

        secure = 0
        open_wifi = 0

        for net in networks:

            if net["security"] == "Open":
                open_wifi += 1
            else:
                secure += 1

        self.network_card.winfo_children()[1].configure(text=str(total))
        self.secure_card.winfo_children()[1].configure(text=str(secure))
        self.open_card.winfo_children()[1].configure(text=str(open_wifi))
        self.risk_card.winfo_children()[1].configure(text=str(open_wifi))