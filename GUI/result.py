import tkinter as tk


class ResultViewer(tk.Frame):

    def __init__(self, parent, results: dict, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(background='#9AC5F4')

        self.results = results
        print(results)
        self.counter = 0

        self.title_one = tk.Label(self, text='Data Structure 1', font=('Elvetica', 16), background='#9AC5F4')
        self.title_one.grid(row=0, column=1, padx=50, pady=25)
        self.title_two = tk.Label(self, text='Data Structure 2', font=('Elvetica', 16), background='#9AC5F4')
        self.title_two.grid(row=0, column=2, padx=50, pady=25)

        for (key, value) in zip(self.results.keys(), self.results.values()):
            self.counter += 1
            print(value[0])
            self.key_label = tk.Entry(self, font=('Elvetica', 12))
            self.key_label.insert(0, key)
            self.key_label.configure(state='readonly')
            self.key_label.grid(row=self.counter, column=0, padx=5, pady=5)

            self.ds_one_value = tk.Entry(self, font=('Elvetica', 12))
            self.ds_one_value.insert(0, value[0])
            self.ds_one_value.configure(state='readonly')
            self.ds_one_value.grid(row=self.counter, column=1, padx=5, pady=5)

            self.ds_two_value = tk.Entry(self, font=('Elvetica', 12))
            self.ds_two_value.insert(0, value[1])
            self.ds_two_value.configure(state='readonly')
            self.ds_two_value.grid(row=self.counter, column=2, padx=5, pady=5)

        self.back_to_insert = tk.Button(self, text='Inserimento', font=('Elvetica', 14),
                                        command=lambda: self.parent.show_insert())
        self.back_to_insert.grid(row=self.counter + 1, column=0, padx=50, pady=25, columnspan=3)

