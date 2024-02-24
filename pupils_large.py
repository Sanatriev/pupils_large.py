import time
start=time.time()
class Pudil():
    def __init__(self,surname,name,mark):
        self.surname=surname
        self.name=name
        self.mark=mark

Best_pupils=[]
suma=0
amound=0
with open("pupils_large.txt","r",encoding="utf-8")as file:
    for line in file:
        line=line.split(" ")
        p=Pudil(line[0],line[1],int(line[2]))
        print(p.surname,p.name,"-",p.mark)
        


    if p.mark==5:
        Best_pupils.append(p.surname)
    amound+=1
    suma +=p.mark
print("Відміники:")
for i in Best_pupils:
    print(i)
n=suma/amound
print("Середня цінка класу:",n)
end=time.time()
print("Час виконаня:",end-start,"секунд")
