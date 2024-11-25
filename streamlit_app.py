import streamlit as st

# Apply custom CSS for full-screen layout and styling
def apply_custom_css():
    st.markdown(
        """
        <style>
        /* Full-screen layout */
        .main {
            padding: 0rem;
        }
        
        iframe {
            width: 100%;
            height: 100vh;
            border: none;
            border-radius: 8px;
        }

        body {
            background-color: #f9f9f9;
            color: #333333;
            font-family: Arial, sans-serif;
        }

        .header {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }

        .footer {
            margin-top: 1rem;
            text-align: center;
            font-size: 0.8rem;
            color: #5c5c5c;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Apply custom CSS
apply_custom_css()

# Custom branding
st.markdown('<div class="header"><h1>AgriConnect - Empowering Agriculture</h1></div>', unsafe_allow_html=True)

st.write("""
Welcome to **AgriConnect**, your ultimate platform for accessing agricultural knowledge and resources. 
Discover the latest insights, best practices, and tools to enhance agricultural productivity and sustainability.
""")

# Embed only the functional part of the Vikaspedia agriculture page
content_url = "https://en.vikaspedia.in/viewcontent/agriculture"
st.components.v1.html(
    f"""
    <iframe 
        src="{content_url}" 
        style="width:100%; height:100vh;" 
        onload="(function() {{
            // Hide unwanted elements by class or ID
            const unwantedElements = ['.footer', '#header', '#sidebar', '.app-footer', '.ministry-logo'];
            unwantedElements.forEach(selector => {{
                const elements = document.querySelectorAll(selector);
                elements.forEach(element => element.style.display = 'none');
            }});
        }})();">
    </iframe>
    """,
    height=800,
)

# Footer
st.markdown(
    """
    <div class="footer">
        © 2024 AgriConnect | Your Agriculture Companion.
    </div>
    """,
    unsafe_allow_html=True,
)
