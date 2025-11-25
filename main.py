

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")

print("Original Data Head:")
print(df.head())

df["date"] = pd.to_datetime(df["date"])


df = df.set_index("date")


df = df.sort_index()


df = df.interpolate().fillna(method="bfill").fillna(method="ffill")


df.to_csv("cleaned_weather.csv")
print("\nCleaned data saved as cleaned_weather.csv")

daily_stats = df.resample("D").mean()
monthly_stats = df.resample("M").mean()
yearly_stats = df.resample("Y").mean()

daily_stats.to_csv("daily_stats.csv")
monthly_stats.to_csv("monthly_stats.csv")
yearly_stats.to_csv("yearly_stats.csv")

print("Stats saved: daily_stats.csv, monthly_stats.csv, yearly_stats.csv")

plt.figure()
plt.plot(daily_stats.index, daily_stats["temperature"])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.tight_layout()
plt.savefig("plot_daily_temperature.png")
plt.close()

plt.figure()
plt.bar(monthly_stats.index.strftime("%Y-%m"), monthly_stats["rainfall"])
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plot_monthly_rainfall.png")
plt.close()

plt.figure()
plt.scatter(df["temperature"], df["humidity"], alpha=0.5)
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.tight_layout()
plt.savefig("plot_humidity_vs_temperature.png")
plt.close()

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(daily_stats.index, daily_stats["temperature"])
plt.title("Daily Temperature Trend")

plt.subplot(2, 1, 2)
plt.bar(monthly_stats.index.strftime("%Y-%m"), monthly_stats["rainfall"])
plt.title("Monthly Rainfall")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("plot_combined_subplots.png")
plt.close()

print("Plots saved successfully!")

df["month"] = df.index.month

def season(m):
    if m in [12, 1, 2]: return "Winter"
    if m in [3, 4, 5]: return "Summer"
    if m in [6, 7, 8]: return "Monsoon"
    return "Autumn"

df["season"] = df["month"].apply(season)

monthly_grouped = df.groupby("month").mean()
season_grouped = df.groupby("season").mean()

monthly_grouped.to_csv("grouped_by_month.csv")
season_grouped.to_csv("grouped_by_season.csv")

print("Grouping completed!")
print("\nAll tasks completed successfully!")
print("Your required files are ready!")
