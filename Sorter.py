import pandas as pd
import streamlit as st
from PIL import Image
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import urllib.request

url = "https://raw.githubusercontent.com/BISMCA/Files/main/rev_sort.csv"
rev_sort = pd.read_csv(url)

#Streamlit Page
st.cache(suppress_st_warning=True)
urllib.request.urlretrieve(
  'https://github.com/BISMCA/Files/blob/e33c2ce8dbbf2e400cee59437aa8e5c15831fe6e/sort.jpg?raw=true',
   "sort.png")
img = Image.open("sort.png")
st.image(img, caption = 'Lets Travel')

st.subheader("Hi, you can check reviews of your favourite hotels here")


#st.dataframe(data = rev_sort)
#AgGrid(rev_sort)

gb = GridOptionsBuilder.from_dataframe(rev_sort)
gb.configure_pagination(paginationAutoPageSize=False) #Add pagination
gb.configure_side_bar() #Add a sidebar
#gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()

grid_response = AgGrid(
    rev_sort,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=True,
    #theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    reload_data=True
)

data = grid_response['data']
selected = grid_response['selected_rows'] 
df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df