# Time: O(n) | Space: O(1)

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            continue

        remainder = grades[i] % 5

        if remainder >= 3:
            grades[i] += 5 - remainder

    return grades
