from pyrogram import Client
import asyncio

from pyrogram.raw.functions.messages import DeleteHistory

# Замените на свои значения
API_ID = "17349"
API_HASH = "344583e45741c457fe1862106095a5eb"

app = Client("delete_chats_session", api_id=API_ID, api_hash=API_HASH)


async def delete_all_chats():
    async with app:
        async for dialog in app.get_dialogs():
            chat_id = dialog.chat.id
            username = dialog.chat.username
            title = dialog.chat.title or dialog.chat.first_name or dialog.chat.last_name or "Без имени"

            if username:
                chat_display = f"@{username} ({title})"
            else:
                chat_display = title

            # Спросить подтверждение у пользователя
            print(f"Вы хотите удалить переписку с {chat_display}? [y/n]")
            # user_input = input().strip().lower()
            user_input = 'y'

            if user_input == "y" or True:
                try:
                    await app.invoke(
                        DeleteHistory(
                            peer=await app.resolve_peer(chat_id),
                            revoke=True,
                            max_id=10000000
                        )
                    )
                    print(f"Переписка с {chat_display} успешно удалена.")
                except Exception as e:
                    print(f"Ошибка при удалении переписки с {chat_display}: {e}")
            else:
                print(f"Переписка с {chat_display} пропущена.")


if __name__ == "__main__":
    app.run(delete_all_chats())
