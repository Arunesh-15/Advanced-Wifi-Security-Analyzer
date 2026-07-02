import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=220, corner_radius=0)

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="WiFi\nSecurity",
            font=("Segoe UI", 24, "bold")
        )
        title.pack(pady=25)

        buttons = [
            "🏠 Dashboard",
            "📡 Scan",
            "🛡 Analysis",
            "📄 Reports",
            "⚙ Settings"
        ]

        for text in buttons:
            btn = ctk.CTkButton(
                self,
                text=text,
                height=40
            )
            btn.pack(pady=8, padx=15, fill="x")