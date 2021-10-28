from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
aantalMoves = 0
for i in range(4):
    aantalMoves += 1
    for c in range(0,i + 1):
        robotArm.grab()
        for d in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for f in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()