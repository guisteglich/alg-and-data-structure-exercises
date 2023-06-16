# def timeConversion(s):
# s = '12:01:00PM'
# print(f"Horário: {s}")
# turno = s[-2:]
# print(f"O turno é: {turno}")
# hora = s[:-2].split(":")
# print(f"Split é: {hora}")

def timeConversion(s):
    turno = s[-2:]
    horario = s[:-2].split(":")
    
    if turno == 'PM':
        if int(horario[0]) == 12:
            return horario[0] + ":" + horario[1] + ":" + horario[2]
        hora = int(horario[0]) + 12
        return str(hora) + ":" + horario[1] + ":" + horario[2]
    else:
        if int(horario[0]) == 12:
            return '00:' + horario[1] + ":" + horario[2]
        return horario[0] + ":" + horario[1] + ":" + horario[2]


time1 = '07:05:45PM'
time2 = '12:01:00AM'
time3 = '03:34:08AM'
time4 = '12:45:54PM'

print(timeConversion(time1))
print(timeConversion(time2))
print(timeConversion(time3))
print(timeConversion(time4))

