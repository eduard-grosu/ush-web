table = '''
    <html>
        <head>
            <title>USH Informatica - Back</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        </head>
        <body>
            <style>
                body {{
                    user-select: none;
                }}
                .nowrap {{
                    white-space: nowrap;
                }}
            </style>
            {body}
        </body>
    </html>
'''

def weekday_sort(items):
    weekdays = [
        'LUNI',
        'MARTI',
        'MIERCURI',
        'JOI',
        'VINERI',
        'SAMBATA',
        'DUMINICA'
    ]

    day, hour = items[0].split(' ')
    index = int(hour[:2])

    if day in weekdays:
        index += weekdays.index(day) * 24

    return index

def create_table(courses):
    courses_names = {
        'ASC': 'Arhitectura Sistemelor de Calcul',
        'FP': 'Fundamentele Programarii'
    }

    def th_wrap(value):
        return f'<th scope="col"><b>{value}</b></th>'

    def td_wrap(value):
        return f'<td>{value}</td>'

    def body_wrap(data, x):
        _list = [alumni[x] if x < len(alumni) else '' for alumni in data.values()]
        _list = ''.join(map(td_wrap, _list))
        return f'<tr><th scope="row">{x+1}</th>{_list}</tr>'

    html = ''
    for course, data in courses.items():
        data = {k: v for k, v in sorted(data.items(), key=weekday_sort)}
        keys = list(data.keys())

        # Max. n. of elements inside a list found under 'course', for fixed 'horizontal' recursion
        max_elm_count = max(len(lst) for lst in data.values())

        _html = '''
            <h2 class="text-center">{course}</h2>
            <div class="table-responsive">
                <table class="table table-bordered table-hover">
                    <thead class="thead-dark"><tr><th scope="col">#</th>{head}</tr></thead>
                    <tbody>{body}</tbody>
                </table>
            </div>
        '''.format(
            course=courses_names.get(course),
            head=''.join(map(th_wrap, keys)),
            body=''.join([body_wrap(data, x) for x in range(max_elm_count)])
        )

        html += _html

    return html
