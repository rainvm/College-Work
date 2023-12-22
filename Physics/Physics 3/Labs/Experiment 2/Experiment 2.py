import pandas as pd

import DataAnalysisTools as dat
import numpy as np

mu = 1.256637e-6
N = 142.0
I = []
I.append(np.array([1.1 + 0.5 * i for i in range(9)]))
I.append(np.array([1.3 + 0.5 * i for i in range(9)]))
I.append(np.array([1.85 + 0.5 * i for i in range(10)]))
I.append(np.array([1.55 + 0.5 * i for i in range(8)]))
rData = np.array([28.4, 28.5, 28.2, 28.3, 31.5, 31.0, 31.3, 31.0]) / 2
loop = [[10.5, 10, 9.6, 9.3, 8.9, 8.5, 8.4, 8.0, 7.6], [11, 10.7, 10.2, 9.9, 9.5, 9.2, 8.9, 8.6, 8.4],
        [10.6, 10.1, 9.8, 9.5, 9.3, 9.0, 8.7, 8.5, 8.4, 8.0], [9.3, 9.1, 9.0, 8.9, 8.6, 8.5, 8.3, 8.1]]
r = np.mean(rData)
dr = dat.totalUncertainty(rData, 0.1)
dloop = 0.05

print(dloop)
B = []
dB = []
for i in I:
    B.extend(np.divide((4.0 / 5.0) ** (3.0 / 2.0) * mu * N * i, r))
    dB.extend(i / r * np.sqrt((0.005 / i) ** 2 + (dr / r) ** 2))
print("Magnetic Field")
for i in range(len(B)):
    print(f'{B[i]:.3} ± {dB[i]:.3}')
V = np.array([200, 300, 400, 500])
dV = 2
dChargeToMass = []
chargeToMass = []
for i in range(4):
    chargeToMass.extend(2 * V[i] / ((np.array(loop[i]) * np.array(B[i])) ** 2))
    dChargeToMass.extend(V[i] / (r * np.array(B[i])) ** 2 * np.sqrt((dV / V[i]) ** 2 + (2 * dloop / np.array(loop[i])) ** 2))

print("Charge to mass ratio:")
for i in range(len(chargeToMass)):
    print(f'{chargeToMass[i]:.3} ± {dChargeToMass[i]:.3}')
