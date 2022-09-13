print("Welke dag van de week is het? MA DI WO DO VR ZA ZO?")
dag = input()
if dag == 'MA':
    dag = 1
if dag == 'DI':
    dag = 2
if dag == 'WO':
    dag = 3
if dag == 'DO':
    dag = 4
if dag == 'VR':
    dag = 5
if dag == 'ZA':
    dag = 6
if dag == 'ZO':
    dag = 7



x = 7

while x > 0:
    print(x)
    x -= 1



    if x == dag:
        if dag == 1:
            dag = 'MA'
        if dag == 2:
            dag = 'DI'
        if dag == 3:
            dag = 'WO'
        if dag == 4:
            dag = 'DO'
        if dag == 5:
            dag = 'VR'
        if dag == 6:
            dag = 'ZA'
        if dag == 7:
            dag = 'ZO'
        print('Het is! ' + str(dag))
        