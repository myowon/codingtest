import pandas as pd

def answer_two():
    path = 'C:/Users/pc/OneDrive/Desktop/q3/world_bank2020.csv'
    GDP_df = pd.read_csv(path, skiprows=4)
    GDP_df = GDP_df.filter(regex='(Country Name|20(1[1-9]|20))', axis=1)
    GDP_df = GDP_df.set_index('Country Name')
    GDP_df = GDP_df.rename(columns={"Country Name": "Country"})
    GDP_df = GDP_df.rename(index= {"Korea, Rep.":"South Korea","Iran, Islamic Rep.":"Iran", 
                                   "Hong Kong SAR, China": "Hong Kong"})
    return GDP_df

answer_two()
