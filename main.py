"""
Message Stitcher Bot — ДЕМО-версия.

⚠️ Это демонстрационная версия для ознакомления.
Полный рабочий код доступен в платной версии.

Полная версия включает:
- handlers.py — FSM, обработчики, умная склейка сообщений
- database.py — SQLite, работа с буферами
- main.py — полная точка входа с polling

📦 Купить полную версию: [ссылка на VibeDepot]
"""

import logging
import sys

from config import BOT_TOKEN

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s · %(levelname)s · %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)


def main():
    log.info("=" * 60)
    log.info("🚀 Message Stitcher Bot — ДЕМО-версия")
    log.info("=" * 60)
    log.info(f"✅ BOT_TOKEN загружен ({len(BOT_TOKEN)} символов)")

    log.info("")
    log.warning("⚠️ Это демо. Полный функционал доступен в платной версии.")
    log.warning("   Скрытые модули: handlers.py, database.py, main.py")
    log.warning("   Купить: [ссылка на VibeDepot]")
    log.info("")

    log.info("📖 Что умеет полная версия:")
    log.info("   • Сбор сообщений в буфер")
    log.info("   • Умная склейка (знаки препинания + заглавные буквы)")
    log.info("   • Работа в личке и группах")
    log.info("   • Предпросмотр буфера")
    log.info("   • Очистка с подтверждением")
    log.info("   • Админ-панель со статистикой")


if __name__ == "__main__":
    main()