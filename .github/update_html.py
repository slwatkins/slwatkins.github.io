#!/usr/bin/env python3

import plotly.express as px
import plotly.graph_objects as go
import covid
import pandas as pd
from scipy import signal
import numpy as np

df = covid.get_data()

# total cases plot via plotly

fig = px.line(
    df[df['county'].isin(covid._io.BAYAREA_COUNTIES)],
    x='date',
    y="cases",
    color='county',
    color_discrete_sequence=px.colors.qualitative.Set1,
    labels={
        "county": "County",
        "date": "",
        "cases": "Total Cases",
    },
    template='none',
)
fig.update_xaxes(showline=True, linecolor='black', mirror=True, ticks='inside')
fig.update_yaxes(showline=True, linecolor='black', mirror=True, ticks='inside')
fig.write_html('covid/total_cases_by_county.html')

# cases per day plot via plotly

fig = go.Figure()

vals = [0, 1, 2, 3, 4]
ncounties = len(covid._io.BAYAREA_COUNTIES)

colors = px.colors.qualitative.Set1[:ncounties]

for ii, county in enumerate(covid._io.BAYAREA_COUNTIES):

    df_temp = df[df['county'] == county]
    cases_per_day = np.concatenate(([0], np.diff(df_temp.cases)))

    for val in vals:
        if val > 0:
            cases = signal.savgol_filter(
                cases_per_day,
                val * 7 + np.mod(val * 7 + 1, 2),
                3,
            )
        else:
            cases = cases_per_day
        
        fig.add_trace(
            go.Scatter(
                visible=False,
                line=dict(color=colors[ii]),
                name=county,
                x=df_temp.date,
                y=cases,
            )
        )

for item in fig.data[::len(vals)]:
    item.visible=True


steps = []
for i in range(len(vals)):
    step = dict(
        method="update",
        label=f"{i} Weeks" if i != 1 else f"{i} Week",
        args=[{"visible": [False] * len(fig.data)},
              ],  # layout attribute
    )
    for jj in range(i, len(fig.data), len(vals)):
        step["args"][0]["visible"][jj] = True
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Filter Window: "},
    steps=steps,
    pad={'t': 50},
)]

fig.update_layout(
    sliders=sliders,
    legend_title={'text': 'County'},
    template='none',
    height=650,
)

fig.update_xaxes(
    showline=True,
    linecolor='black',
    mirror=True,
    ticks='inside',
)
fig.update_yaxes(
    showline=True,
    linecolor='black',
    mirror=True,
    ticks='inside',
    title='New Cases per Day',
)

fig.write_html('covid/total_cases_by_county.html')

