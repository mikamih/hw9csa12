import pandas as pd

dict1 = {'Ten': ['Thanh pho Ha Noi', 'Tinh Ha Giang', 'Tinh Cao Bang'], 'cap':['Thanh pho Trung uong', 'Tinh', 'Tinh'], 'vung':['Dong bang', 'Dong bang', 'Dong bang'], 'dien tich':[3358.6, 7929.5, 6700.3], 'dan so (nghin nguoi)':[8093.9, 858.1, 530.9]}
df1 = pd.DataFrame(data= dict1)
print(df1)
print(type(df1))
