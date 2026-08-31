
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sells_report.CSV')
last_5_years = df.nlargest(5, 'Year').sort_values('Year')

plt.figure(figsize=(10, 6))
plt.plot(last_5_years['Year'], last_5_years['Mango'], label='Mango', marker='o')
plt.plot(last_5_years['Year'], last_5_years['Orange'], label='Orange', marker='s')

plt.title('Mango vs Orange Sales (Last 5 Years)')
plt.xlabel('Year')
plt.ylabel('Sales Volume')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
