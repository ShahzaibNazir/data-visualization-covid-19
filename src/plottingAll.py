import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.express as px


def plot_cases_and_deaths(dataset,cases, deaths):
    plt.figure(figsize=(15,10))
    sn.relplot(x= cases, y=deaths, data = dataset, hue = cases)
    plt.xticks(rotation=45)
    plt.show()


def main():
    data = pd.read_csv("covid19.csv")
    df = data[["dateRep", "cases", "deaths", "color"]]
    dates = df['dateRep']
    cases = df["cases"]
    deaths = df['deaths']
    colors = df['color']

    testDates = dates[1:200]
    testCases = cases[1:200]
    testDeaths = deaths[1:200]
    testcolors = colors[1:200]

    # function calling
    plot_cases_and_deaths(df,testCases,testDeaths)

if __name__ == "main":
    main()


