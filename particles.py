import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from celluloid import Camera

num = 100
resolution = 200
frames = 200
g = 1

particles = np.random.randint(0, resolution, [num, 2]).astype(float)
velocity = np.zeros([num, 2], dtype=float)

# canvas[np.ix_(*particles.T)] = 1

# print(np.mgrid[particles.T])

# plt.imshow(canvas)
# plt.show()

# plt.axis([0, 10, 0, 1])

center = [resolution / 2.] * 2
fig, ax = plt.subplots()
sequence = []

camera = Camera(fig)
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

    frame = ax.imshow(canvas, animated=True)
    sequence.append([frame])
    camera.snap()
    print('Rendered frame {}'.format(i+1))

    # plt.clf()
    # plt.imshow(canvas)
    # plt.pause(0.01)
    # plt.axis('off')

# plt.show()

ani = animation.ArtistAnimation(fig, sequence, interval=10, blit=True, repeat_delay=0)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#

# writer = animation.FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# writer = PillowWriter(fps=20, codec='libx264', bitrate=20)
# writer.setup(fig, "./test-movie.gif", dpi=100)
# ani.save("test-movie.gif", writer=writer, dpi=100)

anim = camera.animate()
anim.save('animation.gif', writer='PillowWriter', fps=20, dpi=100, bitrate=10000)

# plt.show()
