# Import Entire Module
import Modules_1
Modules_1.say_hello("Pranav")
print("PI value:", Modules_1.pi)


# Import Specific Items
from Modules_1 import say_hello, pi
say_hello("Ruchir")
print("PI:", pi)


# Import Module with Alias
import Modules_1 as M1
M1.say_hello("Alias Call")
print("Alias PI:", M1.pi)


# Import Specific Items With Alias
from Modules_1 import say_hello as greet, pi as PI
greet("friend!")
print("PI Alias:", PI)