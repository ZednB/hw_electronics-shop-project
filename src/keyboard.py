from src.item import Item


class MixinLog:

    def __init__(self) -> None:
        self.__languages = ['EN', 'RU']

    def get_lang(self):
        return self.__languages


class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity) -> None:
        super().__init__(name, price, quantity)
        self.mixin = MixinLog().get_lang()
        self.__language = self.mixin[0]

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language):
        self.__language = language

    def change_lang(self):
        if self.__language == self.mixin[1]:
            self.__language = self.mixin[0]
            return self.__language
        if self.__language == self.mixin[0]:
            self.__language = self.mixin[1]
            return self.__language
        else:
            raise AttributeError
