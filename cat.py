import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "első rács": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "második rács": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        }
    )

 
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()


st.dataframe(df, use_container_width=st.session_state.use_container_width)
