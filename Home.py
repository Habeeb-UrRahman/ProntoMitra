# import streamlit as st

# # Page configuration
# st.set_page_config(
#     page_title="Pronto Mitra",
#     page_icon="🤝",
# )

# # Sidebar
# st.sidebar.title("Pronto Mitra")
# st.sidebar.image('assets/logo_1_1.png', width=250)
# st.sidebar.success("Select a Tool above.")

# # Main content
# st.title("Welcome to Pronto Mitra 👋")

# st.markdown(
#     """
#     Pronto Mitra serves as the central dashboard in our project, integrating two key models to enhance our document management and predictive capabilities. The dashboard is designed to provide comprehensive insights and predictions to streamline our processes and improve efficiency.
#     """
# )

# # Tool descriptions
# with st.expander("About Pronto Genie"):
#     st.markdown("""
#     Pronto Genie is the prediction model within Pronto Mitra, focused on forecasting document counts based on various input parameters. By leveraging machine learning techniques, Pronto Genie enables us to anticipate the number of documents that will be received in future periods, thus facilitating better planning and resource allocation.

#     **Key Features:**
#     - Data Input: Users can upload data files containing historical document records.
#     - Data Processing: The model preprocesses the data, extracting relevant features such as date, job code, and module.
#     - Model Training: Pronto Genie utilizes Ridge regression with polynomial features, selected for its ability to capture non-linear relationships and prevent overfitting.
#     - Prediction: The model predicts future document counts for specified months, providing day-wise and module-wise breakdowns.
#     - Visualization: The predictions are visualized through graphs and tables, offering a clear view of the expected document inflow.
#     """)

# with st.expander("About Pronto Viz"):
#     st.markdown("""
#     Pronto Viz is the data analysis Tool within Pronto Mitra, designed to analyze the time taken by employees to process documents. This tool plays a crucial role in document allocation and resource management, ensuring that tasks are distributed efficiently and employee performance is monitored effectively.

#     **Key Features:**
#     - Data Input: Users can upload data files detailing employee processing times and document handling.
#     - Data Analysis: The tool analyzes the time taken for each document, identifying patterns and bottlenecks in the process.
#     - Resource Management: Based on the analysis, Pronto Viz provides insights into optimal document allocation, ensuring that workload is balanced among employees.
#     - Performance Monitoring: The tool helps track employee performance over time, identifying areas for improvement and training needs.
#     - Visualization: Results are presented through intuitive charts and dashboards, highlighting key metrics and performance indicators.
#     """)

# # Buttons and PDF embedding
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("Open Manual for Pronto Genie"):
#         st.markdown("<a href='https://github.com/Habeeb-UrRahman/ProntoMitra_Manuals/blob/main/Pronto%20Genie%20User%20Manual.pdf' target='_blank'>Open Manual for Pronto Genie</a>", unsafe_allow_html=True)

# with col2:
#     if st.button("Open Manual for Pronto Viz"):
#         st.markdown("<a href='https://github.com/Habeeb-UrRahman/ProntoMitra_Manuals/blob/main/ProntoViz%20User%20Manual.pdf' target='_blank'>Open Manual for ProntoViz</a>", unsafe_allow_html=True)

# # Footer with adjusted styling and alignment
# st.markdown("""
#     <style>
#     .footer {
#         position: fixed;
#         left: 0;
#         bottom: 0;
#         width: 100%;
#         background-color: rgba(0, 0, 0, 0.5); /* Transparent background */
#         color: white; /* White text color */
#         text-align: right; /* Align text to the right */
#         padding: 10px; /* Padding for better spacing */
#         font-size: 14px;
#         border-top: 0.5px solid #eaeaea;
#     }
#     .footer a {
#         margin-left: 10px; /* Margin between LinkedIn icon and text */
#     }
#     .footer img {
#         width: 24px; /* Reduce LinkedIn logo size */
#         vertical-align: middle; /* Align logo vertically with text */
#     }
#     </style>
#     <div class="footer">
#         <p style="margin-right: 500px;">Developed by <a href="https://www.linkedin.com/in/saitharunjami/" target="_blank"><img src="https://img.icons8.com/color/48/000000/linkedin.png"/></a> Jami Sai Tharun <a href="https://www.linkedin.com/in/habeeb-urrahman/" target="_blank"><img src="https://img.icons8.com/color/48/000000/linkedin.png"/></a> Habeeb Ur Rahman</p>
#     </div>
#     """, unsafe_allow_html=True)





