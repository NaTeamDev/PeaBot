from msilib.schema import tables
from turtle import color
import discord, time
from discord.ext import commands
from random import choice

bot = commands.Bot(command_prefix="pb!", description="Je suis un bot multi-fonctions !")

bot.remove_command("help")

creator = 888023836921057310

supportTeam = 906213157343727646

@bot.event
async def on_ready():
	print("Ready !")

	await bot.change_presence(status = discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="la commande //help"))

#-- Informations Commands --

#Command "HELP"
@bot.command()
async def help(ctx):
        emhelp = discord.Embed(title="Commandes", description=f"Voici les commandes que je peux effectuer : \n\n Mon préfix est **{bot.get_prefix}**\n\n**help** : Obtenir la liste des commandes. \n**support** : Obtenir un lien d'invitation vers mon serveur de support. \n**invite** : Obtenir un lien d'invitation du bot. \n**servinfos** : Obtenir des informations sur le serveur. \n**botinfos** : Obtenir des informations sur moi-même. \n\n[Support] **maint_on** : Lancer une maintenance. \n[Support] **maint_off** : Terminer une maintenance. \n\n[Mod] **clear [nombre]** : Supprimer un nombre de messages. \n\n**avatar [@membre]** : Donner l'avatar d'un membre du serveur. \n\n[Admin] **say [titre : UN SEUL MOT] [message]** : Ecrire quelque chose avev le bot. \n\n*Légende* \n**[Support]** : Ceci vous indique que c'est une commande que seul l'équipe de PeaBot peut utiliser. \n**[Mod]** : Ceci vous indique que la commande est une commande de Modération. \n**[Admin]** : Ceci vous indique qur vous devez disposer de la permission \"Administrateur\".", color=0x0000FF)

        await ctx.send(embed = emhelp)

#Command "SUPPORT"
@bot.command()
async def support(ctx):
        emsupport = discord.Embed(title="Serveur de support", description="Clique sur le lien ci-dessous pour rejoindre mon serveur de support : \nhttps://discord.gg/4VE25wfU.", color=0x0000FF)

        await ctx.send(embed = emsupport)

#Command "INVITE"
@bot.command()
async def invite(ctx):
	eminv = discord.Embed(title="Invitations", description="Clique sur le lien ci-dessius pour m'inviter sur ton serveur : \nhttps://discord.com/api/oauth2/authorize?client_id=890211850006954034&permissions=1644972474359&scope=bot%20applications.commands.", color=0x0000FF)

	await ctx.send(embed = eminv)

#Command "SERVINFOS"
@bot.command()
async def servinfos(ctx):
	serverName = ctx.guild.name
	membersCount = ctx.guild.member_count
	serverDescription = ctx.guild.description
	numberOfTextChannels = len(ctx.guild.text_channels)
	numberOfVoiceChannels = len(ctx.guild.voice_channels)
	serverDescription = ctx.guild.description

	if serverDescription == None:
		serverDescription = "Aucune"

	else:
		pass

	emservInf = discord.Embed(title="Informations du serveur", description="Voici les informations de ce serveur.", color=0x0000FF)

	emservInf.add_field(name="Nom du serveur", value=serverName)
	emservInf.add_field(name="Nombre de membres", value=membersCount)
	emservInf.add_field(name="Nombre de salons textuels", value=numberOfTextChannels)
	emservInf.add_field(name="Nombre de salons vocaux", value=numberOfVoiceChannels)
	emservInf.add_field(name="Description", value=serverDescription)

	await ctx.send(embed = emservInf)

#Command "SERVSETTINGS"
@bot.command()
async def 

#Command "BOTINFOS"
@bot.command()
async def botinfos(ctx):
	embotInf = discord.Embed(title="Informations de PeaBot", description="Voici les informations sur moi-même.", color=0x0000FF)

	embotInf.add_field(name="Créateur", value="BlackGamer#9111")
	embotInf.add_field(name="Tag Discord", value="#6692")
	embotInf.add_field(name="Date de création", value="14 février 2022")

	embotInf.set_footer(text="Et bah tu sais tout sur moi !")

	await ctx.send(embed=embotInf)

#-- Support Team Commands --

