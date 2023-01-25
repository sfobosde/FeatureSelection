from matplotlib import pyplot as plt

from Entities.IFeatureSelectionCore import IFeatureSelectionCore
import pandas as pd
import seaborn as sns

from Event import UserEvent


# Calculation core class.
class FeatureSelectionCore(IFeatureSelectionCore):
    __excluding_columns: list
    key_column: str

    def __init__(self):
        self.show_dataset = UserEvent()
        self.show_cleaned_dataset = UserEvent()
        self.throw_exception = UserEvent()

        self.__excluding_columns = list()

        self.key_column = str()

    # Handle event and catch dataset file.
    def receive_dataset_file(self, ds_file):
        if ds_file:
            self.dataset = pd.read_csv(ds_file)
            self.cleaned_dataset = self.dataset

            self.show_dataset(self.dataset)

    # Get selected key column.
    def catch_key_column(self, key_column):
        self.key_column = key_column

    # The handler of dropping columns from set event.
    def drop_columns(self, columns: list):
        self.__excluding_columns = columns
        self.exclude_columns()
        self.show_cleaned_dataset(self.cleaned_dataset)

    def exclude_columns(self):
        if not len(self.__excluding_columns):
            self.__excluding_columns.append(self.dataset.columns[0])

        self.cleaned_dataset = self.dataset.drop(self.__excluding_columns, axis=1)

    # Standardize handler.
    def handle_standardize(self, key_column):
        self.key_column = key_column

        self.iterate_columns(10)

    def iterate_columns(self, step):
        i = 0
        while i + step < len(self.cleaned_dataset):
            columns_range = [i, i + step]
            i += step
            self.standardize_dataset(columns_range)
        self.standardize_dataset([i, len(self.cleaned_dataset)])

    # Standardize dataset.
    def standardize_dataset(self, columns_range: list):
        if not self.key_column:
            self.key_column = self.dataset.columns[0]

        column = self.dataset[self.key_column]
        data = (self.cleaned_dataset - self.cleaned_dataset.mean()) / (self.cleaned_dataset.std())

        data = pd.concat([column, data.iloc[:, columns_range[0]:columns_range[1]]], axis=1)

        self.standardized_dataset = pd.melt(data, id_vars=self.key_column,
                                            var_name="features",
                                            value_name='value')

        # Call graph drawing.

    # Show violined plot.
    def show_violinplot(self):
        plt.figure(figsize=(10, 10))
        try:
            sns.violinplot(x="features", y="value", hue=self.key_column, split=True, data=self.standardized_dataset,
                           inner="quart")
        except:
            sns.violinplot(x="features", y="value", hue=self.key_column, data=self.standardized_dataset, inner="quart")

        plt.xticks(rotation=90)
        plt.show()

    def show_swarmplot(self):
        plt.figure(figsize=(10, 10))
        sns.swarmplot(x="features", y="value", hue=self.key_column, data=self.standardized_dataset, size=1)

        plt.xticks(rotation=90)
        plt.show()

    def show_correlating_table(self):
        f, ax = plt.subplots(figsize=(18, 18))
        sns.heatmap(self.cleaned_dataset.corr(), annot=True, linewidths=.5, fmt='.1f', ax=ax)
        plt.show()

    def show_correlation_grid(self, correlation_columns: list):
        plt.figure(figsize=(10, 10))
        sns.set(style="white")
        g = sns.PairGrid(self.cleaned_dataset.loc[:, correlation_columns], diag_sharey=False)
        g.map_lower(sns.kdeplot, cmap="Blues_d")
        g.map_upper(plt.scatter)
        g.map_diag(sns.kdeplot, lw=3)
        plt.show()

    # Calculations start event.
    def start_calculations(self):
        self.exclude_columns()
        self.show_cleaned_dataset(self.cleaned_dataset)
        self.iterate_columns(10)

        self.show_correlating_table()

        print("Calc ended")

