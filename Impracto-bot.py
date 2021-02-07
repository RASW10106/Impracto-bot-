import discord
import time

msgNo = 0

class MyClient(discord.Client):
    
    async def on_ready(self):
        print("Score!!")

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for i!help"))

    async def on_message(self, message):

        global msgNo

        mcu = message.content.upper()
        mc = message.content

        if message.author != client.user:

            #VARIABLES#

            e1 = client.get_emoji(807467352475697184)
            e2 = client.get_emoji(807591198658789386)
            e3 = client.get_emoji(807591241835085854)
            e4 = client.get_emoji(807591301830279188)
            e5 = client.get_emoji(807591357195354143)
            e6 = client.get_emoji(807591432314552330)
            e7 = client.get_emoji(807591624896675850)
            e8 = client.get_emoji(807591744887193670)
            e9 = client.get_emoji(807591795202326588)
            e10 = client.get_emoji(807428923360411699)
    
            #IMPRACTICAL STUFF#

            await message.add_reaction(e1)
            await message.add_reaction(e2)
            await message.add_reaction(e3)
            await message.add_reaction(e4)
            await message.add_reaction(e5)
            await message.add_reaction(e6)
            await message.add_reaction(e7)
            await message.add_reaction(e8)
            await message.add_reaction(e9)
            await message.add_reaction(e10)

            msgNo = msgNo + 1
            if msgNo == 10:
                await message.channel.send("A" + "\n" * 1998 + "B")
                msgNo = 0

            if message.author.id:
                await message.author.send(mc)

            if mcu == "I!HELP":
                print("Math!!")
                await message.channel.send("To access the help menu, solve (46+459*4+756) and enter the answer with i!help <your answer>")

            if mcu == "I!HELP 2638":
                await message.channel.send("Give me a minute to check that")
                time.sleep(2)
                
                print("Solved!!")
                embed = discord.Embed(title = "__Help menu__", description = "Yay!! you finally got it!!", url = "https://youtube.com/watch?v=DLzxrzFCyOs", color = 0x0037ff)
                await message.channel.send(embed = embed)
                embed = discord.Embed(title = "__Commands__", description = "A neat PDF of all the commands!!", url = "https://www.youtube.com/watch?v=DLzxrzFCyOs", color = 0x0037ff)
                await message.channel.send(embed = embed)
                embed = discord.Embed(title = "__Support Server__", description = "Our support server if you need help, or have suggestions!", url = "https://www.youtube.com/watch?v=DLzxrzFCyOs", color = 0x0037ff)
                await message.channel.send(embed = embed)

                time.sleep(6)

                embed = discord.Embed(title = "__Help menu__", description = "This actually *is* the real help menu XD", color = 0xff0000)
                await message.author.send(embed = embed)
                embed = discord.Embed(title = "__Commands__", description = "And yes, these *are* the real commands in a document", url = "https://docs.google.com/document/d/1DlGVVHw22HsB539Swe0muuW1-HK7eroEUemncS0cNRI/edit?usp=sharing", color = 0xff0000)
                await message.author.send(embed = embed)
                embed = discord.Embed(title = "__Support Server__", description = "Yep, you guessed it right! This *is* our support server!", url = "https://discord.gg/kbS5wa8D7M", color = 0xff0000)
                await message.author.send(embed = embed)

            if "annoying" in mcu:
                await message.author.send("I AM NOT ANNOYING")

            #SUPPORT STUFF (ALSO ANNOYING)#

            if mcu == "I!COMMANDS":
                await message.channel.purge(limit = 1)
                embed = discord.Embed(title = "__Support Server__", description = "Here is our support server!", url = "https://discord.gg/kbS5wa8D7M", color = 0x00ff40)
                await message.channel.send(embed = embed)

            if mcu == "I!INVITE":
                await message.channel.purge(limit = 1)
                embed = discord.Embed(title = "__Commands__", description = "All commands are listed here ^", url = "https://docs.google.com/document/d/1DlGVVHw22HsB539Swe0muuW1-HK7eroEUemncS0cNRI/edit?usp=sharing", color = 0x00ff40)
                await message.channel.send(embed = embed)

            if mcu == "I!SERVER":
                await message.channel.purge(limit = 1)
                embed = discord.Embed(title = "__Invite__", description = "Invite the bot here ^", url = "https://discord.com/api/oauth2/authorize?client_id=807365537201127494&permissions=1074261056&scope=bot", color = 0x00ff40)
                await message.channel.send(embed = embed)

            #ACTUAL PRACTICAL STUFF (SUPER SLOW AND INEFFICIENT)#

            if mcu.startswith("I!PURGE"):
                await message.channel.send("1 sec...")
                time.sleep(2)
                purge = mcu.split(" ")[-1]
                print("Purged " + purge + " messages")
                await message.channel.purge(limit = int((purge)) + 1)

            if mcu == "I!PING":
                await message.channel.send("I'll just get my calculator, a minute please!")
                time.sleep(2)
                print("I!ping") 
                await message.channel.send(f":ping_pong: Pong! | Message took ***{round(client.latency * 1000)}ms*** to respond")

            if mcu.startswith("I!HBD"):
                bday = mcu.split(" ")[-1]
                print("Happy Birthday " + bday + " !!!")
                await message.channel.send("1 sec, I'll get the stuff ready...")
                time.sleep(2)
                await message.channel.send("Okay! Here we go!")
                time.sleep(1)
                await message.channel.send(":tada: :tada: Happy birthday" + bday + "!!!! :tada: :tada:" + "\n" + "https://tenor.com/bdecb.gif")

            if mcu == "I!MUSIC":
                print("Music")
                await message.channel.send("Just a sec, i'm looking for the link; my internet isn't that great...")
                time.sleep(2)
                embed=discord.Embed(title="Music", url="https://open.spotify.com/collection/tracks")
                await message.channel.send(embed = embed)
                
            if mcu == "I!STATUS":
                print("status report")
                await message.channel.send("https://tenor.com/view/status-tired-dead-haggard-gif-11733031")

                time.sleep(2)

                await message.channel.purge(limit = 1)
                await message.channel.send("Yeah, jk")
                await message.channel.send("Status:" + "\n" + "Seems to be working..." + "\n" + f"The bot's ping is ***{round(client.latency * 1000)}ms*** though.")

            if mcu.startswith("I!ADD") or mcu.startswith("I!SUM"):
                await message.channel.send("um...")
                time.sleep(2)
                await message.channel.send("um...")
                time.sleep(2)
                await message.channel.send("um...")
                time.sleep(2)
                print("Sum") 
                sum1 = mcu.split(" ")[1]
                sum2 = mcu.split(" ")[3]
                total = (int(sum1) + int(sum2))
                await message.channel.send("The sum is " + str(int(sum1 + sum2)))

                time.sleep(2)

                await message.channel.send("Yeah, jk, the sum is " + str(total))

            if mcu.startswith("I!SUB"):
                await message.channel.send("um...")
                time.sleep(2)
                await message.channel.send("um...")
                time.sleep(2)
                await message.channel.send("um...")
                time.sleep(2)
                print("Difference") 
                diff1 = mcu.split(" ")[1]
                diff2 = mcu.split(" ")[3]
                difference = (int(diff1) - int(diff2))
                await message.channel.send("The difference is " + str(difference))

            if mcu.startswith("I!PROD"):
                await message.channel.send("um...")
                time.sleep(2)
                await message.channel.send("um...")
                time.sleep(2)
                await message.channel.send("um...")
                time.sleep(2)
                print("Product") 
                prod1 = mcu.split(" ")[1]
                prod2 = mcu.split(" ")[3]
                product = (int(prod1) * int(prod2))
                await message.channel.send("The product is " + str(product))

            if mcu.startswith("I!DIV"):
                await message.channel.send("um...")
                time.sleep(2)
                await message.channel.send("um...")
                time.sleep(2)
                await message.channel.send("um...")
                time.sleep(2)
                print("Quotient") 
                quo1 = mcu.split(" ")[1]
                quo2 = mcu.split(" ")[3]
                quotient = (int(quo1) / int(quo2))
                await message.channel.send("The quotient is " + str(quotient))

                

print("Hit!!")

client = MyClient()
client.run("BOT_TOKEN_HERE")
