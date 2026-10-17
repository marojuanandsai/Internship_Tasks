if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    # Get all unique scores and sort them in ascending order
    scores = sorted(list(set([score for name, score in records])))
    
    # The second lowest score is at index 1
    second_lowest = scores[1]
    
    # Extract names of students with the second lowest score
    second_lowest_students = [name for name, score in records if score == second_lowest]
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    
    # Print each student's name on a new line
    for student in second_lowest_students:
        print(student)
