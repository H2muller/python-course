'''
  _____            ___          
 / ___/______ ____/ (_)__  ___ _
/ (_ / __/ _ `/ _  / / _ \/ _ `/
\___/_/  \_,_/\_,_/_/_//_/\_, / 
                         /___/
'''

Assignments:dict = {'Assignment_1': 100,
                    'Assignment_2': 100,
                    'Assignment_3': 100,
                    'Assignment_4': 100,
                    'Assignment_5': 100,
                    'Assignment_6': 100}

course_project:dict = {'grade': 100, 
                        'weight': 4}

def retrieve_course_grade(assignments:dict, course_project:type) -> str:
        assignment_grade_sum: float = 0.0
        for _, grade in assignments.items():
            assignment_grade_sum += grade

        final_grade = ((assignment_grade_sum 
            + (course_project['grade'] * course_project['weight']))
            / (len(assignments) + course_project['weight']))

        if final_grade >= 0.90:
            return 'A'
        elif final_grade > 0.80 and final_grade < 0.90:
            return 'B'
        elif final_grade > 0.70 and final_grade < 0.80:
            return 'C'
        elif final_grade > 0.60 and final_grade < 0.70:	
            return 'D'
        else:
            return 'F'
