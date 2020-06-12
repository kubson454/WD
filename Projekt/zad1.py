import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dane=pd.read_excel(r'C:\Users\Kuba\Desktop\Git\WD\Projekt\imiona.xlsx')

grupa = dane.groupby(['Rok', 'Plec']).agg({'Liczba':'sum'}).unstack()
                            
print(grupa)

wykres = grupa.plot.bar()
wykres.set_ylabel('liczba')
wykres.set_xlabel('rok')
plt.legend()
plt.title('liczba narodzin kobiet i mezczyzn w danym roku')
plt.show()