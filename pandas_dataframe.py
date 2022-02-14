#converting an array to pandas df
df=pd.DataFrame(numpy_array,columns=['col1'])

#joining two pandas dataframes
df2=df.join(df1,on=['joining_column',how='left'])