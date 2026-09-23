"""
Клавиатуры бота «Склейка сообщений».
"""
from aiogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu() -> ReplyKeyboardMarkup:
    """Главное меню в личке бота."""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Мои сообщения")],
            [
                KeyboardButton(text="🔗 Склеить"),
                KeyboardButton(text="🗑 Очистить"),
            ],
            [KeyboardButton(text="❓ Помощь")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Пишите сообщения — я собираю…",
    )


def stitch_kb(count: int = 0) -> InlineKeyboardMarkup:
    """Кнопка «Склеить» с счётчиком."""
    builder = InlineKeyboardBuilder()
    label = f"🔗 Склеить ({count})" if count else "🔗 Склеить"
    builder.button(text=label, callback_data="do_stitch")
    builder.button(text="👁 Посмотреть", callback_data="preview")
    builder.button(text="🗑 Очистить", callback_data="clear_buffer")
    builder.adjust(1)
    return builder.as_markup()


def group_stitch_kb() -> InlineKeyboardMarkup:
    """Кнопки для работы в группах."""
    builder = InlineKeyboardBuilder()
    builder.button(text="🔗 Склеить", callback_data="do_stitch")
    builder.button(text="👁 Посмотреть", callback_data="preview")
    builder.adjust(2)
    return builder.as_markup()


def result_kb() -> InlineKeyboardMarkup:
    """Кнопки после склейки."""
    builder = InlineKeyboardBuilder()
    builder.button(text="📤 Отправить в чат", callback_data="send_to_chat")
    builder.button(text="📋 Скопировать", callback_data="copy_help")
    builder.button(text="🗑 Очистить буфер", callback_data="clear_buffer")
    builder.adjust(1)
    return builder.as_markup()


def confirm_clear_kb() -> InlineKeyboardMarkup:
    """Подтверждение очистки."""
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Да, очистить", callback_data="confirm_clear")
    builder.button(text="❌ Отмена", callback_data="cancel_clear")
    builder.adjust(2)
    return builder.as_markup()


def admin_menu() -> InlineKeyboardMarkup:
    """Админ-панель."""
    builder = InlineKeyboardBuilder()
    builder.button(text="📊 Статистика", callback_data="admin_stats")
    builder.adjust(1)
    return builder.as_markup()


def back_to_menu_kb() -> InlineKeyboardMarkup:
    """Возврат в меню."""
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ В меню", callback_data="back_to_menu")
    return builder.as_markup()