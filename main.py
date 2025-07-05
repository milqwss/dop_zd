import matplotlib.pyplot as plt
import numpy as np

mas = []
x = 0
while x <= 2 * np.pi:
    mas.append(round(x, 2))
    x += 0.01

arrx = np.array(mas, dtype='float16')
arry = np.exp(arrx)

plt.plot(arrx, arry, color='red', linewidth=2)
plt.xlabel('Ось x', labelpad=10, fontsize='10', color='brown')
plt.ylabel('Ось y', labelpad=10, fontsize='10', color='brown')
plt.title('График экспоненты (y = e^x)', pad=10, fontsize='20')
plt.grid(True)
plt.show()