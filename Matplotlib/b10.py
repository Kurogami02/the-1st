import matplotlib.pyplot as plt
import numpy as np

divisions =["Div-A", "Div-B", "Div-C", "Div-D", "Div-E"]
divisions_average_marks =[70, 82, 73, 65, 68]
boys_average_marks=[68,67,77,61,70]

index=np.arange(5)
width=0.30


plt.bar(index, divisions_average_marks, width, color="blue", label="divisions marks")
plt.bar(index+width, boys_average_marks, width, color="orange", label="Boys marks")
plt.title("Horizontally Stacked Bar Graphs")

plt.ylabel("Marks")
plt.xlabel("Divisions")
plt.xticks(index+width/2, divisions)

plt.legend(loc="best")
plt.show()