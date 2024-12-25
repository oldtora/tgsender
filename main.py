from telethon import TelegramClient, events
import random
import os
import asyncio
from utils import load_accounts, load_groups, load_phrases, send_alert

# Путь к файлам
ACCOUNTS_FILE = "accounts.txt"
GROUPS_FILE = "groups.txt"
PHRASES_FILE = "phrases.txt"
IMAGE_FOLDER = "images"

# Загрузка данных
accounts = load_accounts(ACCOUNTS_FILE)
groups = load_groups(GROUPS_FILE)
phrases = load_phrases(PHRASES_FILE)

# Создание клиентов
clients = [TelegramClient(acc['session'], acc['api_id'], acc['api_hash']) for acc in accounts]

# Рандомизация данных
def get_random_account():
    return random.choice(clients)

def get_random_phrase():
    return random.choice(phrases)

def get_random_image():
    files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return os.path.join(IMAGE_FOLDER, random.choice(files)) if files else None

# Проверка подписки и бана
async def check_membership(client, chat):
    try:
        participant = await client.get_participants(chat, filter=telethon.tl.types.ChannelParticipantsSelf)
        if participant:
            return "subscribed"
    except telethon.errors.ChatAdminRequiredError:
        return "banned"
    except telethon.errors.UserNotParticipantError:
        return "not_subscribed"

# Подписка на канал
async def subscribe_to_channel(client, chat):
    try:
        await client(telethon.tl.functions.channels.JoinChannelRequest(chat))
        return True
    except Exception as e:
        print(f"Ошибка подписки: {e}")
        return False

# Отправка комментария
async def send_random_comment(event, client):
    try:
        # Проверка подписки и бана
        membership_status = await check_membership(client, event.chat_id)
        if membership_status == "not_subscribed":
            subscribed = await subscribe_to_channel(client, event.chat_id)
            if not subscribed:
                send_alert(f"Не удалось подписаться на канал {event.chat_id}")
                return

        if membership_status == "banned":
            send_alert(f"Аккаунт {client.session_name} забанен в {event.chat_id}. Смена аккаунта.")
            return

        # Отправка комментария
        comment = get_random_phrase()
        image_path = get_random_image()
        if image_path:
            await client.send_file(
                entity=event.chat,
                file=image_path,
                caption=comment,
                comment_to=event.message.id
            )
            print(f"[{client.session_name}] Отправлен комментарий с изображением: '{comment}'")
        else:
            send_alert(f"Ошибка: нет изображений для отправки!")
    except Exception as e:
        send_alert(f"Ошибка отправки комментария: {e}")
        print(f"Ошибка: {e}")

# Основная функция
async def main():
    await asyncio.gather(*(client.start() for client in clients))

    for client in clients:
        @client.on(events.NewMessage(chats=groups))
        async def new_post_handler(event):
            await send_random_comment(event, client)

    print("Запуск мониторинга...")
    await asyncio.gather(*(client.run_until_disconnected() for client in clients))

# Запуск
asyncio.run(main())
