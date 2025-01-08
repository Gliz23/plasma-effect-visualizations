import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Title for the Streamlit App
st.title("Plasma Effect Visualization")

# Description of Plasma Effect
st.markdown("""
**Plasma Effect:** Plasma effects create wobbly animations in products like screen savers. This effect can be modeled using mathematical functions like sine.
""")

# Task Description
st.markdown("""
### Task: Create a Grid and Plot the Function
We will create a grid with \(x, y \in [-\pi, \pi]\) and plot the function \( f(x, y) = \sin(5 \cdot x) \). This is a simplified representation of a plasma effect.
""")

# Define the grid with x and y values ranging from -π to π
x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(x, y)

# Define the function f(x, y) = sin(5 * x)
Z1 = np.sin(5 * X)

# Create the 3D plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z1, cmap='viridis')

# Set the labels of the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Display the 3D plot in Streamlit
st.pyplot(fig)

# Create a 2D contour plot
fig2 = plt.figure(figsize=(10, 6))
plt.contourf(X, Y, Z1, levels=32, cmap='viridis')
plt.title('2D Contour Plot of f(x, y)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the 2D plot in Streamlit
st.pyplot(fig2)