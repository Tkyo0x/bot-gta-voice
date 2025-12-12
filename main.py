import discord
import asyncio
from flask import Flask, request
from threading import Thread
import os

# --- CONFIGURACIÓN ---
# Token directo para evitar problemas de variables de entorno en la nube gratuita
TOKEN = "MTQ0NzM4NzE3MTA3Mjc3MDE1MA.Ge8ymP._48sBp6ZIkXdLxXSq_CoS5xSNzVLSf0B932vE0"
# ---------------------

intents = discord.Intents.default()
client = discord.Client(intents=intents)
app = Flask(__name__)
bot_loop = None

@client.event
async def on_ready():
    global bot_loop
    bot_loop = asyncio.get_running_loop()
    print(f'✅ BOT ONLINE: {client.user}')

@app.route('/')
def home():
    return "BOT GTA FUNCIONANDO 24/7"

@app.route('/join')
def join_route():
    channel_id = request.args.get('id')
    if channel_id and bot_loop:
        asyncio.run_coroutine_threadsafe(connect_voice(channel_id), bot_loop)
        return "OK"
    return "ERROR"

async def connect_voice(channel_id):
    try:
        channel = client.get_channel(int(channel_id))
        if channel and isinstance(channel, discord.VoiceChannel):
            if client.voice_clients:
                await client.voice_clients[0].disconnect()
            await channel.connect()
            print(f"🔊 Conectado a: {channel.name}")
    except Exception as e:
        print(f"❌ Error: {e}")

def run():
  app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    t = Thread(target=run)
    t.start()
    client.run(TOKEN)