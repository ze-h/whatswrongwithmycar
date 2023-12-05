from Problems import VehicleIssues

v = VehicleIssues

def mod_issue(q, a):
    match q:
        case 1:
            if a == 1:
                v.modify(v, "sample problem", 0.2)
            else:
                v.modify(v, "sample problem", -1)
        case 1.1:
            if a == 0:
                v.modify()
            elif a == 1:
                v.modify()
        case 1.11:
            if a == 0:
                v.modify()
            elif a == 1:
                v.modify()
        
            

