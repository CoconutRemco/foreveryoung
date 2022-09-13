from RobotArm import RobotArm
            
# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 4')
            
# Jouw python instructies zet je vanaf hier:
for i in range(3):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()

robotArm.moveRight()

for j in range(3):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()