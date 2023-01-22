class UserEvent:
    def __init__(self):
        self.__eventhandler_sample = []

    def add_handler(self, handler):
        self.__eventhandler_sample.append(handler)
        return self

    def remove_handler(self, handler):
        self.__eventhandler_sample.remove(handler)
        return self

    def __call__(self, *args, **kwargs):
        for eventhandler_sample in self.__eventhandler_sample:
            eventhandler_sample(*args, **kwargs)
