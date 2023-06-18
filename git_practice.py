import matplotlib.pyplot as plt

input_values=list(range(0,101,2))
squares=[value**2 for value in range(0,101,2)]
fig, ax=plt.subplots()
ax.plot(input_values,squares, linewidth=3)

plt.show()