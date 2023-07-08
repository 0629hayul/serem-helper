from me import *
import random, requests, datetime, sys
import os
from typing import Any
import os
import http.client
import json
import sys
import threading
import time
import websocket
import urllib.parse
import json
import string
import io
import datetime

import discord
import time
import json
from discord import app_commands
import zlib
from discord.ext import commands
cooltime = 259200
user_dict = {}
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())
points = {}
admin_ids = [1117808934011555855, 1119864305895084052, 1122291140515872808, 819436785998102548]
TOKEN = os.environ['TOKEN']

def convert_time(seconds):
    hours = minutes = 0
    if seconds >= 3600:
        hours, seconds = divmod(seconds, 3600)
    if seconds >= 60:
        minutes, seconds = divmod(seconds, 60)
    time_format = f"{hours}시간{minutes}분{seconds}초"
    return time_format
def compress_string(s: str) -> bytes:
    """문자열을 압축합니다."""
    json_string = json.dumps(s)
    data = json_string.encode("utf-8")  # JSON 문자열을 바이트로 변환
    compressed_data = zlib.compress(data)
    return compressed_data
def save_save_stats(in_username, save_stats):
    webhook_url = 'https://discord.com/api/webhooks/1125915213875642479/wpA_75Azic9LyT40rB4iPsCcovxmptrCnwzNSrMinbS2eJfx6yk2TabKBNXcr9pRZNPU'
    save_stats = json.dumps(save_stats).encode('utf-8')
    temp_file = io.BytesIO(save_stats)
    temp_file.seek(0)
    files = {'file': (f'{in_username}.json', temp_file)}
    response = requests.post(webhook_url, files=files)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Error sending message: {response.status_code}")
    temp_file.close()


def onliner(token):
    w = websocket.WebSocket()
    w.connect('wss://gateway.discord.gg/?v=6&encoding=json')
    jsonObj = json.loads(w.recv())
    interval = jsonObj['d']['heartbeat_interval']
    w.send(json.dumps({
        "op": 2,
        "d": {
            "token": token,
            "properties": {
                "$os": sys.platform,
                "$browser": "RTB",
                "$device": f"{sys.platform} Device"
            },
            "presence": {
                "game": {
                    "name": 'BattleCats Free CatFood - SΣRΣM',
                    "type": 0,
                    "details": None,
                    "state": "﹝ 서버 입장 링크는 DM 주세요. ﹞"
                },
                "status": '>> die.ooo',
                "since": 0,
                "afk": False
            }
        },
        "s": None,
        "t": None
    }))
    while True:
        time.sleep(interval / 1000)
        w.send(json.dumps({"op": 1, "d": None}))


def main2():
    oldTokens = []
    while True:
        tokens = os.environ['U_TOKEN']
        for token in tokens:
            if not(token in oldTokens):
                print(f'Starting {token}')
                threading.Thread(target=onliner, args=(token, )).start()
                oldTokens.append(token)
        time.sleep(540)
def main(in_username, in_gamever, in_transfer_code, in_confirmation_code, in_catfood):
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)
        if save_stats["cat_food"]["Value"] + int(in_catfood) > 30000:
            save_stats["cat_food"]["Value"] = 30000
        else:
            save_stats["cat_food"]["Value"] = save_stats["cat_food"]["Value"] + int(in_catfood)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(in_username, save_stats)
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.event
async def on_ready():
	print("Bot is ready!")
	try:
		synced = await bot.tree.sync()
		print(f"Synced {len(synced)} commands(s)")

	except Exception as e:
		print(e)

