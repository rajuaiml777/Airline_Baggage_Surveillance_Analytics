import matplotlib.pyplot as plt
import seaborn as sns


def bar_plot(x, y):
    plt.figure(figsize=(7, 5), facecolor='grey')
    ax = sns.barplot(x = x, y = y)
    width_bars = 4 * [0.8] if len(ax.patches) == 4 \
        else (3 * [0.6] if len(ax.patches) == 3
              else (2 * [0.4] if len(ax.patches) == 2
                    else [0.2]))
    tot_bags = y.sum()
    for bar, new_width in zip(ax.patches, width_bars):
        x = bar.get_x()
        width = bar.get_width()
        centre = x + width / 2.0
        text = round(int(bar.get_height()) / tot_bags, 2)
        ax.text(centre, bar.get_height(), f"{text} %", fontsize=8, color='black')
        bar.set_x(centre - new_width / 2.0)
        bar.set_width(new_width)
    plt.legend([f'Total Bags Checked: {tot_bags}'], prop={"size": 8})