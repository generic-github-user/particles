import numpy as np
import matplotlib.pyplot as plt

num = 1000
resolution = 200
frames = 200

particles = np.random.randint(0, resolution, [num, 2]).astype(float)
velocity = np.zeros([num, 2], dtype=float)

# canvas[np.ix_(*particles.T)] = 1

# print(np.mgrid[particles.T])

# plt.imshow(canvas)
# plt.show()

# plt.axis([0, 10, 0, 1])

center = [resolution / 2.] * 2
g = 1

for i in range(frames):
    for j in range(num):
        p = particles[j]
        d = center - p
        r = np.clip(np.linalg.norm(d), 5, 10e3)
        velocity[j] += d * (g / (r ** 2))
        # particles[j] += velocity[j]

    particles += velocity
    particles = particles % resolution

    canvas = np.zeros([resolution]*2)
    # canvas[np.arange(canvas.shape[0])[:, None], particles.astype(int)] = 1
    for j in range(num):
        p = particles[j].astype(int)
        index = tuple(p)
        canvas[index] = 1

    plt.clf()
    plt.imshow(canvas)
    plt.pause(0.01)
    plt.axis('off')

plt.show()
