import tkinter.ttk as ttk
import customtkinter as ctk


class NetworkTable(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Nearby WiFi Networks",
            font=("Segoe UI", 20, "bold")
        )
        title.pack(anchor="w", padx=15, pady=(10, 5))

        columns = (
            "SSID",
            "Security",
            "Signal",
            "Channel"
        )

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=14
        )

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=180, anchor="center")

        self.table.pack(fill="both", expand=True, padx=10, pady=10)

    def clear(self):
        for row in self.table.get_children():
            self.table.delete(row)

    def load_networks(self, networks):

        self.clear()

        for net in networks:

            self.table.insert(
                "",
                "end",
                values=(
                    net["ssid"],
                    net["security"],
                    net["signal"],
                    net["channel"]
                )
            )