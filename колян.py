import numpy as np
import matplotlib.pyplot as plt

# Определяем x
x = np.linspace(-np.pi, np.pi, 400)

# Функции
y1 = (np.pi / 2) * np.sin(x)
y2 = x

# Находим точку пересечения (приблизительно)
x_intersect = np.pi / 2  # Предполагаем, что пересечение около pi/2

# Создаем маску для выделения области до точки пересечения
mask = (x >= 0) & (x <= x_intersect) & (y2 >= y1)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$y = \frac{\pi}{2} \sin(x)$')
plt.plot(x, y2, label=r'$y = x$')

# Заполняем область
plt.fill_between(x, y1, y2, where=mask, color='gray', alpha=0.5)

# Настройки графика
plt.title(r'Область между $y = \frac{\pi}{2} \sin(x)$ и $y = x$')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-np.pi, np.pi)
plt.ylim(-np.pi, np.pi)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.show()