#Command "MAINT_ON"
@bot.command()
@commands.has_role(supportTeam)
async def maint_on(ctx):
	channel = bot.get_channel(942726568319528991)

	emMaintOn = discord.Embed(title="Maintenance", description="Je suis maintenant en maintenance, mais je reviens très vite !", color=0xFF0000)

	await channel.send(embed = emMaintOn)

#Command "MAINT_OFF"
@bot.command()
@commands.has_role(supportTeam)
async def maint_off(ctx):
	channel = bot.get_channel(942726568319528991)

	emMaintOff = discord.Embed(title="Maintenance", description="Je ne suis désormais plus en maintenance, vous pouvez me réutiliser !", color=0x00FF00)

	await channel.send(embed = emMaintOff)

#-- Fun Commands
@bot.command()
async def random(ctx, min : int = 1, max : int = 2):
	number = randint(min, max)

	message = await ctx.send("Je tire un nombre au hasard...")

	time.sleep(2)

	await message.edit("3")
	# await ctx.send("3")

	time.sleep(1)

	await ctx.send("2")

	time.sleep(1)

	await ctx.send("1")

	time.sleep(1)

	emrandom = discord.Embed(title="Nombre au hasard", description=f"Voici le nombre que j'ai tiré : \n\n{number}.", color=0x00FF00)

	await ctx.send(embed = emrandom)

#-- Moderation Commands

#Command "CLEAR"
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, numberOfMessages : int):
	message = await ctx.channel.history(limit=numberOfMessages+1).flatten()

	for message in message:
		await message.delete()

	emclear = discord.Embed(title="Suppression de messages", description=f"J'ai supprimé {numberOfMessages} messages.", color=0x00FF00)

	emclear.set_footer(text="Ce message va se supprimer dans 10 secondes")

	confirmationMessage = await ctx.send(embed  = emclear)

	time.sleep(10)

	messages = await ctx.channel.history(limit=1).flatten()

	for messages in messages:
		await confirmationMessage.delete()

#Command "SAY"
@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, message = None):
	if message != None: await ctx.send(message)
	else: await ctx.send("Une erreur est survenue : Veuillez spécifier un message à envoyer !")

#-- STAFF Bot commands --


@bot.command
async def admin_kick(ctx, user : discord.User = None, *, reason = "Aucune"):
	if user != None:
		await ctx.guild.kick(user, reason=f"[PeaBot>Admin] Utilisateur expulsé par le STAFF Bot ! Raison : {reason}")

		embed = discord.Embed(
			title="__Alerte Info !__",
			description="Une membre a été expulsé(e) par le STAFF Bot",
			color=0x00FF00
		)
		embed.add_field(name="Membre", value=user)
		embed.add_field(name="Raison", value=reason)

		await ctx.send(embed = embed)
		
		embedMP = discord.Embed(
			title="Expulsion", 
			description=f"Vous avez été expulsé(e) du server {ctx.guild.name} par un administrateur de PeaBot.",
			color=0xFF0000
		)
		embedMP.add_field(name="Raison", value=reason)

		await user.send(embed = embedMP)

#-- Fun Commands --

#Command "AVATAR"
@bot.command()
async def avatar(ctx, user : discord.User):
	emavatar = discord.Embed(title=f"Avatar de {user.name}", description=f"Voici l'avatar de {user.name}.", color=0x0000FF)

	emavatar.set_image(url=user.avatar_url)

	await ctx.send(embed = emavatar)

#Command "BLAGUE"
@bot.command()
async def blague(ctx):
	jockes = [
		"Pourquoi les patissiers ont besoin d'une imprimante ? Pour imprimer les mille-feuilles ! \:rofl:",
		"Mme Dujardin dit à Mme Dubalcon \"Moi j'ai un mari en or !\". Mme Dubalcon dit \"Ah bah le mien est en taule !\" \:rofl:"
	]

	embed = discord.Embed(title="Blague", description=f"Voici une blague : ")

	await ctx.send(embed = embed)

bot.run("ODkwMjExODUwMDA2OTU0MDM0.GuLmuC.JgS05WJ26QVDLmtJ84b6HQGWrA0YfvErwhFlS8")
