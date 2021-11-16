class Courses:
    catalog = {}

    def __init__(self, course, name):
        self.course = course
        self.name = name
        self.catalog = Courses.catalog

    def add(self):
        if self.course not in self.catalog:
            self.catalog[self.course] = []
        self.catalog[self.course].append(self.name)

    def __str__(self):
        data = []
        sort_courses = dict(sorted(self.catalog.items(), key=lambda x: (-len(x[1]), x[1].sort())))

        for k, v in sort_courses.items():
            data.append(f'{k}: {len(v)}')
            for name in v:
                data.append(f'-- {name}')

        return '\n'.join(data)


while True:
    try:
        course_type, user_name = input().split(' : ')
        info = Courses(course_type, user_name)
        info.add()
    except:
        print(info)
        break


'''
Programming Fundamentals : John Smith
Programming Fundamentals : Linda Johnson
JS Core : Will Wilson
Java Advanced : Harrison White
end

------------------ output:

Programming Fundamentals: 2
-- John Smith
-- Linda Johnson
JS Core: 1
-- Will Wilson
Java Advanced: 1
-- Harrison White
'''