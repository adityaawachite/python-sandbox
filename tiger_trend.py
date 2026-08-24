
import matplotlib.pyplot as plt

years = [2020, 2021, 2022, 2023, 2024, 2025, 2026]
population = [3200, 3440, 3682, 3750, 3810, 3880, 3950]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.plot(years, population, color='green', marker='o', linestyle='-', linewidth=2, markersize=8)
ax1.set_title('Tiger Population Trend (2020-2026)', fontsize=14)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Tigers', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)

ax2.bar(years, population, color='orange', edgecolor='black', width=0.6)
ax2.set_title('Tiger Population Count by Year', fontsize=14)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Number of Tigers', fontsize=12)
ax2.set_axisbelow(True)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
