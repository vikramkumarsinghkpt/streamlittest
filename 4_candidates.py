import streamlit as st
import pandas as pd

# # st.set_page_config(layout="wide", page_title="Candidate Profiles", )


# import streamlit as st

# def set_custom_width(width_px):
#   """
#   Function to set a custom width for a Streamlit container using CSS.
#   """
#   style = f"""
#   [data-testid="stContainer"] {{
#       max-width: {width_px}px;
#       width: {width_px}px;
#   }}
#   """
#   return style

# # Set your desired width
# container_width = 1200  # You can adjust this value (between 720 and 3320)

# st.set_page_config(page_title="My Streamlit App", layout="centered")
# st.markdown(set_custom_width(container_width), unsafe_allow_html=True)

# # Your Streamlit app code with container goes here
# with st.container():
#   # Your elements within the container
#   st.write("Content inside the custom width container")








# data = pd.read_csv("output.csv")


file_uploader = st.file_uploader(":file_folder: upload a file", type=(["csv", "txt", "xlsx", "xls"]))
data = get_dataframe(file_uploader)

def display_candidate_profiles():
   st.title("Candidate Profiles")

   state_options = data['State Name'].unique()
   state = st.selectbox("Select State", state_options, index=None)

   if state:
       constituency_options = data[data['State Name'] == state]['Constitution Assembly'].unique()
       constituency = st.selectbox("Select Constituency", constituency_options, index=0)

       if constituency:
           filtered_data = data[(data['State Name'] == state) & (data['Constitution Assembly'] == constituency)]

           if 'Status' in filtered_data.columns:
               # external CSS for styling
               st.markdown("""
               <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">
               <style>
                   *{
                       margin: 0;
                       padding: 0;
                       box-sizing: border-box;
                           
                   }
                       
                     
                                       
                   .cand-container {
                       display: grid;
                       grid-template-columns: repeat(3, 1fr);
                       gap: .5rem;
                       
                   }
                   .cand-box {
                       background-color: rgb(255, 255, 255);
                       position: relative;
                       width: 98%;
                       box-shadow: rgb(210, 210, 210) 2px 2px 3px;
                       margin-left: .8rem;
                       min-height: 145px;
                       margin-bottom: 1.5rem;
                       display: block;
                   }

                   .cand-box figure {
                       width: 100px;
                       height: 100px;
                       border-radius: 50%;
                       display: block;
                       overflow: hidden;
                       border: 5px solid rgb(255, 255, 255);
                       text-align: center;
                       position: absolute;
                       top: 0px;
                       bottom: 0px;
                       margin: auto;
                       left: -2.5rem;
                       z-index: 2;
                       box-shadow: rgb(225, 225, 225) 1px 1px 1px;
                   }

                   .status {
                       display: flex;
                       justify-content: space-between;
                       background-color: #e3effd;
                       padding: 0.7rem 1.5rem 0.7rem 4.5rem;
                       font-size: .7rem;
                       font-weight: 200;
                       color: {text_color};
                   }

                   .nme-prty {
                       padding-left: 4.5rem;
                       margin-top: 1.15rem;                               
                   }


                       </style>
               """, unsafe_allow_html=True)
               # Display candidate cards in columns
               cols = st.columns(3)
               for index, candidate in filtered_data.iterrows():
                   col = cols[index % 3]
                   text_color = 'green' if str(candidate['Status']).lower() == 'won' else 'red'

                   col.markdown(f"""
                   <div class="cand-box">
                       <div class="cand-info">
                           <div class="status" style="color: {text_color};">
                               <div style="text-transform: capitalize; font-weight: bold;">{candidate['Status']}</div>
                               <div>{candidate['Obtained Votes']} <span>({candidate['Difference Votes']})</span></div>
                           </div>
                           <figure><img src="{candidate['Img urls']}" style="width: 100px; height: 100px; border-radius: 50%;"></figure>
                           <div class="nme-prty">
                               <h5 style=" font-size: .9rem;color: #004274;">{candidate['Candidate Name']}</h5>
                               <h6 style="font-size: .8rem;color: #0a8bfd;">{candidate['Party Name']}</h6>
                           </div>
                       </div>
                   </div>
                   """, unsafe_allow_html=True)

display_candidate_profiles()








