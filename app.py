import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

class Encryptor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # ---------------------------------------------------------
        #                      QUIT BUTTON
        # ---------------------------------------------------------
        quit_button = tk.Button(
            text="QUIT",
            fg="white",
            bg="black",
            width=10,
            height=2,
            command=self.master.destroy
        )
        quit_button.pack(
            side="bottom",
            padx=10,
            pady=10
        )

        # ---------------------------------------------------------
        #                           LABEL
        # ---------------------------------------------------------
        label = tk.Label(
            text="Beebe Encryption",
            font=("Arial Bold", 35)
        )
        label.pack(
            # padx=5,
            # pady=5
        )

        # ---------------------------------------------------------
        #                       INPUT BOX
        # ---------------------------------------------------------
        # TODO: MAKE IT LOOK THE WAY IT'S SUPPOSED TO
        entry_box = tk.Entry(
            text="",
            width=50,
            xscrollcommand=True
        )
        entry_box.pack(
            padx=15,
            pady=15
        )

        # ---------------------------------------------------------
        #                    TODO: OUTPUT BOX
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        #                   ENCRPYT BUTTON
        # ---------------------------------------------------------
        # TODO: ENCRYPT FUNC
        # TODO: ALIGN THE BUTTON PROPERLY
        def encrypt():
            pass

        encrypt_button = tk.Button(
            text="ENCRYPT",
            command=encrypt,
            fg="white",
            bg="black",
            width=10,
            height=2
        )
        encrypt_button.pack(
            side="left",
            padx=10,
            pady=10
        )

        # ---------------------------------------------------------
        #                   DECRYPT BUTTON
        # ---------------------------------------------------------
        # TODO: DECRYPT FUNC
        # TODO: ALIGN THE BUTTON PROPERLY
        def decrypt():
            pass

        decrypt_button = tk.Button(
            text="DECRYPT",
            command=decrypt,
            fg="white",
            bg="black",
            width=10,
            height=2
        )
        decrypt_button.pack(
            side="right",
            padx=10,
            pady=10
        )


app = Encryptor(master=root)
app.mainloop()
