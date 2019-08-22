import numpy as np
from sklearn import linear_model

class MarketingCosts:

    # param marketing_expenditure list. Expenditure for each previous campaign.
    # param units_sold list. The number of units sold for each previous campaign.
    # param desired_units_sold int. Target number of units to sell in the new campaign.
    # returns float. Required amount of money to be invested.
    @staticmethod
    def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):
        marketing_expenditure = np.asarray(marketing_expenditure).reshape(-1, 1)
        units_sold = np.asarray(units_sold).reshape(-1, 1)
        regr = linear_model.LinearRegression()
        regr.fit(marketing_expenditure , units_sold)
        return np.float((desired_units_sold - regr.intercept_)/regr.coef_)

#For example, with the parameters below the function should return 250000.0.
print(MarketingCosts.desired_marketing_expenditure(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))