"""
vote_guard.py

This example shows making a bot keeping track of votes, and banned users.
"""


from talkomatic import Bot, RoomType # import the Bot class from the talkomatic package


bot = Bot() # create a new Bot instance

# with this decorator, the function will be called when the bot finishes connecting to the server
@bot.on_connect
async def on_connect() -> None:
    # we find the first non-full room, and we join it
    for room in bot.rooms:
        if (not room.is_full) and room.room_type == RoomType.PUBLIC:
            await bot.join_room(room)
            return
    print("We didn't find any non-full rooms to join. :(") # :(
    await bot.disconnect()

# this function will execute when:
@bot.on_room_join     # - when the bot joins a room
@bot.on_user_vote     # - when a user votes
@bot.on_user_leave    # - when a user leaves
async def update_message(*args) -> None: # we use *args here since we don't care about the arguments
    bot_message = "Votes:\n\n"
    for voted, voters in bot.current_room.votes.items(): # we iterate over the voted user, and the voters
        voted_user = bot.get_user_by_id(voted.id) # we try to resolve the voted user, if we can't, we just use the ID-only one
        bot_message += f"{str(voted_user if voted_user != None else voted)}\n" # we add the name the voted user
        for voter in voters: # for each voter that's voted for that user
            voter_user = bot.get_user_by_id(voter.id) # we try to resolve the voter user, if we can't, we just use the ID-only one
            bot_message += f"  - {str(voter_user if voter_user != None else voter)}\n" # we add the name of the voter
        bot_message += "\n" # we add a new line after each user's votes (for readability)
    if len(bot.current_room.votes) == 0: # no voted users!
        bot_message += "No users are currently voting for anyone to be banned.\n"
    
    if (bot.current_room.banned_users != None) and (bot.current_room.banned_users != []): # there are banned users!
        bot_message += "\nBanned users:\n"
        for banned_user in bot.current_room.banned_users: # we display the banned users' IDs
            bot_message += f"  - User with ID: {banned_user.id}\n"
    
    await bot.send_message(bot_message) # we send the bot's message!

# we're ready to go! let's run the bot with a username and location
bot.run("Vote Guard", "Bot")
