import discord
import asyncio
from flask import Flask, request
from threading import Thread
import os

# --- TU TOKEN DE LA CUENTA SECUNDARIA ---
# (Si Discord te lo reseteó por ponerlo en el chat, busca el nuevo en la consola F12)
TOKEN = "MTQ0NzM4NzE3MTA3Mjc3MDE1MA.Ge8ymP._48sBp6ZIkXdLxXSq_CoS5xSNzVLSf0B932vE0"
# ----------------------------------------

# Usamos la libreria self-bot
client = discord.Client()
app = Flask(__name__)
bot_loop = None

@client.event
async def on_ready():
    global bot_loop
    bot_loop = asyncio.get_running_loop()
    print(f'✅ CUENTA CONECTADA: {client.user}')

@app.route('/')
def home():
    return "CUENTA GTA FUNCIONANDO"

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
        # Verificamos si es canal de voz
        if channel and isinstance(channel, discord.VoiceChannel):
            # Si ya está en otro canal, se sale
            if client.voice_clients:
                await client.voice_clients[0].disconnect()
            
            # Se une al canal (como usuario, self_deaf=True para no consumir ancho de banda)
            await channel.connect(self_deaf=True)
            print(f"🔊 Entré al canal: {channel.name}")
    except Exception as e:
        print(f"❌ Error: {e}")

def run():
  app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    t = Thread(target=run)
    t.start()
    client.run(TOKEN)
