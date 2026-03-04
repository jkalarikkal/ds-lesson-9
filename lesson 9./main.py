import pandas as pd
import matplotlib.pyplot as mat

table = pd.read_csv("/Users/jaanvikalarikkal/Desktop/data science/lesson 9./sp500_top10_stocks_clean.csv")
print(table)
table.info()
#to see average adjusted price for each company overall (all the years)

tick = table.groupby("Ticker")["Adj_Close"].mean()
print(tick)

#mat.bar(tick.index, tick)
#mat.title('S and P adjisted prices')
#mat.show()


#to find mean of all the days for each company (high + low mean)

meanie = table.groupby("Ticker")[["High","Low"]].mean()


meanie["mean"] = (meanie["High"] + meanie["Low"])/2
print(meanie)

'''
mat.bar(meanie.index, meanie["mean"])
mat.title("Means of the companies")
mat.show()
'''

#best performing day for each company 

lampie = table.groupby("Ticker")["Adj_Close"].idxmax()
print(lampie)

# bob = table.loc[lampie]
# print(bob)


# mat.scatter(bob["Ticker"], bob["Adj_Close"], color = "red", label = "ended close")
# mat.scatter(bob["Ticker"], bob["High"], color = "blue", label = "highest" )
# mat.legend()
# mat.title("Comaprisons of company volatility")
# mat.show()


#lowest 'low' of every company 

lowey = table.groupby("Ticker")["Low"].min()
mat.bar(lowey.index, lowey)
mat.title("Lowest of the low", color = "red")
mat.show()
