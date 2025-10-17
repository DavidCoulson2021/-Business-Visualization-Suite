import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# 1. Circular Bar Plot
categories = ['Sales', 'Marketing', 'Operations', 'HR', 'R&D', 'Finance']
values = [78, 65, 82, 58, 70, 88]
theta = [i * (360 / len(categories)) for i in range(len(categories))]

fig1 = go.Figure()
fig1.add_trace(go.Barpolar(
    r=values,
    theta=theta,
    marker_color=px.colors.qualitative.Plotly,
    marker_line_color="black",
    marker_line_width=1,
    opacity=0.8,
    name='Category'
))
fig1.update_layout(title='Circular Bar Plot', polar=dict(bgcolor='white'), showlegend=True, template='plotly_white')

# 2. Dumbbell Chart
before = [60, 50, 70, 45, 65, 75]
after = [78, 65, 82, 58, 70, 88]

fig2 = go.Figure()
for i, cat in enumerate(categories):
    fig2.add_trace(go.Scatter(
        x=[before[i], after[i]],
        y=[cat, cat],
        mode='lines+markers',
        line=dict(color='gray', width=2),
        marker=dict(size=10),
        name=cat
    ))
fig2.update_layout(title='Dumbbell Chart', xaxis_title='Value', yaxis_title='Category', template='plotly_white')

# 3. Sunburst Chart
labels = ["Company","Sales","Marketing","Operations","HR","R&D","Finance","North","South","East","West"]
parents = ["","Company","Company","Company","Company","Company","Company","Sales","Sales","Marketing","Marketing"]
values_sunburst = [0,0,0,0,0,0,0,40,38,35,30]

fig3 = go.Figure(go.Sunburst(labels=labels, parents=parents, values=values_sunburst, branchvalues="total"))
fig3.update_layout(title='Sunburst Chart', template='plotly_white')

# 4. Treemap
fig4 = go.Figure(go.Treemap(labels=categories, parents=[""] * len(categories), values=values))
fig4.update_layout(title='Treemap Chart', template='plotly_white')

# 5. Marimekko Chart
segment = ['Product1','Product1','Product2','Product2']
channel = ['Online','Retail','Online','Retail']
value_mari = [30,70,40,60]
df_mari = pd.DataFrame({'Segment': segment, 'Channel': channel, 'Value': value_mari})
fig5 = px.bar(df_mari, x='Segment', y='Value', color='Channel', title='Marimekko Chart', template='plotly_white')

# 6. Calendar Heatmap
dates = pd.date_range(start='2025-01-01', periods=12)
values_heat = [5,6,8,2,7,3,6,9,4,5,7,8]
df_heat = pd.DataFrame({'Date': dates, 'Value': values_heat})
fig6 = px.density_heatmap(df_heat, x='Date', y='Value', title='Calendar Heatmap', template='plotly_white')

# 7. Streamgraph
months = ['Jan','Feb','Mar','Apr','May','Jun']
genreA = [10,12,8,15,9,11]
genreB = [5,7,6,8,5,6]
genreC = [3,4,2,5,3,4]
df_stream = pd.DataFrame({'Month': months, 'GenreA': genreA, 'GenreB': genreB, 'GenreC': genreC})
fig7 = px.area(df_stream, x='Month', y=['GenreA','GenreB','GenreC'], title='Streamgraph', template='plotly_white')

# 8. Animated Scatter Plot
years = [2018,2019,2020,2021,2022]*3
revenue = [50,60,55,65,70,40,45,50,60,55,30,35,40,45,50]
profit = [5,6,5,7,8,4,5,5,6,7,3,4,4,5,6]
company = ['A']*5 + ['B']*5 + ['C']*5
df_anim = pd.DataFrame({'Year': years, 'Revenue': revenue, 'Profit': profit, 'Company': company})
fig8 = px.scatter(df_anim, x='Revenue', y='Profit', color='Company', animation_frame='Year', title='Animated Scatter Plot', template='plotly_white')

# 9. Static Scatter Plot
fig9 = px.scatter(df_anim, x='Revenue', y='Profit', color='Company', title='Static Scatter Plot', template='plotly_white')

# 10. Polar Area Plot
fig10 = go.Figure()
for i, cat in enumerate(categories):
    fig10.add_trace(go.Barpolar(
        r=[values[i]],
        theta=[i * (360 / len(categories))],
        name=cat,
        marker_color=px.colors.qualitative.Plotly[i]
    ))
fig10.update_layout(title='Polar Area Chart of Business Categories', polar=dict(bgcolor='white'), showlegend=True, template='plotly_white')

# 11. Bullet Chart
targets = [80,70,85,60,75,90]
fig11 = go.Figure()
for i, cat in enumerate(categories):
    fig11.add_trace(go.Bar(x=[targets[i]], y=[cat], orientation='h', marker=dict(color='lightgray'), showlegend=False))
    fig11.add_trace(go.Bar(x=[values[i]], y=[cat], orientation='h', marker=dict(color='steelblue'), name=cat))
fig11.update_layout(title='Bullet Chart — KPI Tracking', barmode='overlay', template='plotly_white')

# 12. Chord Diagram (Simulated)
source = ['A','A','B','C']
target = ['B','C','D','A']
value_chord = [5,10,7,3]
df_chord = pd.DataFrame({'Source': source, 'Target': target, 'Value': value_chord})
nodes = sorted(set(source + target))
node_indices = {node: i for i, node in enumerate(nodes)}
angle = 2 * np.pi / len(nodes)
positions = {node: (np.cos(i * angle), np.sin(i * angle)) for i, node in enumerate(nodes)}

node_trace = go.Scatter(
    x=[positions[node][0] for node in nodes],
    y=[positions[node][1] for node in nodes],
    mode='markers+text',
    marker=dict(size=20, color=list(range(len(nodes))), colorscale='Viridis'),
    text=nodes,
    textposition='top center',
    hoverinfo='text'
)

edge_traces = []
for _, row in df_chord.iterrows():
    x0, y0 = positions[row['Source']]
    x1, y1 = positions[row['Target']]
    cx, cy = (x0 + x1)/2, (y0 + y1)/2 + 0.2
    t = np.linspace(0, 1, 100)
    bez_x = (1 - t)**2 * x0 + 2 * (1 - t) * t * cx + t**2 * x1
    bez_y = (1 - t)**2 * y0 + 2 * (1 - t) * t * cy + t**2 * y1
    edge_traces.append(go.Scatter(x=bez_x, y=bez_y, mode='lines',
        line=dict(width=row['Value'], color='rgba(100,100,100,0.5)'), hoverinfo='none'))

fig12 = go.Figure(edge_traces + [node_trace])
fig12.update_layout(title='Chord Diagram Simulation',
    xaxis=dict(showgrid=False, zeroline=False, visible=False),
    yaxis=dict(showgrid=False, zeroline=False, visible=False),
    plot_bgcolor='white',
    showlegend=False,
    margin=dict(t=40, b=0, l=0, r=0)
)

