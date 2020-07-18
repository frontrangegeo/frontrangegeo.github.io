#! /usr/bin/env python3.6
import seaborn as sns
import matplotlib.pyplot as plt
from data import times
import textwrap

sns.set(style="whitegrid")
plt.rcParams["axes.labelsize"] = 22
sns.set(font_scale=2)
# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 8))

#Load Phx Timing Data
tasks = [key for key in times]

# Plot the total time in Flatirons
sns.set_color_codes("pastel")
sns.barplot(x=[times[task]['Flatirons'] for task in tasks], y=tasks,
            label="Flatirons", color="b")

# Plot the time in Phoenix on top
sns.set_color_codes("muted")
sns.barplot(x=[times[task]['Phoenix'] for task in tasks], y=tasks,
            label="Phoenix", color="b")

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
plt.setp(ax.get_legend().get_texts(), fontsize='22')
ax.set(xlim=(0, 100), ylabel="",
       xlabel="% of Flatirons Time, 4 Node Cluster")
sns.despine(left=True, bottom=True)
f.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)
for ax in plt.gcf().axes:
    l = ax.get_xlabel()
    z = ax.get_ylabel()
    ax.set_xlabel(l, fontsize=22)
    ax.set_ylabel(z, fontsize=22)
ax.set_yticklabels([textwrap.fill(e, 7) if e != "Tomography" else "Tomography" for e in tasks])
plt.show()
