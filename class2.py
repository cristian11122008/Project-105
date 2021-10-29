import csv
import pandas as pd
import plotly.express as px
with open ("class2.csv", newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
totalmarks=0
totalentery=len(file_data)
for marks in file_data:
    totalmarks=totalmarks+float(marks[1])

mean=totalmarks/totalentery
print(str(mean))
df=pd.read_csv("class2.csv")
fig=px.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[dict(
    type="line",
    y0=mean,
    y1=mean,
    x0=0,
    x1=totalentery
)])
fig.show()
