from customtkinter import *
from CTkMessagebox import CTkMessagebox

from scripts import systems


class main:
    def __init__(self, root = CTk):
        self.root = root
        self.root.geometry("330x330")
        self.root.title("Калькулятор систем счисления")


        self.root.resizable(False, False)

        self.GetGui()

    def GetRezult(self):
        try:
            num = str(self.Entry1.get())
            system = int(self.Entry3.get())
            system_from = int(self.Entry2.get())

            output = self.TextArea
        
        except Exception:
            CTkMessagebox(title="Ошибка", message="Введённые данные не корректны!", icon='cancel')
        else:
            digit = systems(num=num.lower(), system=system, system_from=system_from)
            if (system_from == 0 or  system_from > 36 or system_from < 2) or (system == 0 or system > 36 or system < 2):
                CTkMessagebox(title="Ошибка", message="Введённые данные не корректны!", icon='cancel')
            else:
                if system == 2 and system_from == 10:
                    result = digit.convert_from()
                
                elif system == 10:
                    result = digit.convert_to()
                else:
                    result = digit.multi()
                output.delete("1.0", 'end')
                try:
                    output.insert("1.0", result)
                except UnboundLocalError:
                    result = str(result)[2:]
                    output.insert("1.0", result)


    def GetGui(self):
        CTkLabel(self.root, text="Число для перевода: ").grid(column=1, row=1, padx=15, pady=10)

        self.Entry1 = CTkEntry(self.root)
        self.Entry1.grid(column=2, row=1, padx=15, pady=10)

        CTkLabel(self.root, text="Система счисления: ").grid(column=1, row=2, padx=15, pady=10)

        self.Entry2 = CTkEntry(self.root)
        self.Entry2.grid(column=2, row=2, padx=15, pady=10)

        CTkLabel(self.root, text="Конечная система: ").grid(column=1, row=3, padx=15, pady=10)

        self.Entry3 = CTkEntry(self.root)
        self.Entry3.grid(column=2, row=3, padx=15, pady=10)

        CTkButton(self.root, text='Перевести', command=self.GetRezult).grid(column=2, row=4, padx=15, pady=20)
        
        self.TextArea = CTkTextbox(self.root, width=280, height=60, )
        self.TextArea.grid(column=1, row=5, columnspan=2)



if __name__ == "__main__":
    root = CTk()
    main(root)
    root.mainloop()