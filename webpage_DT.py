import os
from os import chdir
import time
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import os.path
import numpy as np
import pandas as pd
import csv
import plotly as py
import plotly.graph_objs as go
import ipywidgets as widgets
py.offline.init_notebook_mode(connected=True)
import plotly.express as px
import streamlit as st

chdir(r'C:\Users\aksha\Documents\Digital_Twin_ACMV')
st.markdown("# Digital Twin Control for ACMV Systems")
st.markdown("## A prototype developed for a 40-seater food court")
st.markdown("""

    A digital twin model aims at assessing real-time exceedance of air quality criteria 
    (such as infection risk) due to occupancy and activities, and enhancing recovery via 
    ventilation control and other actions.

    We develop a Digital Twin Control (DTC) system that can optimize 
    the energy efficiency of air-conditioning and mechanical ventilation 
    (ACMV) systems while incorporating the ventilation requirements for 
    safe indoor air quality. 

    This live dashboard shows the proposed Digital-twin controlled infection risk of COVID-19
    over a period of one hour at the food court and compares it with the infection risk
    without the proposed control. Energy consumption is also shown for the scenarios. 
    You can find the article [here](https://www.overleaf.com/read/gvdwmyymtjsn).
    
""")
chdir(r'C:\Users\aksha\Documents\Digital_Twin_ACMV')
img = Image.open('foodcourt-layout.png')
st.image(img, caption='Foodcourt space and air-vents layout')
img = Image.open('foodcourt-seat-layout.png')
st.image(img, caption='Foodcourt seat layout')

placeholder1 = st.empty()
# placeholder2 = st.empty()

my_list = []
directory = r'C:\Users\aksha\Documents\Digital_Twin_ACMV\conc_control'
for filename in os.listdir(directory):
    my_list.append(filename.split("-")[-1].split(".")[0])
    
# print(my_list)
df = pd.read_csv(r'C:\Users\aksha\Documents\Digital_Twin_ACMV\data_control\probinf_timenorm.csv')
df_n = pd.read_csv(r'C:\Users\aksha\Documents\Digital_Twin_ACMV\data_nocontrol\probinf_timenorm.csv')
df_v = pd.read_csv(r'C:\Users\aksha\Documents\Digital_Twin_ACMV\data_control\inletvel.csv')
df_vn = pd.read_csv(r'C:\Users\aksha\Documents\Digital_Twin_ACMV\data_nocontrol\inletvel.csv')
df_e = pd.read_csv(r'C:\Users\aksha\Documents\Digital_Twin_ACMV\data_control\energyconsumption_timenorm.csv')
df_en = pd.read_csv(r'C:\Users\aksha\Documents\Digital_Twin_ACMV\data_nocontrol\energyconsumption_timenorm.csv')

x_coord = [1.4, 2.83, 7, 8.41, 12.57, 13.86, 18.1, 19.41, 23.62, 24.87]
z_coord = [4.38, 5.04, 8.49, 9.29]

for element in my_list:    
    index = my_list.index(element)
    
    with placeholder1.container():
        image_col, text_col = st.columns((1,1))
        # image_col.header("Computational-fluid-dynamics (CFD) based quanta concentration over time WITH proposed DTC")
        directory = r'C:\Users\aksha\Documents\Digital_Twin_ACMV\conc_control'
        chdir(directory)
        img1 = Image.open('conc-03032022-' + element + '.jpg')
        image_col.image(img1, caption='Computational-fluid-dynamics (CFD) based quanta concentration WITH proposed DTC at time' + " " + str(int(element) - 3600) + ' seconds')

        # text_col.header("Computational-fluid-dynamics (CFD) based quanta concentration over time WITHOUT proposed DTC")
        directory = r'C:\Users\aksha\Documents\Digital_Twin_ACMV\conc_nocontrol'
        chdir(directory)

        img2 = Image.open('conc-03032022-' + element + '.jpg')
        text_col.image(img2, caption='Computational-fluid-dynamics (CFD) based quanta concentration WITHOUT proposed DTC at time' + " " +  str(int(element) - 3600) + ' seconds')

        # time.sleep(.1)


