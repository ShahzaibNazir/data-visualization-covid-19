import pandas as pd
import plotly.express as px

def frequencyGraph_dates(dataset,dates, cases):
    figg = px.line(dataset, x=dates, y=cases)
    figg.show()

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
    frequencyGraph_dates(df,testDates,testCases)

if __name__ == "main":
    main()



