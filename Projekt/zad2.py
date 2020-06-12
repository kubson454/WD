import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dane=pd.read_excel(r'C:\Users\Kuba\Desktop\Git\WD\Projekt\imiona.xlsx')

grupa = (dane.groupby(['Rok']).sum())
print(grupa)

grupa['roznica'] = round(((grupa.Liczba - grupa.Liczba.shift(1)) / grupa.Liczba * 100 ),1)

wykres = grupa.plot(y="roznica", kind="bar")
wykres.set_ylabel('roznica w %')
wykres.set_xlabel('rok')
plt.title('dynamika narodzin w latach 2000-2017')
plt.show()

