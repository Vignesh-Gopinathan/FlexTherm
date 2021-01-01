import os
import re
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

Tl = []
Epot = []
q =[]
boundary = []

root = os.getcwd() + '/Results'
Tl = os.listdir(root)
Epot = os.listdir(root + '/' + Tl[0] + '/')
q = os.listdir(root + '/' + Tl[0] + '/' + Epot[0] + '/')
boundary = os.listdir(root + '/' + Tl[0] + '/' + Epot[0] + '/' + q[0] + '/')
Tl = np.sort(np.array(Tl))
Epot = np.sort(np.array(Epot))
q = np.sort(np.array(q))
boundary = np.sort(np.array(boundary))

# Data Collection.
i = 0
j = 0
data_superheat = np.zeros(12150).reshape(-1,5)
data_contour = np.zeros(116640).reshape(-1,6)

for T in Tl:
    for E in Epot:
        for Q in q:
            for b in boundary:
                contour_path = root + '/' + T + '/' + E + '/' + Q + '/' + b + '/' + '/contour.csv'
                probe_path = root + '/' + T + '/' + E + '/' + Q + '/' + b + '/' + '/probeT.csv'
                if os.path.isfile(contour_path):
                    result = re.search('Tl_(.*)',T)
                    data_superheat[i,0] = result.group(1)
                    result = re.search('Epot_(.*)',E)
                    data_superheat[i,1] = result.group(1)
                    result = re.search('q_(.*)',Q)
                    data_superheat[i,2] = result.group(1)
                    result = re.search('boundary_(.*)',b)
                    data_superheat[i,3] = result.group(1)
                    contour = np.genfromtxt(contour_path,delimiter=' ')
                    j = i*8
                    end = j + 8
                    data_contour[j:end,4] = contour[1:,0]
                    data_contour[j:end,5] = contour[1:,1]
                    while (j < end):
                        data_contour[j,0] =  data_superheat[i,0] 
                        data_contour[j,1] =  data_superheat[i,1]
                        data_contour[j,2] =  data_superheat[i,2]
                        data_contour[j,3] =  data_superheat[i,3]
                        j += 1
                if os.path.isfile(probe_path):
                    probe = np.genfromtxt(probe_path,delimiter=' ')
                    data_superheat[i,4] = probe[1] 
                    i+=1

#***********************************************************************************************************************************************************#

# Data Frame Creation for Superheat.
df_superheat = pd.DataFrame(data = data_superheat[:,:], columns = ['Liquidus_Temperature', 'Electrical_Potential', 'Heat_release_Wall', 'Electrolyte_Boundary', 'Superheat'])

features_superheat = ['Liquidus_Temperature', 'Electrical_Potential', 'Heat_release_Wall', 'Electrolyte_Boundary']
target_superheat = ['Superheat']

df_superheat = df_superheat[df_superheat.Liquidus_Temperature != 0]
df_superheat = df_superheat.sample(frac = 1)
df_superheat = df_superheat[df_superheat.Superheat > 30]

# Data Set preparation for Superheat.
train_superheat = df_superheat[:][0:int(df_superheat.size*0.6/6)]
valid_superheat = df_superheat[:][int(df_superheat.size*0.6/6):int(df_superheat.size*0.8/6)]
test_superheat = df_superheat[:][int(df_superheat.size*0.8/6):]

# CSV file Creation for Superheat.
df_superheat.to_csv('data_superheat.csv',index = False, sep = " ")
 
# Polynomial Regression model for Superheat.
r2_train_superheat = 0
r2_valid_superheat = 0
r2_test_superheat = 0

print("Polynomial Regression model for Superheat:")
for order_superheat in range(1,9):
    poly_superheat = PolynomialFeatures(degree = order_superheat)
    X_train_poly = poly_superheat.fit_transform(train_superheat[['Liquidus_Temperature', 'Electrical_Potential', 'Heat_release_Wall', 'Electrolyte_Boundary']])

    lm = linear_model.LinearRegression()
    lm.fit(X_train_poly, train_superheat['Superheat'])

    train_predicted_superheat = lm.predict(X_train_poly)
    valid_predicted_superheat = lm.predict(poly_superheat.fit_transform(valid_superheat[['Liquidus_Temperature', 'Electrical_Potential', 'Heat_release_Wall', 'Electrolyte_Boundary']]))
    test_predicted_superheat = lm.predict(poly_superheat.fit_transform(test_superheat[['Liquidus_Temperature', 'Electrical_Potential', 'Heat_release_Wall', 'Electrolyte_Boundary']]))

    r2_train_superheat = r2_score(train_superheat['Superheat'], train_predicted_superheat) 
    r2_valid_superheat = r2_score(valid_superheat['Superheat'], valid_predicted_superheat)
    r2_test_superheat = r2_score(test_superheat['Superheat'], test_predicted_superheat)
    
    print("Polynomial Degree:",order_superheat,"\tAccuracy Train:",r2_train_superheat,"\tAccuracy Valid:",r2_valid_superheat,"\tAccuracy Test:",r2_test_superheat)


