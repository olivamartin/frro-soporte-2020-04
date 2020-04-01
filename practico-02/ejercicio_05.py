import ejercicio_04 as ej4

def EstudiantesDicc(listaEstudiantes):
  d = {}
  for s in listaEstudiantes:
    if s.nombre_carrera not in d.keys():
      d[s.nombre_carrera] = 0
      d[s.nombre_carrera] += 1
    else:
      d[s.nombre_carrera] += 1
  print(d)

e1 = ej4.Estudiante('Gastón',20,'M','80',1.88,'Ingeniería en Sistemas',2017,41,25)
e2 = ej4.Estudiante('Martín',21,'M','85',1.78,'Ingeniería en Sistemas',2017,41,25)
e3 = ej4.Estudiante('Lucía',19,'M','85',1.78,'Ingeniería Civil',2017,35,15)
e4 = ej4.Estudiante('Marta',25,'M','85',1.78,'Ingeniería Química',2017,34,31)
estudiantes = {e1,e2,e3,e4}
EstudiantesDicc(estudiantes)