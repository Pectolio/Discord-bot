import discord
from discord.ext import commands, tasks
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

CANAL_ID = 1416998797451595856  # reemplaza con el ID de tu canal

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")
    encuesta_mensual.start()

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! Latencia: {round(bot.latency * 1000)}ms")

@bot.command()
async def hola(ctx):
    await ctx.send(f"¡Hola, {ctx.author.mention}! 👋")

@tasks.loop(hours=24)
async def encuesta_mensual():
    ahora = datetime.datetime.now()

    if ahora.day == 30:
        canal = bot.get_channel(CANAL_ID)

        poll = discord.Poll(
            question="¿Genero Pelicula Mensual?",
            duration=datetime.timedelta(days=5),
        )

        poll.add_answer(text="Ciencia Ficcion", emoji="🛸")
        poll.add_answer(text="Terror", emoji="👻")
        poll.add_answer(text="Comedia", emoji="🤡")
        poll.add_answer(text="Accion", emoji="🔫")
        poll.add_answer(text="Drama", emoji="🎭")
        poll.add_answer(text="Animacion", emoji="✏️")
        poll.add_answer(text="Suspenso", emoji="🗡️")
        poll.add_answer(text="Fantasia", emoji="🧙‍♂️")

        await canal.send(poll=poll)
        await canal.send("@here ¡Recuerden votar por los generos que mas les tinca para este mes!")
        
    elif ahora.day == 1:
        canal = bot.get_channel(CANAL_ID)

        poll = discord.Poll(
            question="¿Semana Pelicula Mensual?",
            duration=datetime.timedelta(days=3),
        )

        poll.add_answer(text="Semana 1 Del mes")
        poll.add_answer(text="Semana 2 Del mes")
        poll.add_answer(text="Semana 4 Del mes")
        poll.add_answer(text="Semana 5 Del mes")

        await canal.send(poll=poll)
        await canal.send("@here ¡Recuerden votar para la semana que mas les acomode!")
        
    elif ahora.day == 2:
        canal = bot.get_channel(CANAL_ID)

        poll = discord.Poll(
            question="¿Dia de la pelicula?",
            duration=datetime.timedelta(days=3),
        )

        poll.add_answer(text="Viernes")
        poll.add_answer(text="Sabado")
        poll.add_answer(text="Domingo")

        await canal.send(poll=poll)
        await canal.send("@here ¡Recuerden votar por el dia que mas les acomode")
        
    elif ahora.day == 3:
        canal = bot.get_channel(CANAL_ID)

        poll = discord.Poll(
            question="¿Horario de la pelicula",
            duration=datetime.timedelta(days=3),
        )

        poll.add_answer(text="17:00 CH/23:00 FR")
        poll.add_answer(text="18:00 CH/00:00 FR")
        poll.add_answer(text="19:00 CH/01:00 FR")

        await canal.send(poll=poll)
        await canal.send("@here ¡Recuerden por el horario, piensen en tomate")
bot.run(TOKEN)