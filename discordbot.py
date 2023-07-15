from me import *
import random, requests, datetime, sys
import os
from typing import Any
import os
import http.client
import urllib.parse
import json
import string
import io
import discord
import time
import json
from discord import app_commands
import zlib
from discord.ext import commands
cooltime = 86400
cooltime2 = 86400
cooltime3 = 86400
user_dict = {}
user_dict2 = {}
user_dict3 = {}
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())
points = {}
admin_ids = [1117808934011555855, 1119864305895084052, 1122291140515872808, 819436785998102548, 887622983852642314, 1080459282044166184]
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
def normal_tickets(in_username, in_gamever, in_transfer_code, in_confirmation_code, in_value):
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

        save_stats["normal_tickets"]["Value"] = int(save_stats["normal_tickets"]["Value"]) + int(in_value)
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
def rare_tickets(in_username, in_gamever, in_transfer_code, in_confirmation_code, in_value):
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

        save_stats["rare_tickets"]["Value"] = int(save_stats["rare_tickets"]["Value"]) + int(in_value)
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
def platinum_tickets(in_username, in_gamever, in_transfer_code, in_confirmation_code, in_value):
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

        save_stats["platinum_tickets"]["Value"] = int(save_stats["platinum_tickets"]["Value"]) + int(in_value)
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
def legend_ticket_edit(in_username, in_gamever, in_transfer_code, in_confirmation_code):
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

        save_stats["legend_tickets"]["Value"] = int(save_stats["legend_tickets"]["Value"]) + 1
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

