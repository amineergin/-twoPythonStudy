students = ["Amine", "Melike", "Zehra", "Simge", "Kübra", "Beyza", "Ece", "Ecenur", "Erva", "Doğa", "Gülsüm", "Zeynep"]
result_of_lists = [[],[]]
for index, student in enumerate(students):
    if index % 2 == 0:
        result_of_lists[0].append(student)
    else:
        result_of_lists[1].append(student)

print(result_of_lists)