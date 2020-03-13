# pulp v.1.6.0
## -*- coding: utf-8 -*-
import json
import pulp
import codecs

def read_json():
    res = []
    with codecs.open("./menus.json","r","utf-8") as f:
        df = json.load(f)
    N = len(df)
    menu_names = []
    price = []
    energy = []
    protein = []
    fat = []
    carbohydrates = []
    salt = []
    red = []
    green = []
    yellow = []
    d = ["menu_name","price","energy","protein","fat","carbohydrates","salt","red","green","yellow"]
    for i in range(N):
        s = str(i)
        menu_names.append(df[s][d[0]])
        price.append(df[s][d[1]])
        energy.append(df[s][d[2]])
        protein.append(df[s][d[3]])
        fat.append(df[s][d[4]])
        carbohydrates.append(df[s][d[5]])
        salt.append(df[s][d[6]])
        red.append(df[s][d[7]])
        green.append(df[s][d[8]])
        yellow.append(df[s][d[9]])
    return N,[menu_names,price,energy,protein,fat,carbohydrates,salt,red,green,yellow]
def main():
    N,df = read_json()
    
    problem = pulp.LpProblem("Problem-2",pulp.LpMinimize)
    x = [pulp.LpVariable("x{}".format(str(i)),cat="Binary") for i in range(N)]
    print(x)
    print(df[1])
    problem+=pulp.lpDot(x,df[1])
    cate = {2:"energy",3:"protein",4:"fat",5:"carbohydrates",6:"salt",7:"red",8:"green",9:"yellow"}
    for i in range(2,10):
        print(cate[i])
        l,r = map(float,input().split())
        problem+=pulp.lpDot(x,df[i])>=l
        problem+=pulp.lpDot(x,df[i])<=r
    print(problem)
    status=problem.solve()
    if status==1:
        print([df[0][i] for i in range(len(x)) if x[i].value() == 1])
        print(problem.objective.value())
    else:
        print("not solve")
if __name__=="__main__":
    main()