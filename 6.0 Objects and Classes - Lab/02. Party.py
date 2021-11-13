class Party:
    def __init__(self):
        self.users = []

    def __repr__(self):
        return f'Going: {", ".join(self.users)}\nTotal: {len(self.users)}'


add_people = Party()
[add_people.users.append(name) for name in iter(input, 'End')]
print(add_people)


'''
Peter
John
Katy
End
'''