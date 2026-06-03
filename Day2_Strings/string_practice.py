print("Prob 1 :- Upper & Lower Case")
name = 'Rudra'
print(name.upper())
print(name.lower())
print("")

print("Prob 2 :- First & Last Character")
print(name[0])
print(name[-1])
print("")

print("Prob 3 :- Replace Spaces")
text = " Hello World "
print(text)
new_text = text.replace(' ','_')
print(new_text)
print("")

print("Prob 4 :- Character Counter")
print(len(name))
print("")

print("Prob 5 :- Reverse a Word")
print(name[::-1])

print("prob 5 :- Reverse a Word")
reverse = ''
for i in range(len(name)-1,-1,-1):
    reverse += name[i]
print(reverse)

