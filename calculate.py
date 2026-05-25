saved_grades_list = {}
def calculate():
    grade_points = {
        'Excellence': 4,
        'Merit': 3,
        'Achieved': 2,
    }
    calculate_list = []
    for subject_name, subject_data in saved_grades_list.items():
        for standard in subject_data.values():
            if standard['grade'] in grade_points:
                calculate_list.append({"subject": subject_name, 
                                       "standard": standard})

    def get_point(item):
        return grade_points.get(item['standard']['grade'], 0)

    calculate_list.sort(key=get_point, reverse=True)

    total_credits = 0
    rank_score = 0
    calculated_list = {}
    for standard in calculate_list:
        if total_credits >= 80:
            break

        grade = standard['standard']['grade']
        credit = int(standard['standard']['credits'])
        subject = standard['subject']
        
        if grade in grade_points:
            if total_credits + credit > 80:
                credit = 80 - total_credits

            current_rank_score = credit * grade_points[grade]

            total_credits += credit
            rank_score += current_rank_score

            if subject not in calculated_list:
                calculated_list[subject] = {'credits': 0, 'rank_score': 0}
            
            calculated_list[subject]['credits'] += credit
            calculated_list[subject]['rank_score'] += current_rank_score

    return (
        total_credits,
        rank_score,
        calculated_list
    )