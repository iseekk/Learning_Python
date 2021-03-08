with open("1_modules.txt", "r") as f:
    module_weights = [int(i.strip()) for i in f.readlines()]


def calc_fuel(mass):
    return mass // 3 - 2


total = 0

for module in module_weights:
    fuel = calc_fuel(module)
    extra_mass = fuel
    while True:
        extra_fuel = calc_fuel(extra_mass)
        if extra_fuel > 0:
            fuel += extra_fuel
            extra_mass = extra_fuel
            continue
        else:
            break
    total += fuel

print(total)