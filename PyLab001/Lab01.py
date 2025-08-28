import math

# print (math.pi)
# Hello :3

radius = 5
area = math.pi * radius**2
print(area)

radius = 3
Volume_sphere = 4/3 * math.pi * radius**3
print(Volume_sphere)

Alpha = 3
Bravo = 4
Charlie_sq = Alpha**2 + Bravo**2
Charlie = int(math.sqrt(Charlie_sq))
print(Charlie)

My_Name = "M.N. Orban"
Name_len = len(My_Name)
print(Name_len)

#If I were still in the military my first name would be IT2
First_Initial = "M."
Middle_Initial = "N."
Last_Name = "Orban"
name_len = len(First_Initial) + len(Middle_Initial) + len(Last_Name)
print(name_len)

My_Name = First_Initial + Middle_Initial + " " + Last_Name
print(My_Name)

# this is functionally upper(My_Name)
My_Name_UC = My_Name.upper()
My_Name_LC = My_Name.lower()
print(My_Name_UC, My_Name_LC)

Age = 23
My_Height = 76
My_Weight = 200.0  #It's rude to ask
print(type(Age)), type(My_Weight), type(My_Height)
BMI = My_Weight / My_Height**2 * 703
print(BMI)

#I just wanted you to know that I considered learning how to make this play YouTube
#videos so that I could make the program play 'Modern Major General' when you hit run