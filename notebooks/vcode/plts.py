"""Plot functions for the specparam visualizers."""

import numpy as np

from fooof.plts.utils import check_ax

###################################################################################################
###################################################################################################

def plot_spectra(freqs, powers, log_freqs=True, log_powers=True,
                 ylim=None, ax=None, **plt_kwargs):
    """Plot power spectra."""

    ax = check_ax(ax)

    if log_freqs:
        freqs = np.log10(freqs)

    if log_powers:
        powers = [np.log10(power) for power in powers]

    for power in powers:
        ax.plot(freqs, power, **plt_kwargs)

    if ylim is not None:
        ax.set_ylim(ylim)

    ax.set(xticks=[], yticks=[], xlabel=None, ylabel=None);


def plot_bar(d1, d2, ax=None):
    """Plot a bar plot comparison of two measures."""

    ax = check_ax(ax)

    ax.bar([0, 1], [d1, d2])
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Δ offset', 'Δ exponent']);
    ax.set_yticks([]);
    ax.set_ylim([-2, 2])
