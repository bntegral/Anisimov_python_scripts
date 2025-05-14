import numpy as np
from matplotlib import pyplot, ticker

fig, ax = pyplot.subplots(figsize=(10, 6), dpi=200, layout='constrained')

y = [e * np.loadtxt("Lesson_6-8\settings.txt", dtype=float)[1] for e in np.loadtxt("Lesson_6-8\data.txt", dtype=float)[110:-50]]
x = np.arange(len(y)) / np.loadtxt("Lesson_6-8\settings.txt", dtype=float)[0]
pyplot.xlabel('Время, c')
pyplot.ylabel('Напряжение, В')
pyplot.plot(x, y, color='purple', label='U(t)')
pyplot.legend()
ax.text(50.3, 1.01, f'Время заряда: {np.round(len(y[:np.argmax(y) + 1]) / np.loadtxt("Lesson_6-8\settings.txt", dtype=float)[0], 2)}c,\nВремя разряда {np.round(len(y[np.argmax(y) + 1:]) / np.loadtxt("Lesson_6-8\settings.txt", dtype=float)[0], 2)} c', size=7)
pyplot.grid(True, which='minor', color='gray', linestyle=':', alpha=0.7)
pyplot.grid(True, which='major', color='black', linestyle='-', alpha=0.8, linewidth=0.5)
ax = pyplot.gca()
ax.set_xlim([0, 66])
ax.set_ylim([0.45, max(y)+0.025])
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MaxNLocator(28))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MaxNLocator(33))
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке", loc='center', wrap=True)
pyplot.scatter([x[i] for i in range(0, len(y), 70)], [y[i] for i in range(0, len(y), 70)], marker='s', color='pink', linewidths=0.9, zorder=2)
fig.savefig('Lesson_6-8\\figure.svg')
pyplot.show()