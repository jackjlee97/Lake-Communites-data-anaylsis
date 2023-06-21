import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

lake_comm_dataset = pd.read_csv(r"C:\\Users\\Owner\\OneDrive\\Documents\\Datasets\\dodsonlakecomm.csv")

lake_comm_dataset_dropna = lake_comm_dataset.dropna(subset=['primaryprod', 'phytoplankton', 'rotifers', 'crust_zooplankton',
       'cladocerans', 'copepods', 'macrophytes', 'fish'])
lake_comm_dataset_dropna.to_csv("lake_comm_dataset.dropna.csv")
print(lake_comm_dataset_dropna)

info = lake_comm_dataset_dropna.info()
print(info)

columns_headings = lake_comm_dataset_dropna.columns
print(columns_headings)

#data description
describe = lake_comm_dataset_dropna.describe()
print(describe)
(pandas.DataFrame(describe)).to_csv('lake_comm_dataset_dropna_description.csv', index=True)


# correlation between groups of organisms, create new data frame changing numerics to string
columns_int = ['area', 'primaryprod', 'phytoplankton', 'rotifers', 'crust_zooplankton',
       'cladocerans', 'copepods', 'macrophytes', 'fish']

correlation_lake_comm_dataset_dropna = lake_comm_dataset_dropna[columns_int].corr()
print(correlation_lake_comm_dataset_dropna)
correlation_dataframe = pandas.DataFrame(correlation_lake_comm_dataset_dropna)
correlation_dataframe.to_csv('correlation_lake_comm_dataset_dropna.csv', index=True)


def get_correlation_label(value):
    if value >= 0.8:
        return "Very High Positive Correlation"
    elif value >= 0.6:
        return "High Positive Correlation"
    elif value >= 0.4:
        return "Medium Positive Correlation"
    elif value >= 0.2:
        return "Low Positive Correlation"
    elif value >= 0.1:
        return "Very Low Positive Correlation"
    elif value >= -0.1:
        return "No Correlation"
    elif value >= -0.2:
        return "Very Low Negative Correlation"
    elif value >= -0.4:
        return "Low Negative Correlation"
    elif value >= -0.6:
        return "Medium Negative Correlation"
    elif value >= -0.8:
        return "High Negative Correlation"
    else:
        return "Very High Negative Correlation"

correlation_dataframe = correlation_dataframe.applymap(get_correlation_label)
print(correlation_dataframe)
correlation_dataframe.to_csv('correlation_lake_comm_dataset_dropna2.csv', index=True)

#average values by country, create stacked bar chart and save to file
lake_comm_dataset_dropna_country_mean = lake_comm_dataset_dropna.groupby("country", as_index=False)[columns_int].mean()
print(lake_comm_dataset_dropna_country_mean)

lake_comm_dataset_dropna_country_mean.plot(x = 'country', y = ['primaryprod', 'phytoplankton', 'rotifers', 'crust_zooplankton',
       'cladocerans', 'copepods', 'macrophytes', 'fish'], kind='bar', stacked=True)
plt.title("Country Organisms Means")
plt.xlabel("Country")
plt.ylabel("Organism groups Mean")

plt.savefig('stacked_bar_chart.png', dpi=300, bbox_inches='tight')

#scatter between lake size and number organisms community size
# Graphs add what metrics are needed
# x value
x_value = 'fish'
# y value
y_value = 'area'
#correllation coefficent
corr_coef = np.corrcoef(lake_comm_dataset[x_value],lake_comm_dataset[y_value])[0, 1]

lake_comm_dataset.plot.scatter(
    x= x_value,
    y= y_value
)
plt.title("Scatter plot of " + x_value +" and " + y_value)
plt.xlabel(x_value)
plt.ylabel(y_value)
plt.annotate('r = {:.2f}'.format(corr_coef), xy=(0.7, 0.9), xycoords='axes fraction')

plt.savefig('Scatter plot of ' + x_value + ' and ' + y_value + '.png', dpi=300, bbox_inches='tight')
