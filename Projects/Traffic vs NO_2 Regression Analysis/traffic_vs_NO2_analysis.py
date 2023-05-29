aq_id = 'NL10318'

qoi = 'NO2'

import pandas as pd
print(f"You've entered {qoi} as qoi and {aq_id} as the aq_id. "
      f"Here is some information about the air-quality measurement station with this id.")
pd.read_csv('datasets/aq_station_info.csv', index_col=['aq_id']).loc[[aq_id]]

import numpy as np
import pandas as pd

# next command ensures that plots appear inside the notebook
%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns  # also improves the look of plots
sns.set()
plt.rcParams['figure.figsize'] = 10, 5  # default hor./vert. size of plots, in inches
plt.rcParams['lines.markeredgewidth'] = 1  # to fix issue with seaborn box plots; needed after import seaborn

from sklearn.linear_model import LinearRegression  # for linear regression
from sklearn.cluster import KMeans  # for clustering
from sklearn.tree import DecisionTreeClassifier  # for decision tree mining
from sklearn.metrics import accuracy_score, confusion_matrix, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from treeviz import tree_print  # to print decision tree

df_data = pd.read_csv('datasets/all_data.csv',
                      header=[0, 1],
                      parse_dates=[0],
                      index_col=[0])
df_data.index = df_data.index.tz_convert('Europe/Amsterdam')

df_aq = df_data[[(qoi, aq_id)]].copy()
df_aq.columns = [qoi]
df_ratings = pd.read_csv('datasets/ratings.csv',
                         index_col=['rating'])
df_aq[f'{qoi} rating'] = pd.cut(df_aq[qoi],
                                bins=df_ratings[qoi],
                                labels=False)

df_traffic = df_data['traffic'].shift(-1).copy()
df_weather = df_data['weather'].copy()

df_data = pd.concat([df_aq,
                     df_traffic,
                     df_weather],
                    axis=1)

df_data['date_part'] = df_data.index.floor('D')
df_data['year'] = df_data.index.year
df_data['month'] = df_data.index.month
df_data['weekday'] = df_data.index.weekday
df_data['hour'] = df_data.index.hour
df_data['day_of_year'] = df_data.index.dayofyear
df_data['week'] = df_data['day_of_year']//7 + 1
df_data.head(42300)

options = ['2020']
df_year2020 = df_data.loc[df_data['year'].isin(options)]

optionsweek = ['3', '4']
df_excerpt = df_year2020.loc[df_year2020['week'].isin(optionsweek)]

#df_excerpt.head(100)
fig, ax = plt.subplots(nrows=3, ncols=1, squeeze=False, sharex=True, figsize=(10, 10))
df_excerpt['nr_of_vehicles'].plot(marker="o", linestyle='', ax=ax[0,0])
df_excerpt['temperature (degreesC)'].plot(marker="o", linestyle='', ax=ax[1,0])
df_excerpt['NO2'].plot(marker="o", linestyle='', ax=ax[2,0]);

ax[0,0].set_title('Number of vehicles')
ax[1,0].set_title('Temperature (degrees C)')
ax[2,0].set_title('NO2')
ax[0,0].set_ylabel('Vehicles')
ax[1,0].set_ylabel('Temperature')
ax[2,0].set_ylabel('Concentration NO2')

fig.suptitle('Differences due to COVID-19', weight='bold')

df_middle = df_data[((df_data['day_of_year'] >= 72) & (df_data['day_of_year'] < 132))]

fig, ax = plt.subplots(nrows=2, ncols=1, squeeze=False, sharex=True, figsize=(10, 10))
sns.violinplot(data=df_middle, x='year', y='nr_of_vehicles', ax=ax[0,0]);
sns.violinplot(data=df_middle, x='year', y='NO2', ax=ax[1,0]);

ax[0,0].set_title('Number of vehicles')
ax[1,0].set_title('Average Concentration of NO2')

