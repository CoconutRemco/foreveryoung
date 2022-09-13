from RobotArm import RobotArm
            
# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 6')
            
# Jouw python instructies zet je vanaf hier:

for i in range(7):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for j in range(7):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()