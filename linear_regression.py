from __future__ import division
from standard_math import mean
import math as m


class LinearRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_b0b1(self, x, y):

        """
        In simple linear regression, b1 is the slope of the regression line.
        b0 is the intercept of the regression line with the y-axis.

        Equation for the simple regression line : y-hat = b0 + b1*x


        :param x: a list of x values for a series of points
        :param y: a list of y values for a series of points

        :return: b0, b1

        """

        x_bar = mean(x)
        y_bar = mean(y)

        x_minus_xbar = [i - x_bar for i in x]
        y_minus_ybar = [j - y_bar for j in y]

        b1_column_denom = [i*j for i, j in zip(x_minus_xbar, y_minus_ybar)]
        b1_column_num = [i**2 for i in x_minus_xbar]

        numerator = sum(b1_column_denom)
        denominator = sum(b1_column_num)

        b1 = numerator / denominator
        b0 = y_bar - (b1 * x_bar)

        return b0, b1

    def r_squared(self, x, y):
        """
           R-squared is a statistical measure of how close the data is to the
           fitted regression line.
           It is also known as the coefficient of determination.

           The higher the value of R squared, the better the model fits your data.
           R is always between 0 and 1.

        :param x: a list of x values for a series of points
        :param y: a list of y values for a series of points
        :return: r_squared

        """

        y_bar = mean(y)
        y_minus_ybar = [j - y_bar for j in y]
        y_minus_ybar_squared = [j ** 2 for j in y_minus_ybar]
        b0, b1 = self.get_b0b1(x, y)
        y_hat = [b0 + b1 * i for i in x]
        yhat_minus_ybar = [yh - y_bar for yh in y_hat]
        yhat_minus_ybar_squared = [h ** 2 for h in yhat_minus_ybar]

        r_squared = sum(yhat_minus_ybar_squared) / sum(y_minus_ybar_squared)

        return r_squared

    def standarderror(self, y, y_dash):
        """
        The standard error of the estimate is a measure of the accuracy of
        predictions made with a regression line.

        :param y:
        :param y_dash:
        :return: standard_error
        """
        y_minus_ydash = [i-j for i,j in zip(y, y_dash)]
        y_minus_ydash_squared = [i**2 for i in y_minus_ydash]
        total = sum(y_minus_ydash_squared)
        n = len(y)
        standard_error = m.sqrt(total/n)
        return standard_error

