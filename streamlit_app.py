import streamlit as st

from core_app import core_app
from column_dict import custom_mapping
from display_utils import get_license_image


#options to have the layout wide
st.set_page_config(layout='wide')
#option to see altair tooltip in graph fullscreen mode
st.markdown('<style>#vg-tooltip-element{z-index: 1000051}</style>',
          unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
#option to hide the streamlit bottom right footer
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

app_versions = [
  'annelida',
  'reptiles',
  'crustaceas',
  'polychaeta',
  'GBIF'
]


# beginning of app
st.title('Viz_Zoo Tool')


if 'app_version' not in st.session_state:
  
  # plays when the app_version is not yet chosen
  box, tick = st.columns((6,1))
  with box:
    app_version = st.selectbox(label='choose app version', options=app_versions, format_func=lambda x : x+' (or any custom csv dataset)' if (x=='GBIF') else x)
  with tick:
    custom = st.checkbox(label='use custom data and mapping', value=False)
  version_chosen = st.button(label='validate choice')
  if version_chosen:
    st.session_state['app_version'] = app_version
    st.session_state['custom'] = custom
    st.experimental_rerun()
  
  #simple explanations for the user
  with st.expander(label='upload custom data'):
    st.write('If you want to use a custom dataset for this software, you need to provide a "mapping" of the column names to the name of the fields required for this software to work. Everything is detailed in the README.md at https://github.com/UniversityofBrighton/viszoo/tree/main/README.md')
    st.write('\nThis is an example of "custom column mapping", which is the one used in the GBIF version of the app when you dont provide one yourself: ')
    st.dataframe(custom_mapping)


else:
  #when the app_version is chosen by the user, call core_app
  if st.session_state['app_version'] != 'GBIF':
    st.session_state['custom'] = False
  core_app(st.session_state["app_version"], st.session_state['custom'])

# display open source license
_, col1, col2 = st.columns((6,1,1))
col1.write('licensed under Apache 2.0')
col2.image(get_license_image(),width=15)