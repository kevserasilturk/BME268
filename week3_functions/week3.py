def greet(name):
    print("Hello", name)

def add(a, b):
    return a + b

def compute_pay(hours, rate):
    if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    else:
        return hours * rate

# CALL (EN ÖNEMLİ KISIM)
greet("Kevser")

print("Sum:", add(3, 5))

print("Pay:", compute_pay(45, 10))