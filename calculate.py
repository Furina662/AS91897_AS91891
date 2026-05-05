saved_grades_list = {}
def calculate():
    grade_points = {
        'Excellence': 4,
        'Merit': 3,
        'Achieved': 2,
    }
    calculate_list = []
    for subject_data in saved_grades_list.values():
        for standard in subject_data.values():
            if standard['grade'] in grade_points:
                calculate_list.append(standard)

    def get_point(standard):
        return grade_points.get(standard['grade'], 0)

    calculate_list.sort(key=get_point, reverse=True)

    total_credits = 0
    rank_score = 0

    for standard in calculate_list:
        if total_credits >= 80:
            break

        grade = standard['grade']
        credit = int(standard['credits'])
        
        if grade in grade_points:
            if total_credits + credit > 80:
                credit = 80 - total_credits

            rank_score += credit * grade_points[grade]
        total_credits += credit

    return (
        total_credits,
        rank_score
    )
