import numpy as np

def bottomRange(val, TA, B, s){
    return ((val-B)/(TA-B))**(s)
}

def upperRange(val, TA, U, t){
    return ((val-U)/(TA-U))**(t)
}

def dCal(val, TA, S, t){
    return ((val-S)/(TA-S))**(t)
}
def d(val, par){
    B = par[0]
    TA = par[1]
    U = par[2]
    s = par[3]
    t = par[4]

    if (U == Null){
        pass
    }
    
    if (B == Null){
        pass
    }

    if (val < B){
        return 0
    }
    if (val >= B and val <= U){
        if (val <= TA){
            return dCal(val, TA, B, s)
        }
        if (val > TA){
            return dCal(val, TA, U, t)
        }
    }
    if (val > U){
        return 0
    }

}

if(__name__ = "__main__" ):
    a = (B,TA,U,s,t)
    pass