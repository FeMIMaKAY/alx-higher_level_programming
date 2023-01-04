#!/usr/bin/python3
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{:d} is positive".format(number))
elif number == 0:
<<<<<<< HEAD
    print("{} is zero".format(number))
elif number < 0:
    print("{} is negative".format(number))
=======
    print("{:d} is zero".format(number))
else:
    print("{:d} is negative".format(number))
>>>>>>> 283657ceb70093bb9377fb8148bfe99979a63cff
