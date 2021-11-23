import pandas as pd
import plotly.figure_factory as ff
import csv 
import statistics


df = pd.read_csv("StudentsPerformance.csv")
maths = df["math score"].tolist()

mean = statistics.stdev(maths)
std_deviation = statistics.stdev(maths)


first_std_deviation_start,first_std_deviation_end = mean - std_deviation,mean+std_deviation
print(f"First (start)- {first_std_deviation_start}, First (end)- {first_std_deviation_end},")

second_std_deviation_start,second_std_deviation_end = mean -(2*std_deviation) , mean + ( 2*std_deviation)
print(f"Second (start)- {second_std_deviation_start}, Second (end)- {second_std_deviation_end},")

third_std_deviation_start,third_std_deviation_end = mean -(3*std_deviation) , mean + ( 3*std_deviation)
print(f"Third (start)- {third_std_deviation_start}, Third (end)- {third_std_deviation_end},")

print()
fig = ff.create_distplot([maths],["Maths"],show_hist=False)
fig.show()
