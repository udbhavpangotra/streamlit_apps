import streamlit as st
import time
import numpy as np
# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()


st.write(

    '''    
I will be trying a few random graphs here! just to get some idea about this! :)
    '''
)

a = [1, 2, 3, 4, 5, 5]
b = [1, 2, 12, 31, 23, 123, 12, 41]

st.line_chart(a)
st.line_chart(b)
st.area_chart(a)
st.bar_chart(a)
# st.bokeh_chart(b)
# progress_bar.empty()


# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
