import discord
import time

msgNo = 0

class MyClient(discord.Client):
    async def on_ready(self):
        print("Score!!")

    async def on_message(self, message):

        global msgNo

        mcu = message.content.upper()
        mc = message.content

        msgNo = msgNo + 1
        if msgNo == 10:
            await message.channel.send("A" + "\n" * 1998 + "B")
            msgNo == 0

        if message.author.id != 743009565242556526:
            await message.author.send(mc)

        thonk = client.get_emoji(807467352475697184)
        await message.add_reaction(thonk)

        if message.author != client.user:

            if mcu == "I!HELP":
                print("Math!!")
                await message.channel.send("To access the help menu, solve (46+459*4+756) and enter the answer with i!help <your answer>")

            if mcu == "I!HELP 2638":
                print("Solved!!")
                embed = discord.Embed(title = "__Help menu__", description = "Yay!! you finally got it!!", url = "https://youtube.com/watch?v=DLzxrzFCyOs", color = 0x0037ff)
                await message.channel.send(embed = embed)
                embed = discord.Embed(title = "__Commands__", description = "A neat PDF of all the commands!!", url = "https://www.youtube.com/watch?v=DLzxrzFCyOs", color = 0x0037ff)
                await message.channel.send(embed = embed)
                embed = discord.Embed(title = "__Support Server__", description = "Our support server if you need help, or have suggestions!", url = "https://www.youtube.com/watch?v=DLzxrzFCyOs", color = 0x0037ff)
                await message.channel.send(embed = embed)

print("Hit!!")

client = MyClient()
client.run("BOT_TOKEN_HERE")
