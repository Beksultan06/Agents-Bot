from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def create_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📱 SSM", callback_data="agent_ssm"),
         InlineKeyboardButton(text="✍️ Копирайтер", callback_data="agent_copywriter")],
        [InlineKeyboardButton(text="🎬 Сценарист", callback_data="agent_scriptwriter"),
         InlineKeyboardButton(text="🤖 GPT", callback_data="agent_cpt")],
    ])