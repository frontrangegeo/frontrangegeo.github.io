#! /usr/bin/env python3.6
import seaborn as sns
import matplotlib.pyplot as plt
from data import times
sns.set(style="whitegrid")

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
ax.set(xlim=(0, 91), ylabel="",
       xlabel="Time (hours)")
sns.despine(left=True, bottom=True)
f.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)
plt.show()
