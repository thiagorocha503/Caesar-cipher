
class CifraKeyException(Exception):

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return "Key invalid: %s" % str(self.key)