@bot.tree.command(name="normal_tickets", description="냥코티켓 충전하기 [FREE]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력", item_value = "냥코티켓 갯수[MAX:2999]")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str, item_value: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == 1128661547628109907:
            if author_id in user_dict3 and time.time() - user_dict3[author_id] < cooltime3:
                cool_time = round(user_dict3[author_id] + cooltime3 - time.time())
                wait_time = convert_time(cool_time)        
                await interaction.response.send_message(f"냥코티켓 요청 재대기시간이 {wait_time} 남았습니다.", ephemeral=True)
                return
            else:
                user_dict3[author_id] = time.time()
                await interaction.response.send_message(f"냥코티켓 {item_value}개 충전이 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = normal_tickets(author_name, gamever, transfer_code, confirmation_code, item_value)
                embedVar = discord.Embed(title="냥코티켓 충전 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 냥코티켓 {item_value}개 충전을 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#1128663548982210684>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="냥코티켓 충전", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 냥코티켓 {item_value}개 충전 성공했습니다.",inline=False)
                e_channel = bot.get_channel(1128671810091761816)
                await e_channel.send(embed=embedVar)
        else:
            await interaction.response.send_message("티켓 충전 요청은 <#1128661547628109907>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 코인은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(1128671694920351806)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="rare_tickets", description="계정에 레어티켓 충전 [1COIN]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력", item_value = "레어티켓 갯수[MAX:299]")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str, item_value: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == 1128661547628109907:
            if point >= 1:
                points[p_user.id] -= 1
                await interaction.response.send_message(f"레어티켓 {item_value}개 충전이 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = rare_tickets(author_name, gamever, transfer_code, confirmation_code, item_value)
                embedVar = discord.Embed(title="레어티켓 충전 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 레어티켓 {item_value}개 충전을 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#1128663548982210684>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="레어티켓 충전", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 레어티켓 {item_value}개 충전 성공했습니다.",inline=False)
                e_channel = bot.get_channel(1128671810091761816)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"코인이 부족합니다. (현제 보유 코인: **{point}**)\n\n코인 충전 안내 : <#1128660871602769950>", ephemeral=True)
        else:
            await interaction.response.send_message("티켓 충전 요청은 <#1128661547628109907>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 1
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 실링은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(1128671694920351806)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="platinum_tickets", description="계정에 플레티넘티켓 충전 [3COIN]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력", item_value = "플레티넘티켓 갯수[MAX:9]")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str, item_value: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        if m_channel == 1128661547628109907:
            if point >= 3:
                points[p_user.id] -= 3
                await interaction.response.send_message(f"플레티넘티켓 {item_value}개 충전이 요청되었습니다.", ephemeral=False)
                tran,pin,inquiry_code = platinum_tickets(author_name, gamever, transfer_code, confirmation_code, item_value)
                embedVar = discord.Embed(title="플레티넘티켓 충전 성공", color=0xfffffe)
                embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 플레티넘티켓 {item_value}개 충전을 성공했습니다.", inline=False)
                embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#1128663548982210684>", inline=False)

                embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/819436785998102548/d8997736cce6e2919aebe961b301156c.png?size=512")
                embedVar.timestamp = datetime.datetime.now()
                await interaction.user.send(embed=embedVar)
                embedVar = discord.Embed(title="플레티넘티켓 충전", color=0x00ff26)
                embedVar.add_field(name="",value=f"{interaction.user.name}님 플레티넘티켓 {item_value}개 충전 성공했습니다.",inline=False)
                e_channel = bot.get_channel(1128671810091761816)
                await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message(f"코인이 부족합니다. (현제 보유 코인: **{point}**)\n\n코인 충전 안내 : <#1128660871602769950>", ephemeral=True)
        else:
            await interaction.response.send_message("티켓 충전 요청은 <#1128661547628109907>에서 해주세요.", ephemeral=True)
    except Exception as e:
        points[interaction.user.id] += 3
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="사용된 실링은 복구됩니다.",inline=False)
        e_channel = bot.get_channel(1128671694920351806)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
@bot.tree.command(name="my_coin", description="내 코인 확인하기")
async def hello(interaction: discord.Interaction):
    try:
        p_user = interaction.user
        point = points.get(p_user.id, 0)
        await interaction.response.send_message(f"{interaction.user.name}님의 보유 코인은 **{point}c**입니다.", ephemeral=True)
    except Exception as e:
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
@bot.tree.command(name="free_coin", description="무료 코인 받기")
async def hello(interaction: discord.Interaction):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        if m_channel == 1128673572798337137:
            if author_id in user_dict and time.time() - user_dict[author_id] < cooltime:
                cool_time = round(user_dict[author_id] + cooltime - time.time())
                wait_time = convert_time(cool_time)        
                await interaction.response.send_message(f"무료코인 요청 재대기시간이 {wait_time} 남았습니다.", ephemeral=True)
                return
            else:
                user_dict[author_id] = time.time()
                points[interaction.user.id] = points.get(interaction.user.id, 0) + 1
                await interaction.response.send_message(f"무료코인이 요청되었습니다.", ephemeral=False)
        else:
            await interaction.response.send_message("무료코인 요청은 <#1128673572798337137>에서 해주세요.", ephemeral=True)
    except Exception as e:
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
@bot.tree.command(name="legend_ticket", description="레전드티켓 충전 [ONLY VIP]")
@app_commands.describe(gamever = "게임 버전(eg. 12.4)", transfer_code = "이어하기코드 입력", confirmation_code = "인증번호 입력")
async def hello(interaction: discord.Interaction,gamever: str, transfer_code: str, confirmation_code: str):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        author_name = interaction.user.name
        vip_role = discord.utils.get(interaction.guild.roles, id=1128659833831301201)
        if vip_role in interaction.user.roles:
            if m_channel == 1128661547628109907:
                if author_id in user_dict2 and time.time() - user_dict2[author_id] < cooltime2:
                    cool_time2 = round(user_dict2[author_id] + cooltime2 - time.time())
                    wait_time2 = convert_time(cool_time2)        
                    await interaction.response.send_message(f"레전드티켓 충전 재대기시간이 {wait_time2} 남았습니다.", ephemeral=True)
                    return
                else:
                    user_dict2[author_id] = time.time()
                    await interaction.response.send_message(f"레전드티켓 충전이 요청되었습니다.", ephemeral=False)
                    tran,pin,inquiry_code = legend_ticket_edit(author_name, gamever, transfer_code, confirmation_code)
                    embedVar = discord.Embed(title="레전드티켓 충전 성공", color=0xfffffe)
                    embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 레전드티켓 충전을 성공했습니다.", inline=False)
                    embedVar.add_field(name="", value=f"이어하기코드 : **{tran}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry_code}**", inline=False)
                    embedVar.add_field(name="", value=f"SΣRΣM 서버를 이용해주셔서 감사합니다.\n* 구매후기 : <#1128663548982210684>", inline=False)

                    embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/1117808934011555855/beee98df4c9dfd2be35dc3d4eb55326a.png?size=512")
                    embedVar.timestamp = datetime.datetime.now()
                    await interaction.user.send(embed=embedVar)
                    embedVar = discord.Embed(title="레전드티켓 충전", color=0x00ff26)
                    embedVar.add_field(name="",value=f"{interaction.user.name}님 레전드티켓 1개 충전 성공했습니다.",inline=False)
                    e_channel = bot.get_channel(1128671810091761816)
                    await e_channel.send(embed=embedVar)
            else:
                await interaction.response.send_message("레전드 티켓 충전은 <#1127205514217009223>에서 해주세요.", ephemeral=True)
        else:
            await interaction.response.send_message(f"VIP 전용 명령어입니다. 엑세스가 거부되었습니다.\n\nVIP 역할 추가하기 ➜ <#1128663764514918460>", ephemeral=True)
    except Exception as e:
        embedVar = discord.Embed(title="계정 오류", color=0xffec42)
        embedVar.add_field(name="",value="이어하기코드,인증번호를 다시 확인해주세요.",inline=False)
        embedVar.add_field(name="",value="VIP 명령어는 실링을 사용하지 않습니다.",inline=False)
        e_channel = bot.get_channel(1128671694920351806)
        await e_channel.send(f"<@{interaction.user.id}>",embed=embedVar)
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
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
        if message.content.startswith('&data') and message.author.id in admin_ids:
            await message.author.send(f"```{points}```")
        if message.content.startswith('!a') and message.author.id in admin_ids:
            p_user = message.author
            point = points.get(p_user.id, 0)
            member = message.mentions[0]
            points[member.id] = points.get(member.id, 0) + 1
            embedVar = discord.Embed(title="코인 추가", color=0x00ff26)
            embedVar.add_field(name="",value=f"{member.name}님에게 **1sl**를 추가하였습니다.\n**잔여 :{points[member.id]}sl**",inline=False)
            await message.channel.send(embed=embedVar)
            await message.delete()
        if message.content.startswith('!d') and message.author.id in admin_ids:
            p_user = message.author
            point = points.get(p_user.id, 0)
            member = message.mentions[0]
            points[member.id] = points.get(member.id, 0) - 1
            embedVar = discord.Embed(title="코인 차감", color=0x00ff26)
            embedVar.add_field(name="",value=f"{member.name}님에게 **1sl**를 차감하였습니다.\n**잔여 :{points[member.id]}sl**",inline=False)
            await message.channel.send(embed=embedVar)
            await message.delete()
        if message.channel.id == 1128661547628109907 and message.author != bot.user:
            await message.delete()
        if message.channel.id == 1128673572798337137 and message.author != bot.user:
            await message.delete()
    except Exception as e:
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
if __name__ == "__main__":
    bot.run(TOKEN)
