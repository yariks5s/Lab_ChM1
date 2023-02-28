# 4. Знайти найбiльший вiд’ємний корiнь нелiнiйного рiвняння x^3 + sin x−12x+ 1 = 0 методом
# релаксацiї, модифiкованним методом Ньютона та методом простої iтерацiї з точнiстю ε = 10−4
# Знайти апрiорну та апостерiорну оцiнку кiлькостi крокiв. Початковий промiжок та початкове
# наближення обрати однакове для обох методiв
# (якщо це можливо), порiвняти результати роботи методiв мiж собою.

from relaxation_method import iteration as relax_iter
from modified_newton_method import iteration as newton_iter
from simple_iteration_method import iteration as simple_iter

# Set start data
start_x = -3.75
iterations = 10
epsilon = 10**(-4)


print("Relaxation method:")
relax_result = relax_iter(start_x, iterations)

print("\n\nModified Newton method:")
newton_result = newton_iter(start_x, iterations)

print("\n\nSimple iteration method:")
simple_result = simple_iter(start_x, iterations)
