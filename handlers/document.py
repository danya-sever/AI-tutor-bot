from aiogram import Router, F
from aiogram.types import Message
from services.pdf_reader import extract_text
from services.ai_service import generate_summary

router = Router()

@router.message(F.document)
async def handle_document(message: Message):

    bot = message.bot
    document = message.document

    if document.mime_type != 'application/pdf':
        await message.answer('Пожалуйста, отправьте PDF-файл.')
        return

    file_name = document.file_name
    file_path = f'data/{file_name}'

    await bot.download(document, destination=file_path)

    text = extract_text(file_path)

    await message.answer("🧠 Анализирую документ...")

    symbols = str(len(text)).replace(',', ' ')
    words = len(text.split())
    words_str = str(len(text.split())).replace(',', ' ')
    reading_time = max(1, round(words / 200))

    await message.answer(
        f"""
    📥 Документ успешно получен!

    📑 Название:
    {file_name}

    📊 Статистика

    • Символов: {symbols}
    • Слов: {words_str}
    • Время чтения: ≈ {reading_time} мин.

    🤖 Отправляю документ в Gemini...
    """
    )

    summary = generate_summary(text)
    summary += """
    
    
    🤖 Конспект подготовлен с помощью Google Gemini.
    ⚠️ При подготовке к экзаменам рекомендуется сверяться с оригинальным документом.
    """

    await message.answer(summary)
