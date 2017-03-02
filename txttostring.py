#Txt to single string

def txttostring(x):
    f=open(x)
    u=f.read().replace('\n','')
    return u

