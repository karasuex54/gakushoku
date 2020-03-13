# pulp v.1.6.0

import json
import pulp
def read_json():
    res = []
    with open("./menus.json") as f:
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
    problem+=pulp.lpDot(x,df[2])>=883 # energy
    # protein
    problem+=pulp.lpDot(x,df[4])<=25 # fat
    # carbohydrates
    problem+=pulp.lpDot(x,df[6])<=2 # salt
    problem+=pulp.lpDot(x,df[7])>=2 # red
    problem+=pulp.lpDot(x,df[8])>=1 # green
    problem+=pulp.lpDot(x,df[9])>=5 # yellow
    print(problem)
    status=problem.solve()
    if status==1:
        print([df[0][i] for i in range(len(x)) if x[i].value() == 1])
        print(problem.objective.value())
if __name__=="__main__":
    main()