import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Cell2
df = pd.read_csv(r"assignment2data.csv", index_col=None)

# Cell3
electric_power_df = df[df['Series Name'] == 'Electric power consumption (kWh per capita)']
selected_years = [str(year) for year in range(1998, 2015, 3)]
electric_power_years_df = electric_power_df[['Country Name'] + selected_years]

melted_df = pd.melt(electric_power_years_df, id_vars='Country Name', var_name='Year', value_name='Electric Power Consumption')

plt.figure(figsize=(8, 5))  # Adjusted size
sns.barplot(x='Year', y='Electric Power Consumption', hue='Country Name', data=melted_df, dodge=True, palette='viridis', edgecolor='w', linewidth=0.5)
plt.title('Electric Power Consumption (kWh per capita) by Country (1995-2014, 3-year intervals)')
plt.xlabel('Year')
plt.ylabel('Electric Power Consumption (kWh per capita)')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.gca().invert_yaxis()
plt.show()

# Cell4
df['Series Name'] = df['Series Name'].replace({
    'Ease of doing business score (0 = lowest performance to 100 = best performance)': 'Ease of doing business score',
    'Renewable energy consumption (% of total final energy consumption)': 'Renewable energy consumption'
})

selected_columns = ['Country Name', 'Series Name', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
selected_df = df[selected_columns]

china_df = selected_df[selected_df['Country Name'] == 'China']
correlation_df = china_df.set_index('Series Name').transpose()

correlation_df = correlation_df.replace('..', np.nan)
correlation_df = correlation_df.apply(pd.to_numeric, errors='coerce')
correlation_df = correlation_df.dropna(axis=1, how='all')
correlation_df = correlation_df.fillna(0)

correlation_matrix = correlation_df.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap for Series Name Values Over the Years (China)')
plt.show()

# Cell5
selected_columns = ['Country Name', 'Series Name', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
selected_df = df[selected_columns]

india_df = selected_df[selected_df['Country Name'] == 'India']
correlation_df = india_df.set_index('Series Name').transpose()

correlation_df = correlation_df.replace('..', np.nan)
correlation_df = correlation_df.apply(pd.to_numeric, errors='coerce')
correlation_df = correlation_df.dropna(axis=1, how='all')
correlation_df = correlation_df.fillna(0)

correlation_matrix = correlation_df.corr()

sns.set_theme(style='whitegrid')
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='viridis', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap for Series Name Values Over the Years (India)')
plt.show()

# Cell6
# Filter the DataFrame for the specific series
agricultural_land_df = df[df['Series Name'] == 'Agricultural land (sq. km)']

# Select years with a 5-year gap from 2000 to 2020
selected_years = [str(year) for year in range(2000, 2021, 5)]

# Filter the DataFrame for the selected years
agricultural_land_years_df = agricultural_land_df[['Country Name'] + selected_years]

# Melt the DataFrame to create a long format for seaborn
melted_df = pd.melt(agricultural_land_years_df, id_vars='Country Name', var_name='Year', value_name='Agricultural Land (sq. km)')

# Bar plot for Agricultural land
plt.figure(figsize=(12, 8))
sns.barplot(x='Year', y='Agricultural Land (sq. km)', hue='Country Name', data=melted_df, palette='viridis', edgecolor='w', linewidth=0.5)
plt.title('Agricultural Land (sq. km) by Country (2000-2020, 5-year intervals)')
plt.xlabel('Year')
plt.ylabel('Agricultural Land (sq. km)')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

# Reverse the y-axis to make bars rise from bottom to top
plt.gca().invert_yaxis()
plt.show()


# Cell7
# Set a dark color palette
sns.set_palette("dark")

# Set the style to darkgrid
sns.set(style="darkgrid")

selected_columns = ['Country Name', 'Series Name', '2000', '2005', '2010', '2015', '2020']
selected_df = df[selected_columns]

population_in_largest_city_df = selected_df[selected_df['Series Name'] == 'Population in largest city']
population_transposed = population_in_largest_city_df.set_index('Country Name').transpose()

population_transposed = population_transposed.replace('..', pd.NA)
population_transposed = population_transposed.apply(pd.to_numeric, errors='coerce')
population_transposed = population_transposed.dropna(axis=0, how='all')
population_transposed = population_transposed.fillna(0)

# Plotting line plot for Population in largest city with dark lines
plt.figure(figsize=(8, 5))  # Adjusted size
sns.lineplot(data=population_transposed, marker='o', linewidth=2, palette='dark')

plt.title('Population in Largest City by Country')
plt.xlabel('Year')
plt.ylabel('Population in Largest City')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# Cell8
# Select relevant columns
selected_columns = ['Country Name', 'Series Name', '2000', '2005','2010', '2015','2020']
selected_df = df[selected_columns]

# Filter for 'Renewable energy consumption'
renewable_energy_df = selected_df[selected_df['Series Name'] == 'Renewable energy consumption']

# Transpose the DataFrame to have 'Country Name' as rows and years as columns
renewable_energy_transposed = renewable_energy_df.set_index('Country Name').transpose()

# Replace '..' with NaN and convert to numeric
renewable_energy_transposed = renewable_energy_transposed.replace('..', pd.NA)
renewable_energy_transposed = renewable_energy_transposed.apply(pd.to_numeric, errors='coerce')

# Remove rows with all NaN values
renewable_energy_transposed = renewable_energy_transposed.dropna(axis=0, how='all')

# Fill NaN values with zeros (or you can choose another strategy)
renewable_energy_transposed = renewable_energy_transposed.fillna(0)

# Set a dark color palette for lines
dark_palette = sns.color_palette("dark", n_colors=renewable_energy_transposed.shape[1])

# Plotting line plot for Renewable energy consumption with dark lines
plt.figure(figsize=(12, 8))
sns.lineplot(data=renewable_energy_transposed, marker='o', palette=dark_palette)

plt.title('Renewable Energy Consumption (% of total final energy consumption) by Country')
plt.xlabel('Year')
plt.ylabel('Renewable Energy Consumption (%)')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()