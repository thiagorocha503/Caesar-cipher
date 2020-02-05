from view.view import IView
from presenter.presenter import IPresenter
from model.cifra import Cifra


class CifraPresenter(IPresenter):

    def __init__(self, view):
        self.view: IView = view

    def encode(self, text: str, key: str) -> None:
        if key == "" or text == "":
            self.view.showMessageWarning("Campo em branco", "Preencha todos os campos")
            return None
        try:
            cifra = Cifra.encode(text, int(key))
            self.view.setOutput(cifra)
        except Exception as ex:
            self.view.showMessageError("Erro", "Erro inesperado: "+str(ex))

    def decode(self, cifra, key: str) -> None:
        if key == "" or cifra == "":
            self.view.showMessageWarning("Campo em branco", "Preencha todos os campos")
            return None
        try:
            text = Cifra.decode(cifra, int(key))
            self.view.setOutput(text)
        except Exception as ex:
            self.view.showMessageError("Erro", "Erro inesperado: "+str(ex))

    def clean(self) -> None:
        self.view.clean()

    def setView(self, view: IView) -> None:
        self.view = view

    def exit(self) -> None:
        self.view.exit()
