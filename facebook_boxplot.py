import matplotlib.pyplot as plt
import csv

data = []
with open('dataset_Facebook.csv') as csvfile:
    reader1 = csv.reader(csvfile,delimiter=';')
    for row in reader1:
        try:
            data.append(int(row[5]))
        except ValueError:
            print("ignoring the column title")
print(data)

fig,ax1 = plt.subplots(figsize=(10,9))
ax1.set_xlabel('Posts per Hour')
plt.boxplot(data,vert=0)
plt.show()