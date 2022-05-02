import pandas as pd
import numpy as np

df = pd.read_csv("unemployment_data_us.csv")

print(df)

dict = {}

def appendDict(dict, rowValue, colName):
    dict[rowValue][colName].append(row[colName])

for index, row in df.iterrows():
    currYear = row["Year"]
    if row["Year"] != 2020:
        if row["Year"] not in dict:
            dict[row["Year"]] = {"Primary_School" : [row["Primary_School"]],
            "High_School" : [row["High_School"]],
            "Associates_Degree" : [row["Associates_Degree"]],
            "Professional_Degree" : [row["Professional_Degree"]],
            "White" : [row["White"]],
            "Black" : [row["Black"]],
            "Asian" : [row["Asian"]],
            "Hispanic" : [row["Hispanic"]],
            "Men" : [row["Men"]],
            "Women" : [row["Women"]]}
        else:
            dict[currYear]["Primary_School"].append(row["Primary_School"])
            dict[row["Year"]]["High_School"].append(row["High_School"])
            dict[row["Year"]]["Associates_Degree"].append(row["Associates_Degree"])
            dict[row["Year"]]["Professional_Degree"].append(row["Professional_Degree"])
            dict[row["Year"]]["White"].append(row["White"])
            dict[row["Year"]]["Black"].append(row["Black"])
            appendDict(dict, currYear, "Asian")
            appendDict(dict, row["Year"], "Hispanic")
            appendDict(dict, row["Year"], "Men")
            appendDict(dict, row["Year"], "Women")

print(dict)

for year in dict.keys():
    for typeOfUnemployment in dict[year].keys():
        dict[year][typeOfUnemployment] = np.mean(dict[year][typeOfUnemployment])

#print(dict)
#14.84167

newDF = pd.DataFrame(dict)
newDF = newDF.T

print(newDF["Primary_School"])

newDF.to_csv("new_unemployment_data.csv")  

#print(dict[2010]["Primary_School"])
print(newDF)


    

