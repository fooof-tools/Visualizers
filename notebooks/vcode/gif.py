"""Gif related functions."""

import time
from IPython.display import clear_output

import matplotlib.pyplot as plt

###################################################################################################
###################################################################################################

def animate_plot(fig, save, build_ind, label='fig', sleep=0.01, folder='outputs'):
    """Helper function for showing and/or saving out gif images."""

    if save:
        fig.savefig(folder + '/' + label + '/gif_' + str(build_ind), bbox_inches="tight", dpi=300)
        plt.close()
    else:
        plt.show();
        time.sleep(sleep)
