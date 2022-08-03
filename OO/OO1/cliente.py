class Cliente:
    def __init__(self, nome, status=0):
        self.__nome = nome.title()
        self.__status = status

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status
