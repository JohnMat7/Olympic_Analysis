import pandas as pd

# df = pd.read_csv('athlete_events.csv') 
# # region = pd.read_csv('noc_regions.csv')



def preprocess(df,region):
    # global df,region
    #filtering for summer olympics
    df = df[df['Season']=='Summer']
    #merge with region file
    df = df.merge(region,on='NOC',how='left')
    #dropping duplicates
    df.drop_duplicates(inplace=True)
    #one hot endcoding + concatination
    df = pd.concat([df, pd.get_dummies(df['Medal'])],axis=1)
    return df