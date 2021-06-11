import numpy as np
import matplotlib.pyplot as plt

particles = np.random.randint(0, 100, [100, 2]).astype(float)
velocity = np.zeros([100, 2], dtype=float)

# canvas[np.ix_(*particles.T)] = 1

# print(np.mgrid[particles.T])

# plt.imshow(canvas)
# plt.show()

# plt.axis([0, 10, 0, 1])

center = [50.] * 2
g = 1

for i in range(200):
    for j in range(100):
        p = particles[j]
        d = center - p
        r = np.clip(np.linalg.norm(d), 5, 10e3)
        velocity[j] += d * (g / (r ** 2))
        # particles[j] += velocity[j]

    particles += velocity
    particles = particles % 100

    canvas = np.zeros([100, 100])
    # canvas[np.arange(canvas.shape[0])[:, None], particles.astype(int)] = 1
    for j in range(100):
        p = particles[j].astype(int)
        index = tuple(p)
        canvas[index] = 1

    plt.clf()
    plt.imshow(canvas)
    plt.pause(0.01)
    plt.axis('off')

plt.show()
