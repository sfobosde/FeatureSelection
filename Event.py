class UserEvent:
    def __init__(self):
        self.__eventhandlersample = []

    def add_handler(self, handler):
        self.__eventhandlersample.append(handler)
        return self

    def remove_handler(self, handler):
        self.__eventhandlersample.remove(handler)
        return self

    def __call__(self, *args, **kwargs):
        for eventhandlersample in self.__eventhandlersample:
            eventhandlersample(*args, **kwargs)
