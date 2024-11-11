from LifeAC import Grid
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

rows = int(input("Number of rows "))
columns = int(input("Number of columns "))
steps = int(input("Number of steps "))
#tupla_distraccion = tuple(input("Tuple for distraction ej. (0.2,0.8) "))
initial_num_cells = int(input("Number of cells "))
cell_random = bool(input("Is it random 1 = yes, 0 = no "))

print(f"Rows: {rows}")
print(f"Columns: {columns}")
print(f"Steps: {steps}")
#print(f"tupla_distraccion: {tupla_distraccion}")
#print(f"V max: {v_max}")

automata = Grid(columns, rows, steps, initial_num_cells, cell_random = 1)
automata.create_CA()
"""
plt.imshow(automata.binary_matrix, cmap='gray', interpolation='none')
plt.colorbar()
plt.show()

plt.imshow(automata.update_matrix(), cmap='gray', interpolation='none')
plt.colorbar()
plt.show()
"""
#Graph_cellular(automata.binary_matrix).graph()
#
#Graph_cellular(matrix).graph()
count = 0

fig, ax = plt.subplots()


def update(i):
    global count
    print(count)
    if count == 0:
        new_matrix = automata.binary_matrix
    else:
        new_matrix = automata.update_matrix()
    ax.imshow(new_matrix)
    ax.set_axis_off()
    count = count + 1
    
anim = FuncAnimation(fig, update, frames = steps, interval = 1000)
fig.suptitle(f'Life Game', fontsize=14) 
#plt.show()




  
# saving to m4 using ffmpeg writer 
#writervideo = anim.FFMpegWriter(fps=60) 
#anim.save('increasingStraightLine.mp4', writer=writervideo) 
anim.save(filename="gifs/pillow_example.gif", writer="pillow")
plt.close() 