import matplotlib.pyplot as plt
import numpy as np

# input data values

 
# preparing values for graph
columns = ('Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5')
rows = ['%d months' % x for x in (50, 35, 20, 10, 5)]
values = np.arange(0, 2500, 500)
value_increment = 1000
 
# Adding pastel shades to graph
colors = plt.cm.Oranges(np.linspace(22, 3, 12))
n_rows = len(data)
index = np.arange(len(columns)) + 0.3
bar_width = 0.4
 
# Initializing vertical-offset for the graph.
y_offset = np.zeros(len(columns))
 
# Plot bars and create text labels for the table
cell_text = []
 
for row in range(n_rows):
    plt.plot(index, data[row], bar_width, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x) for x in y_offset])
 
# Reverse colors and text labels to display table contents with
# color.
colors = colors[::-1]
cell_text.reverse()
 
# Add a table at the bottom
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
 
# make space for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)
plt.ylabel("Price in ${0}'s".format(value_increment))
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Cost price increase')
 
 
fig = plt.gcf()
plt.savefig('pyplot-table-original.png',
            bbox_inches='tight',
            dpi=150)