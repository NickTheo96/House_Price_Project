import matplotlib.pyplot as plt
import numpy as np
from Class_Data_Loader import DataLoader
from scipy import stats


class DataExploration(DataLoader):  # inherits the members test and train from data_matrix
    def __init__(self, train_X, test_X,  train_Y, test_Y):
        super().__init__(train_X, test_X, train_Y, test_Y)

    def sale_price_against_attribute_scatter_plot(self, target, attribute):  # method that plots sales against an attribute
        x = self._train_X[attribute].values
        y = self._train_X[target].values  # defines the sold price so that it can be loaded into the function each time rather than loading the whole train matrix
        plt.scatter(x, y, c="g", alpha=0.2, label="")  # scatter plot of the sold price and user chosen attribute
        plt.title('Scatter graph of ' + str(target) + ' against ' + str(attribute))
        plt.xlabel(attribute)
        plt.ylabel(target)
        plt.show()

    def describe_attribute(self, attribute):
        print(self._train_X[attribute].describe())

    def histogram(self, attribute):
        x_sigma = self._train_X[attribute].values.std()  # standard deviation
        x_max = self._train_X[attribute].values.max()  # max value
        x_min = self._train_X[attribute].values.min()  # min value
        n = self._train_X[attribute].shape[0]  # number of datapoints

        number_bins = (x_max - x_min) * n ** (1 / 3) / (3.49 * x_sigma)  # formula to give the number of bins for any dataset
        number_bins = int(number_bins)  # floors the double to int
        attribute_being_plotted = self._train_X[attribute].values#values being plotted into the histogram

        # defined y to find y max to place the text
        y, i, _ = plt.hist(attribute_being_plotted, density=True, bins=number_bins, facecolor='paleturquoise', alpha=0.75)


        x = np.linspace(x_min, x_max, len(attribute_being_plotted))
        param = stats.rayleigh.fit(attribute_being_plotted)  # distribution fitting
        pdf_fitted = stats.rayleigh.pdf(x, loc=param[0], scale=param[1])  # fitted distribution
        plt.plot(x, pdf_fitted, 'cornflowerblue', label='rayleigh')#plots the fit

        plt.legend(loc=0)#adds the legend
        plt.ylabel('Probability')
        plt.xlabel(attribute)

        #text that shows the Skewness and Kurtosis
        plt.text((6/9)*x_max, (7/9)*y.max(), r'Skewness: ' + "{0:.3f}".format(self._train_X[attribute].skew()) + '\n' + 'Kurtosis: ' + "{0:.3f}".format(self._train_X[attribute].kurt()), fontsize=12)

        plt.title('Histogram of ' + str(attribute))

        plt.show()




