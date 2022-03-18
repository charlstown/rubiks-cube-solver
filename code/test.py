import matplotlib.pyplot as plt
import numpy as np

ax = []
ay = []
bx = []
by = []
num = 0
plt.ion()
# plt.rcParams['savefig.dpi'] = 200
# plt.rcParams['figure.dpi'] = 200
plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 0.5
while num < 100:
    plt.clf()
    plt.suptitle("TITLE", fontsize=30)
    g1 = np.random.random()

    ax.append(num)
    ay.append(g1)
    agraphic = plt.subplot(2, 1, 1)
    agraphic.set_title('TABLE1')
    agraphic.set_xlabel('x', fontsize=10)
    agraphic.set_ylabel('y', fontsize=20)
    plt.plot(ax, ay, 'g-')
    # table2
    bx.append(num)
    by.append(g1)
    bgraghic = plt.subplot(2, 1, 2)
    bgraghic.set_title('TABLE2')
    bgraghic.plot(bx, by, 'r^')

    plt.pause(0.4)
    if num == 15:
        plt.savefig('picture.png', dpi=300)
        # break
    num = num + 1

plt.ioff()
plt.show()