import logging
import sys
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

# Формат логов
formatter = logging.Formatter(
    '%(asctime)s | %(levelname)-7s | %(name)s | %(message)s',
    datefmt='%H:%M:%S'
)

# Консоль
console = logging.StreamHandler(sys.stdout)
console.setFormatter(formatter)

# Файл со всеми логами
file_all = logging.FileHandler('logs/bot.log', encoding='utf-8')
file_all.setFormatter(formatter)
file_all.setLevel(logging.DEBUG)

# Файл только с ошибками
file_errors = logging.FileHandler('logs/errors.log', encoding='utf-8')
file_errors.setFormatter(formatter)
file_errors.setLevel(logging.ERROR)

# Корневой логгер
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(console)
root_logger.addHandler(file_all)
root_logger.addHandler(file_errors)

# Убираем спам от библиотек
logging.getLogger('aiogram').setLevel(logging.WARNING)
logging.getLogger('asyncio').setLevel(logging.WARNING)
logging.getLogger('aiohttp').setLevel(logging.WARNING)

logger = logging.getLogger('src')