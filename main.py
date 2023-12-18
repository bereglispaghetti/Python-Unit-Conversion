lb_to_g = ["lb", "g", "453.59237"]
lb_to_kg = ["lb", "kg", "0.45359237"]
kg_to_lb = ["kg", "lb", "2.20462262"]
kg_to_t = ["kg", "ton", "0.001"]
arr_metrics = ["lb", "g", "kg", "ton"]

def askForMetric(str):
    while(True):
        x = input("Input %s: " %str)
        if x not in arr_metrics:
            print("Not a valid answer, try again.\n")
        else: return x 

og_metric = askForMetric("original metric")
new_metric = askForMetric("new metric")

while(True):
    try: 
        og_val = float(input("Input numerical value: "))
        break
    except:
        print("Value must be a number, try again.\n")
