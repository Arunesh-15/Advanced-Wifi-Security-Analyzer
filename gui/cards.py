import customtkinter as ctk


class StatCard(ctk.CTkFrame):

    def __init__(self, master, title, value):
        super().__init__(master, width=180, height=110)

        self.pack_propagate(False)

        ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 16)
        ).pack(pady=(15,5))

        ctk.CTkLabel(
            self,
            text=value,
            font=("Segoe UI",28,"bold")
        ).pack()