#***********************************************************************************************************************************************************#

# Data Frame Creation for Ledge Profile.
df_contour = pd.DataFrame(data = data_contour[:,:], columns = ['Liquidus_Temperature', 'Electrical_Potential', 'Heat_release_Wall', 'Electrolyte_Boundary', 'Ledge_profile_x', 'Ledge_profile_z'])
features_contour = ['Liquidus_Temperature', 'Electrical_Potential', 'Heat_release_Wall', 'Electrolyte_Boundary', 'Ledge_profile_x']
target_contour = ['Ledge_profile_z']

df_contour = df_contour[df_contour.Liquidus_Temperature != 0]
df_contour = df_contour.sample(frac = 1)

# CSV file Creation for Ledge profile.
df_contour.to_csv('data_contour.csv',index = False, sep = " ")

# Data Set preparation for Ledge profile.
train_contour = df_contour[:][0:int(df_contour.size*0.6/6)]
valid_contour = df_contour[:][int(df_contour.size*0.6/6):int(df_contour.size*0.8/6)]
test_contour = df_contour[:][int(df_contour.size*0.8/6):]

# Polynomial Regression model for Ledge Profile.
r2_train_contour = 0
r2_valid_contour = 0
r2_test_contour = 0

print("Polynomial Regression model for Ledge Profile:")
for order_contour in range(1,9):
    poly_contour = PolynomialFeatures(degree = order_contour)
    X_train_poly = poly_contour.fit_transform(train_contour[['Liquidus_Temperature', 'Electrical_Potential', 'Heat_release_Wall', 'Electrolyte_Boundary', 'Ledge_profile_x']])

    lm = linear_model.LinearRegression()
    lm.fit(X_train_poly, train_contour['Ledge_profile_z'])

    train_predicted_contour = lm.predict(X_train_poly)
    valid_predicted_contour = lm.predict(poly_contour.fit_transform(valid_contour[['Liquidus_Temperature', 'Electrical_Potential', 'Heat_release_Wall', 'Electrolyte_Boundary', 'Ledge_profile_x']]))
    test_predicted_contour = lm.predict(poly_contour.fit_transform(test_contour[['Liquidus_Temperature', 'Electrical_Potential', 'Heat_release_Wall', 'Electrolyte_Boundary', 'Ledge_profile_x']]))

    r2_train_contour = r2_score(train_contour['Ledge_profile_z'], train_predicted_contour)
    r2_valid_contour = r2_score(valid_contour['Ledge_profile_z'], valid_predicted_contour)
    r2_test_contour = r2_score(test_contour['Ledge_profile_z'], test_predicted_contour)
   
    print("Polynomial Degree:",order_contour,"\tAccuracy Train:",r2_train_contour,"\tAccuracy Valid:", r2_valid_contour,"\tAccuracy Test:", r2_test_contour)

#***********************************************************************************************************************************************************#

# Best fit Case.
trial = np.zeros(8)
order = 3
for i in range(0,8):
    poly_contour = PolynomialFeatures(degree = order)
    X_train_poly = poly_contour.fit_transform(train_contour[['Liquidus_Temperature', 'Electrical_Potential', 'Heat_release_Wall', 'Electrolyte_Boundary', 'Ledge_profile_x']])

    lm = linear_model.LinearRegression()
    lm.fit(X_train_poly, train_contour['Ledge_profile_z'])
    trial[i] = lm.predict(poly_contour.fit_transform([[1218,0.027994,6000,0.975,i]]))

x = np.arange(0,8)
df1 = pd.read_csv('measure.csv',delimiter="\s+")
rmse = np.sqrt(np.square(np.subtract(df1['x'],trial)).mean())
print("RMSE error:",rmse)

plt.figure(figsize=(6, 6), dpi=200)
axes = plt.gca()
axes.plot(x,trial, 'r-')
axes.plot(x,df1['x'], 'g-')
plt.show()