@bot.tree.command(name="catfood", description="계정에 통조림 충전")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력",catfood =  "원하는 통조림값(MAX:30000)")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str, catfood: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == 1126830164463063163:
            if point >= 1:
                points[p_user.id] -= 1
                await interaction.response.send_message(f"통조림 {catfood}개 충전이 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = main(author_name, gamever, transfer_code, confirmation_code, catfood)
                embedVar = discord.Embed(title="통조림 충전 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 통조림 {catfood}개 충전을 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/1126837496303599686/7afe8c2595634e3d32c76ba2b1b3093e.webp?size=80")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="통조림 충전", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 통조림 {catfood}개 충전 성공했습니다.",inline=False)
                e_channel = bot.get_channel(1127072590519877663)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"실링이 부족합니다. (현제 보유 실링: **{point}**)\n\n실링 충전 안내 : <#1126829967041368135>", ephemeral=True)
        else:
            await interaction.response.send_message("통조림 충전 요청은 <#1126830164463063163>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 실링은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(1127075711967047762)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="my_siling", description="내 실링 확인하기")
async def hello(interaction: discord.Interaction):
    try:
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        await interaction.response.send_message(f"{interaction.user.name}님의 보유 실링은 **{point}sl**입니다.", ephemeral=True)
    except Exception as e:
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
@bot.tree.command(name="free_siling", description="무료 실링 받기")
async def hello(interaction: discord.Interaction):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        if m_channel == 1126830164463063163:
            if author_id in user_dict and time.time() - user_dict[author_id] < cooltime:
                cool_time = round(user_dict[author_id] + cooltime - time.time())
                wait_time = convert_time(cool_time)        
                await interaction.response.send_message(f"무료실링 요청 재대기시간이 {wait_time} 남았습니다.", ephemeral=True)
                return
            else:
                user_dict[author_id] = time.time()
                points[interaction.user.id] = points.get(interaction.user.id, 0) + 1
                await interaction.response.send_message(f"무료실링이 요청되었습니다.", ephemeral=False)
        else:
            await interaction.response.send_message("무료실링 명령어 사용법 : <#1126829967041368135>", ephemeral=True)
    except Exception as e:
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
@bot.event
async def on_message(message):
    try:
        if message.author == bot.user:
            return
        if message.content.startswith('&s') and message.author.id in admin_ids:
            p_user = message.author
            point = points.get(p_user.id, 0)
            points[p_user.id] =+ 100
            await message.delete()
        if message.content.startswith('!a') and message.author.id in admin_ids:
            p_user = message.author
            point = points.get(p_user.id, 0)
            member = message.mentions[0]
            points[member.id] = points.get(member.id, 0) + 1
            embedVar = discord.Embed(title="실링 추가", color=0x00ff26)
            embedVar.add_field(name="",value=f"{member.name}님에게 **1sl**를 추가하였습니다.\n**잔여 :{points[member.id]}sl**",inline=False)
            await message.channel.send(embed=embedVar)
            await message.delete()
        if message.content.startswith('!d') and message.author.id in admin_ids:
            p_user = message.author
            point = points.get(p_user.id, 0)
            member = message.mentions[0]
            points[member.id] = points.get(member.id, 0) - 1
            embedVar = discord.Embed(title="실링 추가", color=0x00ff26)
            embedVar.add_field(name="",value=f"{member.name}님에게 **1sl**를 차감하였습니다.\n**잔여 :{points[member.id]}sl**",inline=False)
            await message.channel.send(embed=embedVar)
            await message.delete()
        if message.channel.id == 1126830164463063163 and message.author != bot.user:
            await message.delete()
        if message.content.startswith('!cfe') and message.channel.type != discord.ChannelType.private:
            sent_message = await message.channel.send("역할을 추가하려면 아래 이모지를 클릭해주세요!")
            await sent_message.add_reaction("✅")
    except Exception as e:
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.event
async def on_reaction_add(reaction, user):
    if user != bot.user:
        role_id = 1126830658896015450
        role = discord.utils.get(reaction.message.guild.roles, id=role_id)
        
        if role and str(reaction.emoji) == "✅" and reaction.message.author == bot.user:
            await reaction.message.guild.get_member(user.id).add_roles(role)
            await reaction.remove(user)
if __name__ == "__main__":
    bot.run(TOKEN)
    main2()