ax[0,0].set_ylabel('Vehicles')
ax[1,0].set_ylabel('Concentration')


fig.suptitle('Cars per hour and avg concentration NO2 from 72nd to 132nd (non-inclusive)', weight='bold')
plt.savefig('violinplots.pdf')

df_middlenot2020 = df_data[(df_data['year'] != 2020) & ((df_data['day_of_year'] >= 72) & (df_data['day_of_year'] < 132))]

df_middle2020 = df_data[((df_data['year'] == 2020) & ((df_data['day_of_year'] >= 72) & (df_data['day_of_year'] < 132)))]

lockdown_traffic = df_middle2020['nr_of_vehicles'].mean()
comparison_traffic = df_middlenot2020['nr_of_vehicles'].mean()

diff_traffic = comparison_traffic - lockdown_traffic
diff_traffic


df_middle2020 = df_data[((df_data['year'] == 2020) & ((df_data['day_of_year'] > 71) & (df_data['day_of_year'] < 132)))]

df_middlenot2020 = df_data[(df_data['year'] < 2020) & ((df_data['day_of_year'] > 71) & (df_data['day_of_year'] < 132))]


lockdown_QoI = df_middle2020['NO2'].mean()
comparison_QoI = df_middlenot2020['NO2'].mean()

diff_QoI = comparison_QoI - lockdown_QoI
diff_QoI


df_yearnot2020 = df_data[(df_data['year'] < 2020)]

standard_dev_QoI = df_yearnot2020['NO2'].std()
#standard_dev_QoI
ratio_QoI = diff_QoI/standard_dev_QoI
ratio_QoI

df_yearnot2020 = df_data[(df_data['year'] != 2020)]
group = df_yearnot2020.groupby(['year', 'month'])
groupstable = group.mean()

df_marchtomay = df_data[((df_data['date_part'] >= '2020-03-12') & (df_data['date_part'] <= '2020-05-10'))]
df_marchtomay['NO2'].mean()

groupstable['NO2'].min()
year_aq_low = 2016
month_aq_low = 7

df_yearnot2020 = df_data[(df_data['year'] != 2020)]
group = df_yearnot2020.groupby(['year', 'month'])
groupstable = group.mean()

df_marchtomay = df_data[((df_data['date_part'] >= '2020-03-12') & (df_data['date_part'] <= '2020-05-10'))]
#df_marchtomay['nr_of_vehicles'].mean()
#groupstable['nr_of_vehicles'].min()

year_traffic_low = 'lockdown'
month_traffic_low = 'lockdown'

fig, ax = plt.subplots(nrows=1, ncols=2, squeeze=False, sharey=True, figsize=(20, 10))
df_data.plot(kind='scatter', x='temperature (degreesC)', y=['NO2'], alpha=0.5,  ax=ax[0,0])
df_data.plot(kind='scatter', x='average_wind_speed(m/s)', y=['NO2'], alpha=0.5,  ax=ax[0,1])


ax[0,0].set_ylabel('NO2 Concentration')


fig.suptitle('How Temperature and Average wind speed affect NO2', weight='bold')

df_training = df_data[df_data['year']<2019].dropna().copy()
df_2019 = df_data[df_data['year']==2019].dropna().copy()
df_2020 = df_data[df_data['year']==2020].dropna().copy()

X_reg_train = df_training[['nr_of_vehicles', 'temperature (degreesC)']].copy()  # independent variable; just one column in this case
y_reg_train = df_training[['NO2']].copy()  # dependent variable; just one column

X_reg_test2019 = df_2019[['nr_of_vehicles', 'temperature (degreesC)']].copy()  # independent variable; just one column in this case
X_reg_test2020 = df_2020[['nr_of_vehicles', 'temperature (degreesC)']].copy()
y_reg_test2019 = df_2019[['NO2']].copy()  # dependent variable; just one column
y_reg_test2020 = df_2020[['NO2']].copy()

