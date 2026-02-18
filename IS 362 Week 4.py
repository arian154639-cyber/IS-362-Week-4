import pandas as pd
DataFrame = pd.read_csv("C:/Users/sharf/Downloads/IS_362_Week4_CSV.csv")
print(DataFrame)
ALASKA_LA = DataFrame.iloc[1, 2]
ALASKA_PH = DataFrame.iloc[1, 3]
ALASKA_SD = DataFrame.iloc[1, 4]
ALASKA_SF = DataFrame.iloc[1, 5]
ALASKA_SE = DataFrame.iloc[1, 6]
AM_WEST_LA = DataFrame.iloc[4, 2]
AM_WEST_PH = DataFrame.iloc[4, 3]
AM_WEST_SD = DataFrame.iloc[4, 4]
AM_WEST_SF = DataFrame.iloc[4, 5]
AM_WEST_SE = DataFrame.iloc[4, 6]
ALASKA_DELAYS_MEAN = DataFrame.iloc[1, [2, 3, 4, 5, 6]].mean()
AM_WEST_DELAYS_MEAN = DataFrame.iloc[4, [2, 3, 4, 5, 6]].mean()
ALASKA_DELAYS_MEDIAN = DataFrame.iloc[1, [2, 3, 4, 5, 6]].median()
AM_WEST_DELAYS_MEDIAN = DataFrame.iloc[4, [2, 3, 4, 5, 6]].median()

if ALASKA_LA > AM_WEST_LA:
    print("America West Airlines had less delays at Los Angeles.")
elif ALASKA_LA < AM_WEST_LA:
    print("Alaska Airlines had less delays at Los Angeles.")

if ALASKA_PH > AM_WEST_PH:
    print("America West Airlines had less delays at Phoenix.")
elif ALASKA_PH < AM_WEST_PH:
    print("Alaska Airlines had less delays at Phoenix.")

if ALASKA_SD > AM_WEST_SD:
    print("America West Airlines had less delays at San Diego.")
elif ALASKA_SD < AM_WEST_SD:
    print("Alaska Airlines had less delays at San Diego.")

if ALASKA_SF > AM_WEST_SF:
    print("America West Airlines had less delays at San Francisco.")
elif ALASKA_SF < AM_WEST_SF:
    print("Alaska Airlines had less delays at San Francisco.")

if ALASKA_SE > AM_WEST_SE:
    print("America West Airlines had less delays at Seattle.")
elif ALASKA_SE < AM_WEST_SE:
    print("Alaska Airlines had less delays at Seattle.")

if ALASKA_DELAYS_MEAN> AM_WEST_DELAYS_MEAN:
    print("America West Airlines had less delays on average.")
elif ALASKA_DELAYS_MEAN < AM_WEST_DELAYS_MEAN:
    print("Alaska Airlines had less delays on average.")

if ALASKA_DELAYS_MEDIAN > AM_WEST_DELAYS_MEDIAN:
    print("America West Airlines a had lower median delay.")
elif ALASKA_DELAYS_MEDIAN < AM_WEST_DELAYS_MEDIAN:
    print("Alaska Airlines had a lower median delay.")

print("This analysis shows that, on average, Alaska Airlines has less delays and a lower median delay. Alaska Airlines had less delays at Los Angeles, Phoenix, San Diego, and San Franciso. America West Airlines had less delays at Seattle. In conclusion, if you are flying to Seattle, you should choose America West Airlines. If you plan on flying to Los Angeles, Phoenix, San Francisco, or San Diego, you should choose Alaska Airlines.")
