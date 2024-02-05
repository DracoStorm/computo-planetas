import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def update_plot(frame, p1, p2, line1, line2, scatter1, scatter2):
    line1.set_data(p1[:frame, 0], p1[:frame, 1])
    line2.set_data(p2[:frame, 0], p2[:frame, 1])
    scatter1.set_offsets(p1[frame, :])
    scatter2.set_offsets(p2[frame, :])
    return line1, line2, scatter1, scatter2


def plot_animation(t, p1, p2, N):
    fig, ax = plt.subplots()
    line1, = ax.plot(p1[0], p2[0], 'k', label='trajectory_planet_1')
    line2, = ax.plot(p1[0], p2[0], 'b', label='trajectory_planet_2')
    scatter1 = ax.scatter(p1[0], p2[0], c='k', marker='o', label='planet_1')
    scatter2 = ax.scatter(p1[0], p2[0], c='b', marker='o', label='planet_2')

    ax.grid(True)
    ax.set(xlim=[0.1, 0.4], ylim=[0.1, 0.2],
           xlabel='Distance [x]', ylabel='Distance [y]')
    ax.legend()
    ani = FuncAnimation(fig=fig, func=update_plot, frames=N, fargs=(
        p1, p2, line1, line2, scatter1, scatter2), interval=30, blit=True)

    plt.show()
