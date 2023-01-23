from tkinter import *

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandas import DataFrame

from Entities.Column import Column
from UserForms.MainFrame.IFormDesigner import IFormDesigner
from UserForms.MainFrame.IMainFrame import IMainFrame

import matplotlib.pyplot as plt

class MainFrameDesigner(IFormDesigner):
    bar_graph_button: Button

    def __init__(self, frame: IMainFrame):
        self.window = frame.window
        self.frame = frame
        self.initialize_form()
        self.selected_column = IntVar()
        self.dataset = None

    def initialize_form(self):
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

        control_frame = self.create_frame(root_frame=body_frame,
                                          border_width=0,
                                          padx=20,
                                          pady=20)

        self.bar_graph_button = self.add_button_text(frame=control_frame,
                                                     click_handler=self.create_bar_graph,
                                                     text="Show column Bar",
                                                     padx=10,
                                                     pady=10)
        self.bar_graph_button.grid(column=0, row=0)

        self.add_label(loading_frame,
                       label_text="Load file:")

        self.add_button_text(click_handler=self.frame.load_button_clicked,
                             frame=loading_frame,
                             text="Import",
                             padx=5,
                             pady=15,
                             side=LEFT)

        self.add_button_text(click_handler=self.frame.drop_columns,
                             frame=body_frame,
                             text="Drop selected columns")

    # Creating frame on root frame.
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
                        side=LEFT) -> Button:
        button = Button(frame, text=text, command=click_handler)
        button.pack(
            padx=padx,
            pady=pady,
            side=side)

        return button

    def show_elements(self, dataframe: DataFrame, count=5):
        n_cols = dataframe.shape[1]
        # adding 5 the other rows into the grid.
        for i in range(count):
            for j in range(n_cols):
                text = Text(self.dataset_frame, width=7, height=1)
                text.grid(row=i + 3, column=j)
                text.insert(INSERT, dataframe.loc[i][j])

    def show_dataframe_headers(self, col, i, j):
        text = Text(self.dataset_frame, width=7, height=1, bg="#9BC2E6")
        text.grid(row=i + 2, column=j)
        text.insert(INSERT, col)

    def visualise_dataframe(self, dataframe: DataFrame):
        self.dataset = dataframe
        self.dataset_frame = self.create_frame(pady=20, padx=20)
        column_names = dataframe.columns

        self.create_choice_list(column_names)

        i = 0
        for j, col in enumerate(column_names):
            column = Column(col)
            button = Button(self.dataset_frame,
                            command=column.drop_button_clicked,
                            text="Using")
            button.grid(row=i+1, column=j)
            column.button = button

            column.add_to_droplist.add_handler(self.frame.add_to_dl)
            column.remove_from_droplist.add_handler(self.frame.remove_from_dl)

            self.show_dataframe_headers(col, i, j)

        self.show_elements(dataframe)

    # Print new dataset.
    def show_cleaned_dataset(self, dataframe):
        self.dataset_frame = self.create_frame(pady=20, padx=20)
        column_names = dataframe.columns

        i = 0
        for j, col in enumerate(column_names):
            self.show_dataframe_headers(col, i, j)

        self.show_elements(dataframe)

    # Create radiobutton widget.
    def create_choice_list(self, variants: list):
        j = 0
        for variant in variants:
            radiobutton = Radiobutton(self.dataset_frame,
                                      text=variant,
                                      value=j,
                                      variable=self.selected_column,
                                      command=self.column_selected,
                                      width=8,
                                      font=("Arial", 5))
            radiobutton.grid(column=j, row=0)
            j += 1

    # Get selected in radiobutton column.
    def get_column_name(self):
        column = self.dataset.columns[self.selected_column.get()]
        return column

    # Handle selecting column.
    def column_selected(self):
        self.bar_graph_button.configure(text=f"Show {self.get_column_name()} bar graphic")

    # Show selected column bar graphic clicked.
    def create_bar_graph(self):
        column_name = self.get_column_name()
        column = self.dataset[column_name]
        values = column.value_counts()
        indexes = column.unique()

        graphic_window = Tk()

        figure = Figure(figsize=(6, 4), dpi=100)

        figure_canvas = FigureCanvasTkAgg(figure, graphic_window)
        NavigationToolbar2Tk(figure_canvas, graphic_window)

        axes = figure.add_subplot()
        axes.bar(indexes, list(values))

        figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        graphic_window.mainloop()

