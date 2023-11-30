import matplotlib.pyplot as plt

# Sample top 11 players' data
players = ['Alisson', 'Ruben Dias', 'Thiago Silva', 'Aymeric Laporte', 'Joao Cancelo', 'Kevin De Bruyne', 'Rodri', 'Thiago Alcantra', 'Jorginho', 'Riyad Mahrez', 'Mohamed Salah']
positions = ['GK', 'LB', 'CB', 'CB', 'RB', 'CM', 'CM', 'LM', 'RM', 'LF', 'RF']

# Create a field image (replace with an actual field image)
field_image = plt.imread('Field.png')

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.imshow(field_image)
ax.axis('off')

# Define player positions on the field
x_positions = [317, 80, 220, 380, 550, 330, 330, 120, 545, 200, 450]
y_positions = [886, 740, 760, 760, 740, 425, 610, 391, 391, 260, 260]

# Plot player names and positions
for i in range(11):
    ax.text(x_positions[i], y_positions[i], f'{players[i]}\n{positions[i]}', ha='center', fontsize=12, color='black')




# Show the plot
plt.title('MY Top 11 Soccer Players of the Season 2021/2022')
plt.show()
