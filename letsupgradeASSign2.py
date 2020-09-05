#LIST
lst=[1,7.7,"sammy","lets","upgrade"]

print(lst,"\n",lst[1] ,"\n",lst[3][2])

lst.append("ms dhoni")
print("updated list : ",lst)
print("position is of sammy is ",lst.index('sammy'))
print(lst[-1])
print(lst[1])
print(lst[-1][1])

# DICTIONARIES

dit={"name":"csk","captain":"ms dhoni","age":"39"}
print(dit,"\n",dit.get('name'),"\n",dit.items())
print(dit.keys())
print(dit.pop("name"))
print(dit)
dit["School"] = "MSD"
print(dit)

# SETS
st = {"csk","ms dhoni",7,5,3,2,4,7,8}
print(st)

st1 = {"csk",7}
print(st1.issubset(st))


# TUPLE

tup = ("mahi","@","@","MarRahaHai.in")
print(tup)
print(tup.count("@"))
print(tup.index("mahi"))

# BOOLEAN
a=True
b=False
print(a,b)

# STRINGS

a="sammy is awesome isnt it "
b="is"
print(a)
print(a.capitalize())
print(a.center(55))
print(a.count(b))
print(a.index(b))
print(a.upper())