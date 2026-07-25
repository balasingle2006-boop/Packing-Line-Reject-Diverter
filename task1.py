import matplotlib.pyplot as plt

normal = [100,101,99,100,98,102,100]
low = [100,99,98,90,89,88,87]
noisy = [100,99,130,100,98,97,97,97]

plt.plot(normal, label="Normal")
plt.plot(low, label="Low Weight")
plt.plot(noisy, label="Noisy")

plt.legend()
plt.show()