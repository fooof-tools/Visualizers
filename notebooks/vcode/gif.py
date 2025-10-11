"""Gif related functions."""

import time
from IPython.display import clear_output

import matplotlib.pyplot as plt

###################################################################################################
###################################################################################################

def savefig(fig, save, build_ind, label, folder='outputs', close=True):
    """Helper function for saving out a figure."""

    if save:
        fig.savefig(folder + '/' + label + '/gif_' + str(build_ind),
                    bbox_inches="tight", transparent=True, dpi=300)

    if close:
        plt.close()


def animate_plot(fig, save, build_ind, label='fig', sleep=0.01, folder='outputs'):
    """Helper function for showing and/or saving out gif images."""

    if save:
        savefig(fig, save, build_ind, label, folder, close=True)
    else:
        plt.show();
        time.sleep(sleep)
