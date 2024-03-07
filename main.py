import sys
from matplotlib.animation import FuncAnimation
from getsvg import *
from fourierseries import *
from draw import *


def main(path, order, show=True):
    pts = fromsvg(path)
    coeff = computeCoeff(pts, order)
    fig, ax, epi, Pointlist, Circlelist, Thetalist = processpath(coeff)
    if(show == False):
        hidefig(Pointlist, Circlelist)
    ani = FuncAnimation(fig, update, interval=1, blit=False, repeat=True, frames=361, fargs=[ax, epi, Pointlist, Circlelist, Thetalist])

    ani.save('./N=200.gif', writer='pillow', fps=30)

    plt.show()

    
if __name__ == "__main__":

    path = "Examples\pi1.svg"
    order = 200
    main(path, order, True)  
