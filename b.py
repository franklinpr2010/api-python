rooms = {1: 'Left Conference Room', 2: 'Right Conference Room'}
room = input('Enter the room number:')
if not room in rooms:  # Line-3
    print('Room does not exist')
else:
    print('The room name is:' + rooms[room])