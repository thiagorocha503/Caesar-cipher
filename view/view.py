import abc


class IView(abc.ABC):

    @abc.abstractmethod
    def onClickClean(self):
        raise NotImplemented("onClickClean not implemented")

    @abc.abstractmethod
    def onClickEncode(self):
        raise NotImplemented("onClickEncode not implemented")

    @abc.abstractmethod
    def onClickDecode(self):
        raise NotImplemented("onClickDecode not implemented")

    @abc.abstractmethod
    def onClickExit(self):
        raise NotImplemented("onClickDecode not implemented")

    @abc.abstractmethod
    def clean(self):
        raise NotImplemented("clean not implemented")

    @abc.abstractmethod
    def exit(self):
        raise NotImplemented("exit not implemented")

    @abc.abstractmethod
    def setOutput(self, output):
        raise NotImplemented("exit not implemented")

    @abc.abstractmethod
    def showMessageWarning(self, title, warning):
        raise NotImplemented("showMessageWarning not implemented")

    @abc.abstractmethod
    def showMessageError(self, title, error):
        raise NotImplemented("showMessageError not implemented")
