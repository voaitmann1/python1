import numpy as np

A = np.array([
    [12.0, -51.0, 4.0],
    [6.0, 167.0, -68.0],
    [-4.0, 24.0, -41.0]
])

Q, R = np.linalg.qr(A)

print "������� Q:"
print Q

print "\n������� R:"
print R
