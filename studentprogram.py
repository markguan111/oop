import StudentClass as sc


studentid = 1001
name = 'John'
dob = '1/1/2000'
classification = 'junior'

john = sc.student(studentid, name, dob, classification)


john.calc_age()


john.register()

print("student age is:", john.get_age())

print("student can register between:", john.get_registration())
