from complex import Complex

z = Complex(2, 4) # Complex numbers from our Class
y = Complex(1, 3)

z_py = complex(2, 4) # Complex numbers from python builtin
y_py = complex(1, 3)

# Function to normalize the pythons built in since it returns with j and parenthesis around
def normalize(c: str):
    if isinstance(c, complex): #to round pythons built ins because they have floating point error
        real = round(c.real, 8)
        imag = round(c.imag, 8)

        #Turn them back to integers if they can
        if real == int(real):
            real = int(real)

        if imag == int(imag):
            imag = int(imag)

        return f"{real}+{imag}i" if imag >= 0 else f"{real}{imag}i"
    
    return str(c).strip("()").replace('j', 'i')


# Header
col_width = 20
print("the complex numbers are: z = 2 + 4i and y = 1 + 3i")
print(f"{'Operation' :>{col_width}}", f"{'python built in' :>{col_width}}", f"{'ours' :>{col_width}}", f"{'matching:' :>{col_width}}")
print("-" * col_width*5)

# Below we get results from our class and the python built in and print the results with an "y" if ours and pythons match, and an "x" if they don't
result_py = z_py + y_py
result_our = z + y
match = "yes" if str(normalize(result_py)) == str(result_our) else "no"
print(f"{'z + y':>{col_width}}", f"{str(normalize(result_py)):>{col_width}}", f"{str(result_our):>{col_width}}", f"{str(match):>{col_width}}")

result_py = z_py - y_py
result_our = z - y
match = "yes" if str(normalize(result_py)) == str(result_our) else "no"
print(f"{'z - y':>{col_width}}", f"{str(normalize(result_py)):>{col_width}}", f"{str(result_our):>{col_width}}", f"{str(match):>{col_width}}")

result_py = z_py * y_py
result_our = z * y
match = "yes" if str(normalize(result_py)) == str(result_our) else "no"
print(f"{'z * y':>{col_width}}", f"{str(normalize(result_py)):>{col_width}}", f"{str(result_our):>{col_width}}", f"{str(match):>{col_width}}")

result_py = z_py + 3
result_our = z + 3
match = "yes" if str(normalize(result_py)) == str(result_our) else "no"
print(f"{'z + 3':>{col_width}}", f"{str(normalize(result_py)):>{col_width}}", f"{str(result_our):>{col_width}}", f"{str(match):>{col_width}}")

result_py = z_py * 3
result_our = z * 3
match = "yes" if str(normalize(result_py)) == str(result_our) else "no"
print(f"{'z * 3':>{col_width}}", f"{str(normalize(result_py)):>{col_width}}", f"{str(result_our):>{col_width}}", f"{str(match):>{col_width}}")

result_py = z_py == 3
result_our = z == 3
match = "yes" if str(normalize(result_py)) == str(result_our) else "no"
print(f"{'z == y':>{col_width}}", f"{str(normalize(result_py)):>{col_width}}", f"{str(result_our):>{col_width}}", f"{str(match):>{col_width}}")

result_py = z_py != 3
result_our = z != 3
match = "yes" if str(normalize(result_py)) == str(result_our) else "no"
print(f"{'z != y':>{col_width}}", f"{str(normalize(result_py)):>{col_width}}", f"{str(result_our):>{col_width}}", f"{str(match):>{col_width}}")


result_py = z_py / y_py
result_our = z / y
match = "yes" if str(normalize(result_py)) == str(result_our) else "no"
print(f"{'z / y':>{col_width}}", f"{str(normalize(result_py)):>{col_width}}", f"{str(result_our):>{col_width}}", f"{str(match):>{col_width}}")