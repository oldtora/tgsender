# Рандомизация данных
def get_random_phrase():
    return random.choice(phrases)

# Отправка комментария
async def send_random_comment(event, client):
    try:
        comment = get_random_phrase()  # Получаем случайную фразу из phrases.txt

        # Проверяем, является ли аккаунт участником канала
        try:
            await client.get_participants(event.chat_id)
            print(f"[{client.session.filename}] Аккаунт уже находится в канале.")
        except Exception:
            print(f"[{client.session.filename}] Аккаунт не в канале. Присоединяюсь...")
            try:
                await client(JoinChannelRequest(event.chat_id))  # Присоединяемся к каналу
                print(f"[{client.session.filename}] Успешно присоединился к каналу.")
                await asyncio.sleep(5)  # Задержка для обработки
            except Exception as e:
                print(f"[{client.session.filename}] Ошибка при присоединении к каналу: {e}")
                return

        # Получаем информацию о группе обсуждений
        try:
            discussion = await client(GetDiscussionMessageRequest(
                peer=event.chat_id,  # Канал
                msg_id=event.message.id  # ID сообщения в канале
            ))
            discussion_group_id = discussion.messages[0].peer_id.channel_id  # ID группы обсуждений
            reply_to_msg_id = discussion.messages[0].id  # ID сообщения в группе обсуждений
        except Exception as e:
            print(f"[{client.session.filename}] Не удалось получить привязанную группу обсуждений: {e}")
            return

        # Проверяем, является ли аккаунт участником группы обсуждений
        try:
            await client.get_participants(discussion_group_id)
            print(f"[{client.session.filename}] Аккаунт уже находится в группе обсуждений.")
        except Exception:
            print(f"[{client.session.filename}] Аккаунт не в группе обсуждений. Присоединяюсь...")
            try:
                await client(JoinChannelRequest(discussion_group_id))  # Присоединяемся к группе обсуждений
                print(f"[{client.session.filename}] Успешно присоединился к группе обсуждений.")
                await asyncio.sleep(10)  # Задержка для обработки присоединения
            except Exception as e:
                print(f"[{client.session.filename}] Ошибка при присоединении к группе обсуждений: {e}")
                return

        # Отправляем комментарий
        await client.send_message(
            entity=discussion_group_id,  # Группа обсуждений
            message=comment,  # Текст комментария
            reply_to=reply_to_msg_id  # Привязка к сообщению
        )
        print(f"[{client.session.filename}] Отправлен комментарий: '{comment}'")
    except Exception as e:
        print(f"[{client.session.filename}] Ошибка отправки комментария: {e}")

# Основная функция
async def main():
    try:
        # Старт всех клиентов
        for client in clients:
            await client.connect()
            if not await client.is_user_authorized():
                print(f"Сессия для {client.session.filename} не авторизована. Проверьте файл сессии!")
                exit(1)

        for client in clients:
            @client.on(events.NewMessage(chats=groups))
            async def new_post_handler(event):
                await send_random_comment(event, client)

        print("Запуск мониторинга...")
        await asyncio.gather(*(client.run_until_disconnected() for client in clients))
    except Exception as e:
        print(f"Ошибка в основном процессе: {e}")
        exit(1)

# Запуск
asyncio.run(main())
