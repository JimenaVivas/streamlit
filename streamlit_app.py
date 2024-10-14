import streamlit as st

# Estilos personalizados
st.markdown("""
    <style>
    .main-title {
        font-size: 48px;
        font-weight: bold;
        color: #007BFF;
        text-align: center;
    }
    .header-text {
        font-size: 32px;
        font-weight: bold;
        color: #FF5733;
        margin-top: 20px;
        text-align: center;
    }
    .selectbox-label {
        color: #5DADE2;
        font-size: 20px;
    }
    .stButton>button {
        background-color: #28B463;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #1D8348;
    }
    .navigation-button {
        background-color: #3498DB;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .navigation-button:hover {
        background-color: #2E86C1;
    }
    </style>
""", unsafe_allow_html=True)

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "PC", "Professor", "Team"]

def login():
    st.markdown('<h2 class="header-text">Log in</h2>', unsafe_allow_html=True)
    role = st.selectbox("Choose your role", ROLES, key="role", format_func=lambda x: x if x else "Select a role")

    if st.button("Log in"):
        st.session_state.role = role
        st.experimental_rerun()

def logout():
    st.markdown('<h2 class="header-text">Log out</h2>', unsafe_allow_html=True)

    if st.button("Log out"):
        st.session_state.role = None
        st.experimental_rerun()

role = st.session_state.role

# Custom navigation icons and titles
logout_page = st.Page(logout, title="Log out", icon="🔒")
settings = st.Page("settings.py", title="Settings", icon="⚙️")
visualization = st.Page("Visualization/visualization.py", title="Dashboard", icon="📊", default=(role == "Requester"))
ml = st.Page("ml/ml_analysis.py", title="Machine Learning", icon="🤖", default=(role == "Responder"))
eda = st.Page("EDA/eda.py", title="Exploratory Data Analysis", icon="🔍", default=(role == "Admin"))

account_pages = [logout_page, settings]
visualization_pages = [visualization]
ml_pages = [ml]
eda_pages = [eda]

# Main title
st.markdown('<h1 class="main-title">Data Analytics Dashboard</h1>', unsafe_allow_html=True)
st.image("images/horizontal_blue.png", use_column_width=True)

page_dict = {}

if st.session_state.role in ["Professor", "Team"]:
    page_dict["EDA"] = eda_pages
if st.session_state.role in ["Professor", "Team", "PC"]:
    page_dict["Visualization"] = visualization_pages
if st.session_state.role in ["Professor", "Team"]:
    page_dict["Machine Learning"] = ml_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
