try:
    print(10/"0")
except ZeroDivisionError:
    print("Not divisible by Zero")
except TypeError:
    print("Error: Invalid Type")
except Exception:
    print("Something went wrong")

print("Done")

