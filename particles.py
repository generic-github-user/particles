import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from celluloid import Camera

num = 1000
resolution = 200
frames = 20
g = 1
center = [resolution / 2.] * 2

particles = np.random.uniform(0, resolution, [num, 2]).astype(float)
# velocity = np.zeros([num, 2], dtype=float)
offset = np.zeros_like(particles)
for j in range(num):
    p = particles[j]
    d = center - p
    # r = np.clip(np.linalg.norm(d), 5, 10e3)
    offset[j] = d

# np.ones([num, 2], dtype=float)
velocity = -np.flip(np.clip(offset, -10e3, 10e3)) * 0.02

# canvas[np.ix_(*particles.T)] = 1

# print(np.mgrid[particles.T])
# plt.axis([0, 10, 0, 1])

fig, ax = plt.subplots()
sequence = []

camera = Camera(fig)
for i in range(frames):
    for j in range(num):
        p = particles[j]
        d = center - p
        # Calculate distance between point and target
        r = np.clip(np.linalg.norm(d), 5, 10e3)
        # Adjust velocity based on force of gravity
        velocity[j] += d * (g / (r ** 2))
    # print(velocity[j], d * (g / (r ** 2)))
        # particles[j] += velocity[j]

    particles += velocity
    # particles = particles % resolution
    # Limit particle locations to visible frame
    particles = np.clip(particles, 0, resolution-1)

    canvas = np.zeros([resolution]*2)
    # canvas[np.arange(canvas.shape[0])[:, None], particles.astype(int)] = 1
    for j in range(num):
        # Convert the particle location to an index on the image grid
        p = particles[j].astype(int)
        index = tuple(p)
        # Use particle velocity as color
        canvas[index] = np.linalg.norm(velocity[j]) + 1

    frame = ax.imshow(canvas, animated=True)
    sequence.append([frame])
    # Capture the current frame for rendering
    camera.snap()
    print('Rendered frame {}'.format(i+1))

ani = animation.ArtistAnimation(fig, sequence, interval=10, blit=True, repeat_delay=0)

# writer = animation.FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# writer = PillowWriter(fps=20, codec='libx264', bitrate=20)
# writer.setup(fig, "./test-movie.gif", dpi=100)
# ani.save("test-movie.gif", writer=writer, dpi=100)

anim = camera.animate()
anim.save('animation.gif', writer='PillowWriter', fps=20, dpi=100, bitrate=10000)

# plt.show()
