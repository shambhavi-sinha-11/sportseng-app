import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to calculate performance score
def calculate_score(friction, hardness, roughness, rebound, weights):
    return (
        weights["friction"] * friction +
        weights["hardness"] * hardness +
        weights["roughness"] * roughness +
        weights["rebound"] * rebound
    )

# Define weights for the parameters
weights = {
    "friction": 0.25,
    "hardness": 0.25,
    "roughness": 0.25,
    "rebound": 0.25
}

# Sidebar for user inputs
st.sidebar.header("Enter Surface Parameters")
user_inputs = {
    "friction": st.sidebar.slider("Friction", 0.0, 1.0, 0.5),
    "hardness": st.sidebar.slider("Hardness", 1, 10, 5),
    "roughness": st.sidebar.slider("Roughness", 0.0, 1.0, 0.5),
    "rebound": st.sidebar.slider("Rebound", 0.0, 1.0, 0.5),
}

# Preloaded benchmark materials
materials = {
    "Polyurethane": {"friction": 0.6, "hardness": 7, "roughness": 0.4, "rebound": 0.5},
    "Rubber": {"friction": 0.8, "hardness": 5, "roughness": 0.6, "rebound": 0.7},
    "Engineered Wood": {"friction": 0.4, "hardness": 8, "roughness": 0.3, "rebound": 0.4},
}

# Dropdown for benchmark material selection
st.sidebar.header("Select a Benchmark Material")
selected_material = st.sidebar.selectbox("Material", materials.keys())
benchmark = materials[selected_material]

# Calculate scores
user_score = calculate_score(
    friction=user_inputs["friction"],
    hardness=user_inputs["hardness"],
    roughness=user_inputs["roughness"],
    rebound=user_inputs["rebound"],
    weights=weights,
)

benchmark_score = calculate_score(
    friction=benchmark["friction"],
    hardness=benchmark["hardness"],
    roughness=benchmark["roughness"],
    rebound=benchmark["rebound"],
    weights=weights,
)

# Display scores
st.header("Performance Scores")
st.write(f"**User-defined Surface Score:** {user_score:.2f}")
st.write(f"**Benchmark ({selected_material}) Score:** {benchmark_score:.2f}")

# Visualization
st.header("Comparison of Parameters")
data = pd.DataFrame([user_inputs, benchmark], index=["User Surface", selected_material])

# Bar chart for comparison
st.bar_chart(data)

# Detailed parameter breakdown
st.header("Detailed Parameter Breakdown")
fig, ax = plt.subplots()
data.T.plot(kind="bar", ax=ax, rot=0, colormap="viridis")
plt.title("Comparison of Parameters")
plt.ylabel("Value")
st.pyplot(fig)
