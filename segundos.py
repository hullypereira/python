segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_str = input(segundos_str)

horas = total_str // 3600
segs_restantes = total_str % 3600
minutos = segs_restantes // 60
segs_restantes_finais = segs_restantes % 60

print(horas, "horas, ", minutos, segs_restantes_finais, "segundos") 
