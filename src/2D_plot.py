import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r"Data\FitIndex\test_data_for_plotting.xlsx")

my_list_1 = [1000] * 67
my_list_2 = [2000] * 67
my_list_3 = [3000] * 67
my_list_4 = [4000] * 67

# Create a color map (you can choose a different colormap)
color_map = plt.get_cmap("viridis")

color_1 = df["fitindex 1kbar"]
color_2 = df["fitindex 2kbar"]
color_3 = df["fitindex 3kbar"]
color_4 = df["fitindex 4kbar"]


# Create the scatter plot
plt.scatter(
    my_list_1,
    df["temperature"],
    c=[color_map(i) for i in color_1],
    cmap="viridis",
    marker="s",
    s=8500,
)
plt.scatter(
    my_list_2,
    df["temperature.1"],
    c=[color_map(i) for i in color_2],
    cmap="viridis",
    marker="s",
    s=8500,
)
plt.scatter(
    my_list_3,
    df["temperature.2"],
    c=[color_map(i) for i in color_3],
    cmap="viridis",
    marker="s",
    s=8500,
)
plt.scatter(
    my_list_4,
    df["temperature.3"],
    c=[color_map(i) for i in color_4],
    cmap="viridis",
    marker="s",
    s=8500,
)


# Add labels and a title
plt.xlabel("Pressure (bar)")
plt.ylabel("Temperature (C)")

# Show the colorbar
colorbar = plt.colorbar()
colorbar.set_label("FitIndex Plagioclase")

plt.xticks([1000, 2000, 3000, 4000])

# Reduce white space between horizontal scatter points
plt.tight_layout()


# Show the plot
plt.show()
