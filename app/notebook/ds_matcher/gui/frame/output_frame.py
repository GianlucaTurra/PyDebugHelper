from tkinter import ttk


class OutputFrame(ttk.Frame):

    def __init__(self, parent, results: dict, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.results = results
        self.counter = 1

        self.keys_title = ttk.Label(self, text='Chiave', font=('Elvetica', 16))
        self.keys_title.grid(row=0, column=0, padx=50, pady=25)
        self.title_one = ttk.Label(self, text='Data Structure 1', font=('Elvetica', 16))
        self.title_one.grid(row=0, column=1, padx=50, pady=25)
        self.title_two = ttk.Label(self, text='Data Structure 2', font=('Elvetica', 16))
        self.title_two.grid(row=0, column=2, padx=50, pady=25)

        self.text = f'Sono state trovate {len(results)} differenze!'
        if len(results) == 1:
            self.text = f'È stata trovata {len(results)} differenza!'

        self.results_summary = ttk.Label(self, text=self.text, font=('Elvetica', 16), background='#9AC5F4')
        self.results_summary.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

        for (key, value) in zip(self.results.keys(), self.results.values()):
            self.counter += 1
            self.key_label = ttk.Entry(self, font=('Elvetica', 12))
            self.key_label.insert(0, key)
            self.key_label.configure(state='readonly')
            self.key_label.grid(row=self.counter, column=0, padx=50, pady=5)

            self.ds_one_value = ttk.Entry(self, font=('Elvetica', 12))
            self.ds_one_value.insert(0, value[0])
            self.ds_one_value.configure(state='readonly')
            self.ds_one_value.grid(row=self.counter, column=1, padx=50, pady=5)

            self.ds_two_value = ttk.Entry(self, font=('Elvetica', 12))
            self.ds_two_value.insert(0, value[1])
            self.ds_two_value.configure(state='readonly')
            self.ds_two_value.grid(row=self.counter, column=2, padx=50, pady=5)

        self.back_to_insert = ttk.Button(self, text='Inserimento', command=lambda: self.parent.show_insert())
        self.back_to_insert.grid(row=self.counter + 1, column=0, padx=50, pady=25, columnspan=3)