reg = LinearRegression()

reg.fit(X_reg_train, y_reg_train)

#reg.intercept_, reg.coef_

ax = sns.regplot(X_reg_train['temperature (degreesC)'], y_reg_train['NO2'], ci=None);
ax.legend(['trained model', 'training data'])
ax.set_title("Linear model predicting 'NO2' from 'Temperature C' in the example data set");


df_2019['NO2_predicted'] = reg.predict(df_2019[['nr_of_vehicles', 'temperature (degreesC)']])
df_2019[['NO2', 'NO2_predicted']]

evaluation_QoI_2019 = mean_absolute_error(y_reg_test2019, df_2019['NO2_predicted'])

df_2020['NO2_predicted'] = reg.predict(df_2020[['nr_of_vehicles', 'temperature (degreesC)']])

evaluation_QoI_2020 = mean_absolute_error(y_reg_test2020, df_2020['NO2_predicted'])

evaluation_QoI_2019

hypothesis = 'If we make linear regression models to see the correlation of traffic data on the NO2 concentration in the air then we will see that there is no effective correlation between the two because the amount of cars on the road is shown in regression models to not have a strong effect on the amount of NO2 in the air.'

df_training = df_data[df_data['year']<2019].dropna().copy()
#groupweek = df_training.groupby(['weekday'])

#sns.boxplot(data=df_training, x='nr_of_vehicles', y='NO2');

#sns.violinplot(data=df_data, x='weekday', y='NO2');

###
X_reg_train = df_training[['nr_of_vehicles', 'temperature (degreesC)']].copy()  # independent variable; just one column in this case
y_reg_train = df_training[['NO2']].copy()  # dependent variable; just one column

X_reg_test2019 = df_2019[['nr_of_vehicles', 'temperature (degreesC)']].copy()  # independent variable; just one column in this case
X_reg_test2020 = df_2020[['nr_of_vehicles', 'temperature (degreesC)']].copy()
y_reg_test2019 = df_2019[['NO2']].copy()  # dependent variable; just one column
y_reg_test2020 = df_2020[['NO2']].copy()

reg = LinearRegression()

reg.fit(X_reg_train, y_reg_train)

#reg.intercept_, reg.coef_

#regplot = sns.regplot(X_reg_train['nr_of_vehicles'], y_reg_train['NO2'], ci=None, line_kws={'color':'orange'});
#regplot.legend(['trained model', 'training data'])
#regplot.set_title("Linear model predicting 'NO2' from 'Number of vehicles' in the example data set", weight='bold');
###
#plt.savefig('regressioncars.pdf')

#regplot = sns.regplot(df_training['average_wind_speed(m/s)'], y_reg_train['NO2'], ci=None, line_kws={'color':'orange'});
#regplot.legend(['trained model', 'training data'])

#sns.stripplot(data=df_training, x='highest_wind_gust(m/s)', y='NO2');
df_trainingless2020 = df_data[df_data['year']<=2019].dropna().copy()

#fig, ax = plt.subplots(nrows=2, ncols=2, squeeze=False, figsize=(10,10))
#df_2019['weekday'].violinplot(data=df_2019, x='weekday', y='NO2')
#ax.violinplot(data=df_2020, x='weekday', y='NO2');
#plot = sns.plot(data=df_data, x='temperature (degreesC)', y='NO2')
#plot.set_title("Temperature (C) vs NO2 concentration in the air", weight='bold');
#plt.savefig('hourcarsallyearsnew.pdf')
ax = sns.regplot(df_data['temperature (degreesC)'], df_data['NO2'], ci=None, line_kws={'color':'orange'});
ax.legend(['trained model', 'training data'])
ax.set_title("Linear model predicting 'NO2' from 'Temperature C' in the example data set", weight='bold');
#plt.savefig('no2tempsnew.pdf')
#reg.score(X_mpg_train, y_mpg_train)