# directory = r'C:\Users\aksha\Documents\Digital_Twin_ACMV\conc_control'
# chdir(directory)
# for filename in os.listdir(directory):
#     print(filename)
#     if filename.endswith(".jpg"):
#         img1 = Image.open(filename)
#         x1 = filename.split("-")
#         st.image(img1, caption='Quanta Concentration at time' + " " + x1[-1].split(".")[0] + 'seconds')
        



# with placeholder1.container():
#     image_col, text_col = st.columns((1,1))

#     with image_col:
#         st.header("Computational-fluid-dynamics (CFD) based quanta concentration over time with proposed DTC")
#         directory = r'C:\Users\aksha\Documents\Digital_Twin_ACMV\conc_control'
#         chdir(directory)
#         for filename in os.listdir(directory):
#             print(filename)
#             if filename.endswith(".jpg"):
#                 img = Image.open(filename)
#                 x = filename.split("-")
#                 st.image(img, caption='Quanta Concentration at time' + " " + x[-1].split(".")[0] + 'seconds')
#             # time.sleep(0.1)
        
#         # st.image("https://cdn-images-1.medium.com/max/906/1*dVSDol9pouoO9IX_E_-35Q.png")

#     with text_col:
#         # st.subheader("A Multi-page Interactive Dashboard with Streamlit and Plotly")
#         # st.write("""Beautiful interactive multipage dashboards are made easy with Streamlit
#         #     """)
#         # st.markdown("[Read more...](https://towardsdatascience.com/a-multi-page-interactive-dashboard-with-streamlit-and-plotly-c3182443871a)")

#         st.header("Computational-fluid-dynamics (CFD) based quanta concentration over time without proposed DTC")
#         directory = r'C:\Users\aksha\Documents\Digital_Twin_ACMV\conc_nocontrol'
#         chdir(directory)
#         for filename in os.listdir(directory):
#             print(filename)
#             if filename.endswith(".jpg"):
#                 img = Image.open(filename)
#                 x = filename.split("-")
#                 st.image(img, caption='Quanta Concentration at time' + " " + x[-1].split(".")[0] + 'seconds')
#             # time.sleep(0.1)
#     time.sleep(0.1)

# with st.container():
#     image_col, text_col = st.columns((3,1))
#     with image_col:
#         st.image("https://cdn-images-1.medium.com/max/906/1*hjhCIWGgLzOznTFwDyeIeA.png")

