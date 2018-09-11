import pandas as pd
import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')
csv_dataframe = pd.read_csv('01-0.csv')
#first_10_lines = pd.read_csv('01-0.csv')[0:10]

writer = pd.ExcelWriter('01-0.xlsx', engine='xlsxwriter')

workbook = writer.book

chart = workbook.add_chart({'type':'line'})
#chart.set_x_axis('name':'pixels')
#chart.set_y_axis('name':'Intensity')


intensity_data = csv_dataframe.Col
## range_data = csv_dataframe.Range
# Raage, Col, Row , Intensity
range_data = csv_dataframe.Range

t_intensity_data = intensity_data[0:1000]
t_range_data = range_data[0:1000]

print(t_intensity_data)
print(t_range_data)
#first_column = ufo.loc[:,1]


plt.plot(t_intensity_data, t_range_data,'bo', color='green')
plt.show()
