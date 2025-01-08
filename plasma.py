import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Title for the Streamlit App
st.title("Plasma Effect Visualization")

# Description of Plasma Effect
st.markdown("""
**Plasma Effect:** Plasma effects create wobbly animations in products like screen savers. This effect can be modeled using mathematical functions like sine, cosine, and tangent.
""")

# Task Description
st.markdown("""
### Task: Create a Grid and Plot Multiple Functions
We will create a grid with \(x, y \in [-\pi, \pi]\) and plot the following functions:
1. \( f_1(x, y) = \sin(5 \cdot x) \)
2. \( f_2(x, y) = \cos(5 \cdot x) \)
3. \( f_3(x, y) = \tan(5 \cdot x) \) (with clipping to avoid extreme values)
4. \( f_4(x, y) = \frac{(\sin(3 \cdot x))^2 + (\sin(3 \cdot y))^2}{2} \)
5. \( f_5(x, y) = \frac{(\sin(5 \cdot x))^3 + (\sin(5 \cdot y))^3}{2} \) (using the new function definition)
""")

# Define the grid with x and y values ranging from -π to π
x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(x, y)

# Define the first three functions
Z1 = np.sin(5 * X)
Z2 = np.cos(5 * X)
Z3 = np.clip(np.tan(5 * X), -10, 10)  # Clipping the tangent function

# Define the fourth function (f)
def f(x, y, f_val, p):
    A = (np.sin(f_val * x)) ** p
    B = (np.sin(f_val * y)) ** p
    C = (A + B) / 2
    return C

# Instantiate the functions
Z4 = f(X, Y, 3, 2)
Z5 = f(X, Y, 5, 3)

# Create and show 3D plots for each function
figures = []

# 3D plot for the sine function
st.markdown("### 3D Plot of $f_1(x, y) = \sin(5 \cdot x)$")
fig1 = plt.figure(figsize=(10, 6))
ax1 = fig1.add_subplot(111, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
ax1.set_zlabel('Z-axis')
figures.append(fig1)
st.pyplot(fig1)

# 3D plot for the cosine function
st.markdown("### 3D Plot of $f_2(x, y) = \cos(5 \cdot x)$")
fig2 = plt.figure(figsize=(10, 6))
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='plasma')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.set_zlabel('Z-axis')
figures.append(fig2)
st.pyplot(fig2)

# 3D plot for the tangent function
st.markdown("### 3D Plot of $f_3(x, y) = \tan(5 \cdot x)$ (Clipped)")
fig3 = plt.figure(figsize=(10, 6))
ax3 = fig3.add_subplot(111, projection='3d')
ax3.plot_surface(X, Y, Z3, cmap='inferno')
ax3.set_xlabel('X-axis')
ax3.set_ylabel('Y-axis')
ax3.set_zlabel('Z-axis')
figures.append(fig3)
st.pyplot(fig3)

# 3D plot for the fourth function
st.markdown("### 3D Plot of $f_4(x, y) = \\frac{(\\sin(3 \\cdot x))^2 + (\\sin(3 \\cdot y))^2}{2}$")
fig4 = plt.figure(figsize=(10, 6))
ax4 = fig4.add_subplot(111, projection='3d')
ax4.plot_surface(X, Y, Z4, cmap='magma')
ax4.set_xlabel('X-axis')
ax4.set_ylabel('Y-axis')
ax4.set_zlabel('Z-axis')
figures.append(fig4)
st.pyplot(fig4)

# 3D plot for the fifth function
st.markdown("### 3D Plot of $f_5(x, y) = \\frac{(\\sin(5 \\cdot x))^3 + (\\sin(5 \\cdot y))^3}{2}$")
fig5 = plt.figure(figsize=(10, 6))
ax5 = fig5.add_subplot(111, projection='3d')
ax5.plot_surface(X, Y, Z5, cmap='cividis')
ax5.set_xlabel('X-axis')
ax5.set_ylabel('Y-axis')
ax5.set_zlabel('Z-axis')
st.pyplot(fig5)

# Create a 2D contour plot for the fourth function
st.markdown("### 2D Contour Plot of $f_4(x, y)$")
fig6 = plt.figure(figsize=(10, 6))
plt.contourf(X, Y, Z4, levels=50, cmap='magma')
plt.title('2D Contour Plot of $f_4(x, y)$')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
st.pyplot(fig6)

# Create a 2D contour plot for the fifth function
st.markdown("### 2D Contour Plot of $f_5(x, y)$")
fig7 = plt.figure(figsize=(10, 6))
plt.contourf(X, Y, Z5, levels=25, cmap='cividis')
plt.title('2D Contour Plot of $f_5(x, y)$')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
st.pyplot(fig7)

# Function for the next plot
def f2(X, Y):
    return np.abs(np.cos(20 * (np.cos(X)**2 + np.sin(Y)**2)))

# Calculate Z5
Z5 = f2(X, Y)

# 3D Plot for Z5
st.subheader("3D Surface Plot of f(x, y) = |cos(20(cos²(x) + sin²(y)))|")
fig_3d_2 = plt.figure()
ax2 = fig_3d_2.add_subplot(111, projection='3d')
ax2.plot_surface(X, Y, Z5, cmap='plasma')

# Labeling the axes
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

# Show the 3D plot in Streamlit
st.pyplot(fig_3d_2)

# 2D Contour Plot for Z5
st.subheader("2D Contour Plot of f(x, y)")
fig_2d_2 = plt.figure()
contour2 = plt.contourf(X, Y, Z5, 50, cmap='plasma')
plt.colorbar(contour2)  # Add a color bar for reference
plt.title('2D Contour Plot of Z5')
plt.xlabel('X')
plt.ylabel('Y')

# Show the 2D plot in Streamlit
st.pyplot(fig_2d_2)

# Observation for Z5
st.subheader("Observation for f(x, y)")
st.write("""
The function exhibits periodic behavior with distinct peaks and troughs.
          The color variations in the contour plot signify the amplitude
          variations across the surface.
""")



