#physics and math calculator
import math, sys
mathorphysics = " "

while mathorphysics != "Physics" or mathorphysics != "physics"  or mathorphysics != "math" or mathorphysics != "Math":
    mathorphysics = input("Do you need to calculate math or physics: ")
    
    if mathorphysics == "Physics" or mathorphysics == "physics": #physics portion
        
        physics = " "
        
        while physics != "End":
            physics = input("What do you need to calcuate: ")

            if physics == "Force" or physics == "force":
                acceleration = int(input("What is your acceleration: "))
                mass = int(input("What is your mass: "))
                force = acceleration + mass
                print(f"{force} kgs") 

            elif physics == "Acceleration" or physics == "acceleration":
                velocity = int(input("What is your velocity: "))
                time = int(input("What is your time: "))
                acceleration = velocity/time
                print(f"{acceleration} M/s")
        
            elif physics == "Velocity" or physics == "velocity":
                finalTime = int(input("what is the final time: "))
                initalTime = int(input("what was the initial time"))
                finalPosition = int(input("what was the final position"))
                initalPosition = int(input("what was the inital position"))
                time = finalTime - initalTime
                position = finalPosition - initalPosition
                timeposition = position/time
                print(f"{timeposition} M/s")

            elif physics == "Energy":
                m = int(input("What is the mass"))
                c = 3 * 10**8
                e == ((m*c) **2)
                print(f"E = {e}")

            elif physics == "end":
                break

            else:
                print("invalid")
                print("try again")


    elif mathorphysics == "Math" or mathorphysics == "math": #math portion
        math = " "  
        while math != "End" or math != "end" or math != "END":
            math = input("What do you need to calculate: ") 

            if math == "Slope" or math == "slope":
                m1 = int(input("What is the rise: "))
                m2 = int(input("What is the run"))
                m = m1/m2
                b = int(input("What is the why intercept: "))
                print(f"y = {m}x + {b}")       
            
            elif math == "radius" or math == "Radius":
                diameter = int(input("What is the diameter: "))
                radius = diameter/2
                print(f"Radius of {radius} units")

            elif math == "Diameter":
                radius = int(input("What is your radius"))
                diameter = radius * 2
                print(f"Diameter of {diameter} units")

            elif math == "area of circle":
                radius = int(input("What is the radius: "))
                area = (math.pi * (radius ** 2))
                areanopi = area/math.pi
                print(f"area of {area} units or {areanopi} π units")

            elif math == "end":
                break

            else:
                print("Invalid")
                print("Try again")

    elif mathorphysics == "End":
        sys.exit()

    else:
        print("Invalid, maybe you made a typo ")
        print("Otherwise try again next update")            
