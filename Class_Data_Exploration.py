import pandas as pd
import matplotlib.pyplot as plt
from Class_Data_Loader import data_loader
import sklearn

class data_exploration(data_loader):  # inherits the members test and train from data_matrix
    def __init__(self, test_X, train_X):
        super().__init__(test_X, train_X)


    def sale_price_against_attribute_scatter_plot(self, target, attribute):#method that plots sales against an attribute
        x = self._train_X[attribute].values
        y = self._train_Y  # defines the sold price so that it can be loaded into the function each time rather than loading the whole train matrix
        plt.scatter(x, y, c="g", alpha=0.25, label="")  # scatter plot of the sold price and user chosen attribute
        plt.xlabel(attribute)
        plt.ylabel(target)
        # plt.legend(loc=2)
        plt.show()

