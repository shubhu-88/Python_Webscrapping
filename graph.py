import matplotlib.pyplot as plt
import csv

x=[]
y=[]
year=[]

with open('output.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append(row[5])
        x.append(row[10])
        year.append(row[11])

x.pop(0)
y.pop(0)
year.pop(0)

plt.scatter(y,x,90,marker='o',color='purple')

plt.title('District vs Autonomy_Status (Whose all details are fetched completly)')

plt.ylabel('Autonomy Status')
plt.xlabel('District')
plt.xticks(rotation='vertical')
plt.show()

l=sorted(list(set(y)))
r=[]
for i in l:
    r.append(y.count(i))

k=dict.fromkeys(list(set(y)),0)
for i,j in k.items():
    k[i]=y.count(i)

   
plt.bar(l,r,.35,color='purple')
plt.title('No of colleges vs District (whose all details are fetched completly)')
plt.ylabel('No of colleges')
plt.xlabel('District')
plt.xticks(rotation='vertical')
plt.show()

z=sorted(list(set(year)))
yr=[]
for i in z:
    yr.append(year.count(i))

plt.bar(z,yr,.35,color='purple')
plt.title('No of colleges vs Year of establishment (whose all details are fetched completly)')
plt.ylabel('No of colleges')
plt.xlabel('Year of establishment')
plt.xticks(rotation='vertical')
plt.show()   



    