#     with text_col:
#         st.subheader("Rational UI Design with Streamlit")
#         st.write("""
#             From one point of view Streamlit is a retrograde step in web development because 
#             it lets you mix up the logic of your app with the way it is presented. But from 
#             another it is very much simplifying web design.""")
#         st.markdown("[Read more...](https://towardsdatascience.com/rational-ui-design-with-streamlit-61619f7a6ea4)")

        # x_coord = [1.4, 2.83, 7, 8.41, 12.57, 13.86, 18.1, 19.41, 23.62, 24.87]
        # z_coord = [4.38, 5.04, 8.49, 9.29]

        # df = pd.read_csv(r'C:\Users\aksha\Documents\Digital_Twin_ACMV\data_control\probinf_timenorm.csv')

        seat = {}
        count = 0
        for x in x_coord:
            for z in z_coord:
                
                seat[count] = df[(df['xcoord']==x) & (df['zcoord']==z)]
                count = count + 1

        seat[40] = seat[0].copy()
        seat[40]['probinf'] = 0.001

    # with st.container():
        ##Graph quadose conc
        x = seat[1]['endtime']

        layout = go.Layout(
            title='<b>Probablity of Infection with control</b>',
            yaxis=dict(
                title='<i>Probablity of Infection for past 300s</i>'
            ),
            xaxis=dict(
                title='<i>Time(s)</i>'
            )
        )


        # def update_plot(signals, freq):
            
        #     """
        #     This function updates the plot everytime a widget is changed
        #     """

        data = []
        for s in range(0,41):
            trace1 = go.Scatter(
                x=x,
                y=seat[s]['probinf'].iloc[0:int(index / 10) + 1],
                mode='lines',
                name='seat {}'.format(str(seat[s]['xcoord'].iloc[0]) + '_' + str(seat[s]['zcoord'].iloc[0])),
                line=dict(
                    shape='spline'
                )
            )
            data.append(trace1)

        fig = go.Figure(data=data, layout=layout)
        fig.add_trace(go.Scatter(x=seat[40]['endtime'], y=seat[40]['probinf'], marker=dict(color="#444"),
                                name='Infection Threshold', showlegend=True))
        fig.update_layout(yaxis_range=[0,0.01])
        # py.offline.iplot(fig)
        st.plotly_chart(fig,use_container_width = True)

        # signals = widgets.SelectMultiple(options=list(range(40)), value=(0, ), description='Seat Order')
        # freq = widgets.FloatSlider(min=1, max=20, value=1, description='Freq')
        # widgets.interactive(update_plot, signals=signals, freq=freq)

        # df = pd.read_csv(r'C:\Users\aksha\Documents\Digital_Twin_ACMV\data_nocontrol\probinf_timenorm.csv')

        seat = {}
        count = 0
        for x in x_coord:
            for z in z_coord:
                
                seat[count] = df_n[(df_n['xcoord']==x) & (df_n['zcoord']==z)]
                count = count + 1

        seat[40] = seat[0].copy()
        seat[40]['probinf'] = 0.001

    # with st.container():
        ##Graph quadose conc
        x = seat[1]['endtime']

        layout = go.Layout(
            title='<b>Probablity of Infection without control</b>',
            yaxis=dict(
                title='<i>Probablity of Infection for past 300s</i>'
            ),
            xaxis=dict(
                title='<i>Time(s)</i>'
            )
        )


        # def update_plot(signals, freq):
            
        #     """
        #     This function updates the plot everytime a widget is changed
        #     """

        data = []
        for s in range(0,41):
            trace1 = go.Scatter(
                x=x,
                y=seat[s]['probinf'].iloc[0:int(index / 10) + 1],
                mode='lines',
                name='seat {}'.format(str(seat[s]['xcoord'].iloc[0]) + '_' + str(seat[s]['zcoord'].iloc[0])),
                line=dict(
                    shape='spline'
                )
            )
            data.append(trace1)

        fig = go.Figure(data=data, layout=layout)
        fig.add_trace(go.Scatter(x=seat[40]['endtime'], y=seat[40]['probinf'], marker=dict(color="#444"),
                                name='Infection Threshold', showlegend=True))
        fig.update_layout(yaxis_range=[0,0.01])
        # py.offline.iplot(fig)
        st.plotly_chart(fig,use_container_width = True)

        # signals = widgets.SelectMultiple(options=list(range(40)), value=(0, ), description='Seat Order')
        # freq = widgets.FloatSlider(min=1, max=20, value=1, description='Freq')
        # widgets.interactive(update_plot, signals=signals, freq=freq)
#Velocity
        trace0 = go.Scatter(
            # x = df_v['endtime'],
            x = seat[1]['endtime'],
            y = df_v['velocity'].iloc[0:int(index / 10) + 1],
            name='control'
        )
        trace1 = go.Scatter(
            # x = df_v['endtime'],
            x = seat[1]['endtime'],
            y = df_vn['velocity'].iloc[0:int(index / 10) + 1],
            name = 'without control'
        )
        data1 = [trace0, trace1]
        layout2 = go.Layout(title = "Inlet Air Velocity with and without control", xaxis = {'title':'time(s)'}, yaxis = {'title':'Velocity (m/s)'})
        fig = go.Figure(data = data1, layout = layout2)
        # fig.show()
        st.plotly_chart(fig,use_container_width = True)

#Energy consumption
        trace0 = go.Scatter(
            x = df_e['endtime'],
            # x = seat[1]['endtime'],
            y = df_e['enconsum'].iloc[0:int(index / 10) + 1],
            name='control'
        )
        trace1 = go.Scatter(
            x = df_e['endtime'],
            # x = seat[1]['endtime'],
            y = df_en['enconsum'].iloc[0:int(index / 10) + 1],
            name = 'without control'
        )
        data1 = [trace0, trace1]
        layout2 = go.Layout(title = "Energy Consumption with and without control", xaxis = {'title':'time(s)'}, yaxis = {'title':'Energy (Wh)'})
        fig = go.Figure(data = data1, layout = layout2)
        # fig.show()
        st.plotly_chart(fig,use_container_width = True)

        time.sleep(.1)