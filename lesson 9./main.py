import pandas as pd
import matplotlib.pyplot as mat

table = pd.read_csv("/Users/jaanvikalarikkal/Desktop/data science/lesson 9./sp500_top10_stocks_clean.csv")
print(table)
table.info()
#to see average adjusted price for each company overall (all the years)

tick = table.groupby("Ticker")["Adj_Close"].mean()
print(tick)

mat.bar(tick.index, tick)
mat.title('S and P adjisted prices')
mat.show()
