from view.view import IView


class IPresenter:

    def encode(self, text, key):
        raise NotImplemented("encode not implemented")

    def decode(self, cifra, key):
        raise NotImplemented("decode not implemented")

    def clean(self):
        raise NotImplemented("clean not implemented")

    def setView(self, view: IView) -> None:
        raise NotImplemented("setView not implemented")

    def exit(self) -> None:
        raise NotImplemented("close not implemented")
