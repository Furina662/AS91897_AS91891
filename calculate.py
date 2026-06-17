saved_grades_list = {}
def calculate():
    grade_points = {
        'Excellence': 4,
        'Merit': 3,
        'Achieved': 2,
    }
    calculate_list = []
    for subject_name, subject_data in saved_grades_list.items():
        for standard, standard_grade in subject_data.items():
            if standard_grade['grade'] in grade_points:
                calculate_list.append({
                    "subject": subject_name, 
                    "standard": standard,          
                    "standard_grade": standard_grade 
                })

    def get_point(item):
        return grade_points.get(item['standard_grade']['grade'], 0)

    calculate_list.sort(key=get_point, reverse=True)

    total_credits = 0
    rank_score = 0
    calculated_list = {} 
    
    for packet in calculate_list:
        if total_credits >= 80:
            break

        grade = packet['standard_grade']['grade']
        credit = int(packet['standard_grade']['credits'])
        subject = packet['subject']
        standard = packet['standard']
        
        if grade in grade_points:
            if total_credits + credit > 80:
                credit = 80 - total_credits

            current_rank_score = credit * grade_points[grade]

            total_credits += credit
            rank_score += current_rank_score

            if subject not in calculated_list:
                calculated_list[subject] = {}
            
            calculated_list[subject][standard] = {
                'credits': credit,
                'score': current_rank_score
            }

    return (
        total_credits,
        rank_score,
        calculated_list
    )