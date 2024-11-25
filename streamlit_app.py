import streamlit as st

# Set Streamlit page configuration
st.set_page_config(
    page_title="AgroSphere - Your Agriculture Knowledge Hub",
    page_icon="🌾",
    layout="wide"
)

# Custom CSS for light theme and attractive UI
custom_css = """
<style>
    :root {
        --primary-color: #4CAF50; /* Green */
        --secondary-color: #FFC107; /* Yellow */
        --bg-color: #f9f9f9; /* Light background */
        --text-color: #333333; /* Dark text */
        --button-hover-color: #357a38; /* Darker Green for buttons */
    }
    body {
        background-color: var(--bg-color);
    }
    .main {
        background-color: var(--bg-color);
        color: var(--text-color);
        font-family: Arial, sans-serif;
    }
    h1, h2, h3 {
        color: var(--primary-color);
        font-weight: 700;
    }
    .stButton > button {
        background-color: var(--primary-color);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
    }
    .stButton > button:hover {
        background-color: var(--button-hover-color);
        color: white;
    }
    iframe {
        border: none;
        width: 100%;
        height: 80vh;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Header Section
st.markdown("<h1 style='text-align: center;'>🌾 AgroSphere</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center;'>Empowering Farmers with Actionable Knowledge</h3>",
    unsafe_allow_html=True,
)
st.write("---")

# Navigation Menu
menu = ["Home", "Agriculture"]
choice = st.sidebar.selectbox("Navigate to:", menu)

# Home Page
if choice == "Home":
    st.markdown("## Welcome to AgroSphere!")
    st.markdown(
        """
        **AgroSphere** is your trusted platform for reliable and actionable agricultural knowledge.
        Here, you'll find essential resources, updates, and tools to enhance farming practices and improve productivity.
        Explore the Agriculture section for detailed content.
        """
    )
    st.image(
        "https://via.placeholder.com/1200x500?text=AgroSphere+Banner",
        use_column_width=True,
    )
    st.markdown(
        """
        ### What You'll Find:
        - Latest techniques and innovations in agriculture.
        - Guides for crop management and sustainable practices.
        - Insights on government schemes and policies for farmers.
        """
    )
    st.markdown("🔍 **Click on the sidebar to explore the Agriculture section!**")

# Agriculture Section
elif choice == "Agriculture":
    st.markdown("## Agriculture Knowledge Hub")
    st.image(
        "https://via.placeholder.com/1200x400?text=AgroSphere+-+Agriculture+Resources",
        use_column_width=True,
    )
    st.markdown(
        """
        Below is a trusted agricultural knowledge source embedded directly for your convenience:
        """
    )
    # Embed Vikaspedia Agriculture section
    st.markdown(
        '<iframe src="https://en.vikaspedia.in/viewcontent/agriculture"></iframe>',
        unsafe_allow_html=True,
    )

# Footer Section
st.write("---")
st.markdown(
    "<p style='text-align: center;'>© 2024 AgroSphere | Empowering Communities with Knowledge 🌱</p>",
    unsafe_allow_html=True,
)
