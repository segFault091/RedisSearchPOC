import urllib

import pandas as pd
import streamlit as st


@st.cache
def get_UN_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")


try:
    user_input = st.text_input(label="Search")
    if user_input:
        st.write(f"There is some value. Processing...{user_input}")
    # Some code
except urllib.error.URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
