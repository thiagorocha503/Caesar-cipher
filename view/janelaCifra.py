import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as tkst

from view.view import IView
from presenter.presenter import IPresenter
from presenter.cifraPresenter import CifraPresenter


class JanelaCifra(IView):

    def __init__(self, master: tk.Tk):
        self.presenter: IPresenter = CifraPresenter(self)
        self.windown: tk.Tk = master

        # Style
        self.style = ttk.Style()
        self.style.theme_use('vista')

        # configuração do Tk
        master.title("Cifra de César")
        master.geometry("800x600")
        master.minsize(width=800, height=600)

        # Frame Container
        self.frmContainer = ttk.Frame(master)
        self.frmContainer.pack(fill=tk.BOTH, expand=True)

        # Frame de entrada
        self.frmInput = ttk.LabelFrame(self.frmContainer, text="Entrada", relief=tk.SOLID, borderwidth=2)
        self.frmInput.pack(fill=tk.X, pady=15, padx=30)
        self.txtInput = tkst.ScrolledText(self.frmInput, wrap=tk.WORD, width=60, height=10)
        self.txtInput.pack(pady=15, padx=15, fill=tk.X)
        self.lblKey = ttk.Label(self.frmInput, text="chave")
        self.lblKey.pack(side=tk.LEFT, padx=15, pady=10)
        self.cbBoxKey = ttk.Combobox(self.frmInput, values=[i for i in range(1, 26)])
        self.cbBoxKey['state'] = 'readonly'
        self.cbBoxKey.pack(side=tk.LEFT)

        # Frame de resultado
        self.frmOutput: ttk.LabelFrame = ttk.LabelFrame(self.frmContainer, text="Resultado", relief=tk.SOLID,
                                                        borderwidth=2)
        self.frmOutput.pack(fill=tk.X, pady=15, padx=30)
        self.txtOutput = tkst.ScrolledText(self.frmOutput, width=60, height=10)
        self.txtOutput['state'] = 'disable'
        self.txtOutput.pack(fill=tk.X, pady=15, padx=15)

        # Frame dos botões
        self.frmButtons = ttk.Frame(self.frmContainer)
        self.frmButtons.pack()
        self.btnEncode: ttk.Button = ttk.Button(self.frmButtons, text="Cifrar")
        self.btnEncode.bind("<Button-1>", self.onClickEncodeEvent)
        self.btnEncode.pack(side=tk.LEFT, padx=10, pady=10)
        self.btnDecode: ttk.Button = ttk.Button(self.frmButtons, text="Descifrar")
        self.btnDecode.bind("<Button-1>", self.decodeEvent)
        self.btnDecode.pack(side=tk.LEFT, )
        self.btnClean: ttk.Button = ttk.Button(self.frmButtons, text="Limpar")
        self.btnClean.bind("<Button-1>", self.onClickCleanEvent)
        self.btnClean.pack(side=tk.LEFT, padx=10)

    # noinspection PyUnusedLocal
    def onClickEncodeEvent(self, event):
        self.onClickEncode()

    def onClickEncode(self):
        text = self.txtInput.get('1.0', tk.END)
        key = self.cbBoxKey.get()
        self.presenter.encode(str(text).replace("\n", ""), key)

    # noinspection PyUnusedLocal
    def decodeEvent(self, event):
        self.onClickDecode()

    def onClickDecode(self):
        text = self.txtInput.get('1.0', tk.END)
        key = self.cbBoxKey.get()
        self.presenter.decode(str(text).replace("\n", ""), key)

    # noinspection PyUnusedLocal
    def onClickCleanEvent(self, event):
        self.onClickClean()

    def onClickClean(self):
        self.presenter.clean()

    def onClickExit(self):
        self.presenter.exit()

    def setOutput(self, output):
        self.txtOutput['state'] = 'normal'
        self.txtOutput.delete('1.0', tk.END)
        self.txtOutput.insert(tk.INSERT, output)
        self.txtOutput['state'] = 'disable'

    def clean(self):
        self.txtInput.delete('1.0', tk.END)
        self.txtOutput['state'] = 'normal'
        self.txtOutput.delete('1.0', tk.END)
        self.txtOutput['state'] = 'disable'
        self.cbBoxKey.set("")

    def exit(self):
        self.windown.destroy()

    def showMessageWarning(self, title, warning):
        messagebox.showwarning(title, warning)

    def showMessageError(self, title, error):
        messagebox.showerror(title, error)


if __name__ == '__main__':
    toplevel = tk.Tk()
    JanelaCifra(toplevel)
    toplevel.mainloop()
