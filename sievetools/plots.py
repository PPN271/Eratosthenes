from matplotlib import pyplot as plt

def plot_sieve(all_nmax, all_proportions, log_scale = False):
    if log_scale == False:
        plt.plot(all_nmax, all_proportions)
        plt.xlabel("N")
        plt.ylabel("Proportion of primer numbers")
    else:
        plt.plot(all_nmax, all_proportions)
        plt.xlabel("N")
        plt.ylabel("Proportion of primer numbers")
        plt.xscale("log")
        plt.yscale("log")

