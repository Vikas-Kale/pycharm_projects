from pandas import DataFrame
df=DataFrame.from_dict({'data0':{'a':0,'b':'A'}
                        'data1':{'a':1,'b':'B'}
                        },orient='index')
print(df)