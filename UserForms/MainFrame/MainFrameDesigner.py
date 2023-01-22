from tkinter import *

from pandas import DataFrame

from UserForms.IFormDesigner import IFormDesigner
from UserForms.IFrame import IFrame


class MainFrameDesigner(IFormDesigner):
    def __init__(self, frame: IFrame):
        self.window = frame.window
        self.frame = frame
        self.initialize_form()

    def initialize_form(self):
        self.window.scroll_x = Scrollbar(self.window, orient=HORIZONTAL)
        self.window.scroll_y = Scrollbar(self.window, orient=VERTICAL)

        body_frame = self.create_frame(anchor=NW,
                                       border_width=0,
                                       relief=SOLID,
                                       padx=20,
                                       pady=20)
        body_frame.pack(fill=BOTH)

        loading_frame = self.create_frame(root_frame=body_frame,
                                          anchor=NW,
                                          border_width=0,
                                          relief=SOLID,
                                          padx=20,
                                          pady=20)

        self.add_label(loading_frame,
                       label_text="Загрузите файл:")

        self.add_button_text(click_handler=self.frame.load_button_clicked,
                             frame=loading_frame,
                             text="Загрузить",
                             padx=5,
                             pady=15,
                             side=LEFT)

    def create_frame(self,
                     root_frame=None,
                     anchor=NW,
                     border_width=0,
                     relief=SOLID,
                     padx=0,
                     pady=0):
        if not root_frame:
            root_frame = self.window

        frame = Frame(root_frame,
                      borderwidth=border_width,
                      relief=relief,
                      padx=padx,
                      pady=pady)
        frame.pack(anchor=anchor)

        return frame

    def add_label(self,
                  frame,
                  label_text="",
                  padx=0,
                  pady=0,
                  side=LEFT,
                  font=("Arial", 14)):
        label = Label(frame, text=label_text, font=font)
        label.pack(
            padx=padx,
            pady=pady,
            side=side,)

    def add_button_text(self,
                        frame,
                        click_handler,
                        text='Click Me!',
                        padx=0,
                        pady=0,
                        side=LEFT):
        button = Button(frame, text=text, command=click_handler)
        button.pack(
            padx=padx,
            pady=pady,
            side=side)

    def visualise_dataframe(self, dataframe: DataFrame):
        dataset_frame = self.create_frame()

        n_cols = dataframe.shape[1]

        column_names = dataframe.columns

        i = 0
        for j, col in enumerate(column_names):
            text = Text(dataset_frame, width=7, height=1, bg="#9BC2E6")
            text.grid(row=i, column=j)
            text.insert(INSERT, col)

        # adding 5 the other rows into the grid.
        for i in range(5):
            for j in range(n_cols):
                text = Text(dataset_frame, width=7, height=1)
                text.grid(row=i + 1, column=j)
                text.insert(INSERT, dataframe.loc[i][j])


