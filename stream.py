# CREATING THE APP
import matplotlib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np

st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")

# DISPLAYING TEXT
st.title("This is a Title")
st.header("This is a Header")
st.subheader("This is a Subheader")
st.text("Plain text goes here.")
st.markdown("**Bold**, *italic*, and `code` with Markdown!")
st.caption("Small caption text.")
st.write("st.write() can display almost anything!")

# GETTING USER INPUT
# Text input
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

# Slider
age = st.slider("Select your age", min_value=0, max_value=100, value=25)
st.write(f"You are {age} years old.")

# Checkbox
show_secret = st.checkbox("Show secret message")
if show_secret:
    st.success("You found the secret!")

# Select box
color = st.selectbox("Pick a color", ["Red", "Green", "Blue", "Yellow"])
st.write(f"You chose: {color}")

# Multi-select
fruits = st.multiselect("Pick your favorite fruits", ["Apple", "Banana", "Cherry", "Mango"])
st.write(f"Your favorites: {fruits}")

# Button
if st.button("Click me!"):
    st.balloons()  # Fun celebration effect!

# DISPLAYING DATA WITH PANDAS
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [28, 34, 22, 45],
    "Score": [88.5, 92.3, 78.1, 95.0]
})

st.subheader("Static Table")
st.table(df)  # Non-interactive

st.subheader("Interactive DataFrame")
st.dataframe(df, use_container_width=True)  # Sortable, scrollable

# Metric cards
col1, col2, col3 = st.columns(3)
col1.metric("Average Score", f"{df['Score'].mean():.1f}", "+2.3")
col2.metric("Total Students", len(df))
col3.metric("Top Score", f"{df['Score'].max()}")

# CHARTS AND VISUALIZATION
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["Series A", "Series B", "Series C"]
)

st.subheader("Built-in Charts")
st.line_chart(data)
st.bar_chart(data.abs().head(10))
st.area_chart(data)

# Matplotlib
st.subheader("Matplotlib Figure")
fig, ax = plt.subplots()
ax.hist(data["Series A"], bins=15, color="steelblue", edgecolor="white")
ax.set_title("Distribution of Series A")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# LAYOUT
# Sidebar
st.sidebar.title("⚙Settings")
theme = st.sidebar.radio("Choose theme", ["Light", "Dark"])
st.write(f"Current theme: **{theme}**")

# Columns
st.subheader("Columns")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("Left")
with col2:
    st.success("Middle")
with col3:
    st.warning("Right")

# Tabs
st.subheader("Tabs")
tab1, tab2, tab3 = st.tabs(["Home", "Data", "ℹAbout"])
with tab1:
    st.write("Welcome to the Home tab!")
with tab2:
    st.write("Data goes here.")
with tab3:
    st.write("About this app.")

# Expander
with st.expander("Click to expand"):
    st.write("Hidden content revealed!")

# SESSION STATE
if "count" not in st.session_state:
    st.session_state.count = 0

st.title("Counter App")
st.write(f"Current count: **{st.session_state.count}**")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Increment"):
        st.session_state.count += 1
with col2:
    if st.button("Decrement"):
        st.session_state.count -= 1
with col3:
    if st.button("Reset"):
        st.session_state.count = 0

# CACHE
@st.cache_data
def load_data():
    """Simulates a slow data loading operation."""
    time.sleep(2)  # Simulated delay
    return pd.DataFrame({
        "x": range(100),
        "y": [i ** 2 for i in range(100)]
    })

st.title("Caching Demo")
st.write("First load takes 2 seconds. Subsequent loads are instant!")

with st.spinner("Loading data..."):
    df = load_data()

st.success("Data loaded!")
st.line_chart(df.set_index("x"))

# UPLOAD AND DOWNLOAD
#%%
st.title("File Upload & Download")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(f"Loaded **{len(df)} rows** and **{len(df.columns)} columns**.")
    st.dataframe(df.head())

    # Download processed file
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download processed CSV",
        data=csv,
        file_name="processed_data.csv",
        mime="text/csv"
    )
else:
    st.info("Please upload a CSV file to get started.")

# FINISHING TOUCHES
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Sidebar controls
st.sidebar.title("Sales Dashboard")
num_months = st.sidebar.slider("Months to display", 1, 12, 6)
show_raw = st.sidebar.checkbox("I do NOTHING!")

@st.cache_data
def generate_sales_data(n):
    return pd.DataFrame({
        "Month": [f"Month {i+1}" for i in range(n)],
        "Revenue": np.random.randint(50000, 200000, n),
        "Expenses": np.random.randint(30000, 100000, n),
        "Customers": np.random.randint(100, 500, n)
    })

df = generate_sales_data(num_months)
df["Profit"] = df["Revenue"] - df["Expenses"]

# Title
st.title("Sales Dashboard")
st.markdown(f"Showing data for the last **{num_months} months**.")

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${df['Revenue'].sum():,}")
col2.metric("Total Expenses", f"${df['Expenses'].sum():,}")
col3.metric("Total Profit", f"${df['Profit'].sum():,}")
col4.metric("Total Customers", f"{df['Customers'].sum():,}")

st.divider()

# Charts in tabs
tab1, tab2 = st.tabs(["Revenue & Expenses", "Customers"])
with tab1:
    st.line_chart(df.set_index("Month")[["Revenue", "Expenses", "Profit"]])
with tab2:
    st.bar_chart(df.set_index("Month")["Customers"])

# DEPLOYMENT / DEPLOYING YOUR APP
# Deploy for free on **Streamlit Community Cloud**:
# Push your code to a GitHub repository
# Go to [share.streamlit.io](https://share.streamlit.io)
# Connect your GitHub and select your repo
# Click **Deploy!**
# Your app will be live at `https://your-app-name.streamlit.app`.
# A quick reference cheat sheet can be found in the attached image.
# Function: `st.title()`, `st.header()`, `st.subheader()` (used for Headings)










