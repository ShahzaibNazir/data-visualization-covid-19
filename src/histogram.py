import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.express as px

def histoGram_of_covid(dataset,cases, deaths, colors):
    plt.figure(figsize=(10,10))
    fig = px.histogram(dataset, x=cases, y=deaths, color=colors,
                       marginal="box")
    fig.show()


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
    histoGram_of_covid(df,testCases,testDeaths,testcolors)


if __name__ == "main":
    main()



