lb_to_g = ["lb", "g", "453.59237"]
lb_to_kg = ["lb", "kg", "0.45359237"]
kg_to_lb = ["kg", "lb", "2.20462262"]
kg_to_t = ["kg", "ton", "0.001"]
arr_metrics = ["lb", "g", "kg", "ton"]
operations = [lb_to_g, lb_to_kg, kg_to_lb, kg_to_t]

def askForMetric(str):
    while(True):
        x = input("Input %s: " %str)
        if x not in arr_metrics:
            print("Not a valid answer, try again.\n")
        else: return x 

def operate(oper, k):
    if oper[0] == operations[k][0] and oper[1] == operations[k][1]:
        print("New value is: %f" %(oper[2] * float(operations[k][2])))
        return 0
    if k != 0:
        operate(oper, k - 1)
    else:
        if oper[0] == "lb" and oper[1] == "ton":    # This part is a bit ugly
            print("New value is: %f" %((oper[2] * float(lb_to_kg[2])) * float(kg_to_t[2])))
            return 0
        print("There is no metric conversion for %s to %s in the system.\n" %(oper[0], oper[1]))
        exit()

og_metric = askForMetric("original metric")
new_metric = askForMetric("new metric")

while(True):
    try: 
        og_val = float(input("Input numerical value: "))
        break
    except:
        print("Value must be a number, try again.\n")

operand = [og_metric, new_metric, og_val]
k = len(operations) - 1
operate(operand, k)
