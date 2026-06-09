# Write a script that takes three test scores (e.g., 88, 92, 79)
# calculates their average as a float, and then explicitly converts that average into an integer. 
# Print both the float and integer averages.

score1, score2, score3 = 88, 92, 79

float_avg = (score1 + score2 + score3) / 3
int_avg = int(float_avg)

print("Float Average:", float_avg)
print("Integer Average:", int_avg)



# Create variables of type int, float, str, and bool. 
# Print each variable alongside its data type using the type() function.

a = 42
b = 3.14
c = "Python"
d = True

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))