from sklearn import linear_model
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error, r2_score
# from statsmodels.stats.outliers_influence import variance_inflation_factor

import operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Format
plt.style.use('seaborn-whitegrid')

#Generate a set of sample data for polynomial regression
def generate_data_set():
    np.random.seed(0)
    x = 2 - 3 * np.random.normal(0, 1, 20)
    y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)

    # transforming the data to include another axis
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    return x, y

x_train, y_train = generate_data_set()

# Polynomial degree is 2
degree = 2

# EXTRA STEP to LinReg: Transform the existing features to higher degree features
poly_features = preprocessing.PolynomialFeatures(degree=degree)
x_train_poly = poly_features.fit_transform(x_train)

# Fit the transformed features to Linear Regression (with TRAINING data) to get the model
poly_model = linear_model.LinearRegression()
poly_model.fit(x_train_poly, y_train)

# Prediction & Output
# Using our model to predict trained & test sets for evaluation
y_poly_pred = poly_model.predict(x_train_poly)
# y_test_pred = poly_model.predict(poly_features.fit_transform(x_test))

# Regression plot, aka Observed-versus-Predicted-values plot
def plot_lin_reg(x,y,y_pred):

    # sort the values of x before line plot (polynomial reg only)
    sort_axis = operator.itemgetter(0)
    sorted_zip = sorted(zip(x, y_pred), key=sort_axis)
    x, y_pred = zip(*sorted_zip)

    # plotting and labelling
    plt.scatter(x, y, color='black')
    plt.plot(x, y_pred, linewidth="3")
    plt.title("Polynomial Regression")
    plt.xlabel("Observed Values")
    plt.ylabel("Predicted Values")
    plt.show()

plot_lin_reg(x_train, y_train,y_poly_pred)

#QQplot
def plot_qq(x):
    stats.probplot(x[:,0], dist="norm", plot=plt)
    plt.title("QQ plot for Normality")
    plt.xlabel("Quantiles")
    plt.ylabel("Observed Values")
    plt.show()

# Normality should be tested on original data before transformation
plot_qq(x_train)

# Residual graphs are sinusoidal.. (Use as demo)
# Residuals-versus-Predicted-values plot
# Calculate Residuals
residuals_train = y_poly_pred - y_train
# print(y_poly_pred,'y_poly_pred')
# print(y_train,"y_train")
# residuals_test = y_test_pred - y_test

def plot_residuals(residuals,y):
    # Residual-observed value plot
    plt.scatter(y, residuals,  color='black')
    plt.axhline(0)
    plt.title("Residuals Versus Predicted Values")
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.show()
plot_residuals(residuals_train, y_poly_pred)

# Multicollinearity not necessary for this example. In detectable cases, use VIF to evaluate

# exos is a list of variable names, representing exogenous variables, i.e. An exogenous variable is a variable that is not affected by other variables in the system.
# endogenic are the complements of exogenic variables, whose values are determined by other variables in the system
# data is a panda dataframe

def vif(exos, data):

    # tolerance is the denominator in VIF calculation
    vif_dict, tolerance_dict = {}, {}

    # for each value of k
    for exo in exos:

        # keep track of the variables which are not k
        endos = [i for i in exos if i != exo]

        # and ensure they are categorized accordingly
        X, y = data[endos], data[exo]

        # extract r-squared from the fit
        r_squared = linear_model.LinearRegression().fit(X, y).score(X, y)

        # calculate VIF of k
        vif = 1/(1 - r_squared)
        vif_dict[exo] = vif

        # calculate tolerance
        tolerance = 1 - r_squared
        tolerance_dict[exo] = tolerance

    # return VIF DataFrame
    df_vif = pd.DataFrame({'VIF': vif_dict, 'Tolerance': tolerance_dict})

    return df_vif
# vif(exos, data)

# Evaluation of the model (WHOLE section, on both training and testing set)
# Metrics for evaluation: R^2, RMSE
rmse_train = np.sqrt(mean_squared_error(y_train, y_poly_pred))
r2_train = r2_score(y_train, y_poly_pred)
print("The model performance for the training set")
print("-------------------------------------------")
print("RMSE for training: {:.5f}".format(rmse_train))
print("R2 for training: {:.5f}".format(r2_train))