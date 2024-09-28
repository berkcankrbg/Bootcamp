import pandas as pd
import matplotlib.pyplot as plt

#csv dosyasını yükleme
df = pd.read_csv('Housing (1).csv')

#Area scatter plot
plt.scatter(df['area'],df['price'])
plt.title('Ev Fiyatlarının Alan ile İlişkisi')
plt.xlabel('Alan')
plt.ylabel('Fiyat')
plt.grid()
plt.show()

#Bedrooms scatter plot
plt.scatter(df['bedrooms'],df['price'])
plt.title('Ev Fiyatlarının Yatak Odası ile İlişkisi')
plt.xlabel('Yatak Odası Sayısı')
plt.ylabel('Fiyat')
plt.grid()
plt.show()

#Stories scatter plot
plt.scatter(df['stories'],df['price'])
plt.title('Ev Fiyatlarının Kat Sayısı ile İlişkisi')
plt.xlabel('Kat Sayısı')
plt.ylabel('Fiyat')
plt.grid()
plt.show()

#Bathrooms ortalama fiyat
bathroom_ortalama = df.groupby('bathrooms')['price'].mean().reset_index()
plt.bar(bathroom_ortalama['bathrooms'].astype(str), bathroom_ortalama['price'])
plt.title('Ortalama Ev Fiyatları - Bathroom Sayısına Göre')
plt.xlabel('Bathroom Sayısı')
plt.ylabel('Ortalama Fiyat')
plt.show()

"""
chatgpt'den yardım almak zorunda kaldım ortalama fiyat kısmı için 
matrisi kendim yapamadım chat gpt'den direkt kopyalamak istemedim 

"""




