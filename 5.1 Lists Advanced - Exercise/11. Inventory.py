class Inventory:
    def __init__(self, items):
        self.items = items

    def collect(self, item):
        if item not in self.items:
            self.items.append(item)

    def drop(self, item):
        if item in self.items:
            self.items.remove(item)

    def combine(self, token):
        old_item, new_item = token.split(':')
        if old_item in self.items:
            index = self.items.index(old_item)
            self.items.insert(index + 1, new_item)

    def renew(self, item):
        if item in self.items:
            index = self.items.index(item)
            self.items.append(self.items.pop(index))

    def __str__(self):
        return ', '.join(self.items)


collections = Inventory(input().split(', '))
while True:
    try:
        method, item_type = input().split(' - ')
        if method == 'Combine Items':
            method = 'combine'
        invoke_method = f'collections.{method.lower()}("{item_type}")'
        exec(invoke_method)
    except:
        print(collections)
        break


# ---------------------------------------------(2)-------------------------------------------
#
# collection = input().split(', ')
#
# while True:
#     try:
#         command, item = input().split(' - ')
#
#         if command == 'Collect' and item not in collection:
#             collection.append(item)
#         elif command == 'Drop' and item in collection:
#             collection.remove(item)
#         elif command == 'Combine Items':
#             old_item, new_item = item.split(':')
#             if old_item in collection:
#                 index = collection.index(old_item)
#                 collection.insert(index + 1, new_item)
#         else:
#             if item in collection:
#                 index = collection.index(item)
#                 element = collection.pop(index)
#                 collection.append(element)
#     except:
#         print(', '.join(collection))
#         break
