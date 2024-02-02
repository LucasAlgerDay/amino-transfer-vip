import os
try: import edamino
except ModuleNotFoundError:
    os.system("pip3 install new-edamino")
    import edamino
import asyncio
try: import tqdm as tqdm_module  
except ModuleNotFoundError:
    os.system("pip3 install tqdm")
    import tqdm as tqdm_module  
try:from pyfiglet import figlet_format
except ModuleNotFoundError:
    os.system("pip3 install pyfiglet")
    from pyfiglet import figlet_format

print(
    f"""
Transfer Vip
Script by Lucas Day
Github : https://github.com/LucasAlgerDay"""
)
print(figlet_format("Transfer Vip", font="fourtops"))




client = edamino.Client()

async def main():
    await client.login(input("Email: "), input("Password: "))
    link = input("link vip: ")
    fok = await client.get_info_link(link)
    if fok.linkInfo.objectType != 0:
        print("The link needs to be from a user.")
        await asyncio.sleep(9999)
    else:
        try:
            await client.join_community(fok.linkInfo.ndcId)
        except Exception as e: pass
        amount = int(input("Amount of coins: "))
        count = 0
        client.set_ndc(fok.linkInfo.ndcId)
        for i in tqdm_module.tqdm(range(amount // 500)): 
            try:
                await client.subscribe(user_id=fok.linkInfo.objectId, auto_renew=False)
                count += 500
            except Exception as e:
                print(f"Error subscribing user: {e}")
        print(f"Coins sent: {count}")
        await asyncio.sleep(9999)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
