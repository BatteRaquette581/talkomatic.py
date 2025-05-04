"""
display_rooms.py

This example shows how to display all the rooms in the lobby.

This example does the same as the examples/display_rooms.py script,
but this time we're using the Talkomatic REST API to get the room information.
"""

from talkomatic.api.v1 import get_rooms # we import the RoomInfo class from the Talkomatic API module


rooms = get_rooms() # we get the room information using the get method

for room in rooms: # we print all of the rooms!
    print(room)
