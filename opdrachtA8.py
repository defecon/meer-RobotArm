from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
RobotArm.speed = 3
i = 0
robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    for c in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for d in range(8):
        robotArm.moveLeft()





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()