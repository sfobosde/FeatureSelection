from Event import UserEvent

# The column object to realise event inteface.
class Column:
    is_using: bool
    button = None
    add_to_droplist: UserEvent()
    remove_from_droplist: UserEvent()

    def __init__(self, name):
        self.name = name
        self.is_using = True
        self.add_to_droplist = UserEvent()
        self.remove_from_droplist = UserEvent()

    # Handle button click.
    def drop_button_clicked(self):
        if self.is_using:
            # Selected as to drop.
            self.button.config(text="Dropping")
            self.is_using = False
            self.add_to_droplist(self.name)
        else:
            # Selected as to use.
            self.button.config(text="Using")
            self.is_using = True
            self.remove_from_droplist(self.name)
