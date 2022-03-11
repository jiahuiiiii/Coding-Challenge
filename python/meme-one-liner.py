
def gpa_calculator_v1(dic):
    gpa = 0
    total_credit_hrs = 0
    total_points = 0
    quality_points = ['F', 'D', 'C', 'B', 'A']
    for i in dic['courses']:
        total_points += quality_points.index(i['grade']) * i['credit_hours']
        total_credit_hrs += i['credit_hours']
        gpa = total_points / total_credit_hrs
    gpa = '{:.2f}'.format(gpa)
    name = dic['name']
    semester = dic['semester']
    return f'{name} GPA for {semester} is {gpa}'

def gpa_calculator(dic):
    gpa = 0
    quality_points = 'FDCBA'
    for i in dic['courses']:
        gpa = sum(quality_points.index(i['grade']) * i['credit_hours']) / sum(i['credit_hours'])
    return '{} GPA for {} is {}'.format(dic['name'], dic['semester'], '{:.2f}'.format(gpa))


def gpa_calculator(dic):
    return '{} GPA for {} is {}'.format(dic['name'], dic['semester'], '{:.2f}'.format(sum([i['credit_hours'] * 'FDCBA'.index(i['grade']) for i in dic['courses']]) / sum(i['credit_hours'] for i in dic['courses'])))