import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Pronto Mitra",
    page_icon="🤝",
)

# Sidebar
st.sidebar.title("Pronto Mitra")
st.sidebar.image('assets/logo_1_1.png', width=250)
st.sidebar.success("Select a Tool above.")

# Main content
st.title("Welcome to Pronto Mitra 👋")

st.markdown(
    """
    Pronto Mitra serves as the central dashboard in our project, integrating two key models to enhance our document management and predictive capabilities. The dashboard is designed to provide comprehensive insights and predictions to streamline our processes and improve efficiency.
    """
)

# Tool descriptions
with st.expander("About Pronto Genie"):
    st.markdown("""
    Pronto Genie is the prediction model within Pronto Mitra, focused on forecasting document counts based on various input parameters. By leveraging machine learning techniques, Pronto Genie enables us to anticipate the number of documents that will be received in future periods, thus facilitating better planning and resource allocation.

    **Key Features:**
    - Data Input: Users can upload data files containing historical document records.
    - Data Processing: The model preprocesses the data, extracting relevant features such as date, job code, and module.
    - Model Training: Pronto Genie utilizes Ridge regression with polynomial features, selected for its ability to capture non-linear relationships and prevent overfitting.
    - Prediction: The model predicts future document counts for specified months, providing day-wise and module-wise breakdowns.
    - Visualization: The predictions are visualized through graphs and tables, offering a clear view of the expected document inflow.
    """)

with st.expander("About Pronto Viz"):
    st.markdown("""
    Pronto Viz is the data analysis Tool within Pronto Mitra, designed to analyze the time taken by employees to process documents. This tool plays a crucial role in document allocation and resource management, ensuring that tasks are distributed efficiently and employee performance is monitored effectively.

    **Key Features:**
    - Data Input: Users can upload data files detailing employee processing times and document handling.
    - Data Analysis: The tool analyzes the time taken for each document, identifying patterns and bottlenecks in the process.
    - Resource Management: Based on the analysis, Pronto Viz provides insights into optimal document allocation, ensuring that workload is balanced among employees.
    - Performance Monitoring: The tool helps track employee performance over time, identifying areas for improvement and training needs.
    - Visualization: Results are presented through intuitive charts and dashboards, highlighting key metrics and performance indicators.
    """)

# Buttons and PDF embedding
col1, col2 = st.columns(2)
with col1:
    if st.button("Open Manual for Pronto Genie"):
        st.markdown("<a href='https://github.com/Habeeb-UrRahman/ProntoMitra_Manuals/blob/main/Pronto%20Genie%20User%20Manual.pdf' target='_blank'>Open Manual for Pronto Genie</a>", unsafe_allow_html=True)

with col2:
    if st.button("Open Manual for Pronto Viz"):
        st.markdown("<a href='https://github.com/Habeeb-UrRahman/ProntoMitra_Manuals/blob/main/ProntoViz%20User%20Manual.pdf' target='_blank'>Open Manual for ProntoViz</a>", unsafe_allow_html=True)

# Footer with adjusted styling and alignment
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(0, 0, 0, 0.5); /* Transparent background */
        color: white; /* White text color */
        text-align: right; /* Align text to the right */
        padding: 10px; /* Padding for better spacing */
        font-size: 14px;
        border-top: 0.5px solid #eaeaea;
    }
    .footer a {
        margin-left: 10px; /* Margin between LinkedIn icon and text */
    }
    .footer img {
        width: 24px; /* Reduce LinkedIn logo size */
        vertical-align: middle; /* Align logo vertically with text */
    }
    </style>
    <div class="footer">
        <p style="margin-right: 10px;">Developed by <a href="https://www.linkedin.com/in/saitharunjami/" target="_blank"><img src="https://img.icons8.com/color/48/000000/linkedin.png"/></a> Jami Sai Tharun <a href="https://www.linkedin.com/in/habeeb-urrahman/" target="_blank"><img src="https://img.icons8.com/color/48/000000/linkedin.png"/></a> Habeeb Ur Rahman</p>
    </div>
    """, unsafe_allow_html=True)
