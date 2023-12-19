lb_to_g = ["lb", "g", "453.59237"]
lb_to_kg = ["lb", "kg", "0.45359237"]
kg_to_lb = ["kg", "lb", "2.20462262"]
kg_to_t = ["kg", "ton", "0.001"]
arr_metrics = ["lb", "g", "kg", "ton"]
operations = [-1, lb_to_kg, kg_to_t, -1, kg_to_lb, lb_to_g]

#   g ->(-1) lb -> kg -> t ->(-1) kg -> lb -> g

def askForMetric(str):
    while(True):
        x = input("Input %s: " %str)
        if x not in arr_metrics:
            print("Not a valid answer, try again.\n")
        else: return x 

def operate(operand):
    k = len(operations)
    for i in range(k):
        if i % 3 == 0:
            if operand[0] == operations[k - 1 - i][1]:
                operand[0] = operations[k - 1 - i][0]
                operand[2] = operand[2] * (float(operations[k - 1 - i][2]) ** (-1))
            if operand[0] == operand[1]:
                print("New value is: %f" %operand[2])
                return 0
        else:
            if operand[0] == operations[i][0]:
                operand[0] = operations[i][1]
                operand[2] = operand[2] * (float(operations[i][2]))
            if operand[0] == operand[1]:
                print("New value is: %f" %operand[2])
                return 0
            
og_metric = askForMetric("original metric")
new_metric = askForMetric("new metric")

while(True):
    try: 
        og_val = float(input("Input numerical value: "))
        break
    except:
        print("Value must be a number, try again.\n")

operand = [og_metric, new_metric, og_val]

operate(operand)