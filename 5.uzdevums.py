import datetime

pašreizējā_stunda = datetime.datetime.now().hour

if pašreizējā_stunda < 12:
    print("Labrit!")
elif pašreizējā_stunda < 18:
    print("Labdien!")
else:
    print("Labvakar!")