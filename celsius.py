temp = input  ("Imput the tempurture  you like to convert? (e.g., 45f, 102c etc.) : ")
degree = int(temp[: _1])
i_convention = temp[-1]
if i_convention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"
elif i_convention.upper() =="F":
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "Celsius"
else:
    print("input proper conventqion.")
    quit()
print("the temperture in", o convention, "is" , result, "degrees.")
