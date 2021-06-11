import numpy as np
import matplotlib.pyplot as plt

particles = np.random.randint(0, 100, [100, 2])
canvas = np.zeros([100, 100])
# canvas[np.ix_(*particles.T)] = 1
canvas[np.arange(canvas.shape[0])[:, None], particles] = 1
# print(np.mgrid[particles.T])
plt.imshow(canvas)
plt.show()
