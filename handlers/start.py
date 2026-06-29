from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(
        '👋🏻 Привет!\n\n'
        'Я - AI Tutor Bot, твой помощник в изучении PDF-файлов'
        '📄 Отправь мне PDF-файл, и я:\n'
        '• определю тему\n'
        '• составлю конспект\n'
        '• сделаю краткий вывод'
    )