"""
display_rooms.py

This example shows how to display all the rooms in the lobby.
"""


from talkomatic import Bot # import the Bot class from the talkomatic package


bot = Bot() # create a new Bot instance

# with this decorator, the function will be called when the bot finishes connecting to the server
@bot.on_connect
async def on_connect() -> None:
    # for each room in the lobby, we print the room
    for room in bot.rooms:
        print(room)
    
    # we're done, so we can disconnect
    await bot.disconnect()

# we're ready to go! let's run the bot with a username and location
bot.run("Room Display", "Bot")
