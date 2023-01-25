from matplotlib import pyplot as plt
from sklearn.feature_selection import SelectKBest, chi2, RFE, RFECV

from Entities.IFeatureSelectionCore import IFeatureSelectionCore
import pandas as pd
import seaborn as sns

from Event import UserEvent

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


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

    def show_forest_classifier(self):
        x_train, x_test, y_train, y_test = train_test_split(self.cleaned_dataset,
                                                            self.dataset[self.key_column],
                                                            test_size=0.3, random_state=42)
        clf_rf = RandomForestClassifier(random_state=43)
        clr_rf = clf_rf.fit(x_train, y_train)

        ac = accuracy_score(y_test, clf_rf.predict(x_test))
        print('Точность : ', ac)

        cm = confusion_matrix(y_test, clf_rf.predict(x_test))
        sns.heatmap(cm, annot=True, fmt="d")
        #plt.show()

        # Одномерный выбор признаков и классификация случайных древ.
        select_feature = SelectKBest(chi2, k=5).fit(x_train, y_train)
        print('Список баллов:', select_feature.scores_)
        print('Список признаков:', x_train.columns)

        print(pd.DataFrame(select_feature.scores_, x_train.columns))

        x_train_2 = select_feature.transform(x_train)
        x_test_2 = select_feature.transform(x_test)
        # создаем случайный классификатор древа с n_estimators=10 (default)
        clf_rf_2 = RandomForestClassifier()
        clr_rf_2 = clf_rf_2.fit(x_train_2, y_train)
        ac_2 = accuracy_score(y_test, clf_rf_2.predict(x_test_2))
        print('Точность : ', ac_2)
        cm_2 = confusion_matrix(y_test, clf_rf_2.predict(x_test_2))
        sns.heatmap(cm_2, annot=True, fmt="d")

        # RFE
        clf_rf_3 = RandomForestClassifier()
        rfe = RFE(estimator=clf_rf_3, n_features_to_select=5, step=1)
        rfe = rfe.fit(x_train, y_train)
        print('Выбрано 5 лучших признаков по версии rfe:', x_train.columns[rfe.support_])

        # recursive elimination.
        # Оценка «точности» пропорциональна количеству правильных классификаций.
        clf_rf_4 = RandomForestClassifier()
        rfecv = RFECV(estimator=clf_rf_4, step=1, cv=5, scoring='accuracy')  # 5-кратная перекрестная проверка
        rfecv = rfecv.fit(x_train, y_train)

        print('Оптимальное количество признаков :', rfecv.n_features_)
        print('Лучшие признаки :', x_train.columns[rfecv.support_])

        plt.figure()
        plt.xlabel("Количество выбранных признаков")
        plt.ylabel("Оценка перекрестной проверки количества выбранных признаков")
        plt.plot(range(1, len(rfecv.cv_results_["mean_test_score"]) + 1), rfecv.cv_results_["std_test_score"])
        plt.show()

    # Calculations start event.
    def start_calculations(self):
        self.exclude_columns()
        self.show_cleaned_dataset(self.cleaned_dataset)
        self.iterate_columns(10)

        self.show_forest_classifier()

        print("Calc ended")

