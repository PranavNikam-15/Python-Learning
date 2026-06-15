# Demonstrate variable scope by defining a global variable score = 100, 
# then writing a function that modifies a local variable score = 50, 
# printing both to show isolation.


score = 100

def check_scope():
    score = 50
    print("Local score inside function:", score)

check_scope()
print("Global score outside function:", score)