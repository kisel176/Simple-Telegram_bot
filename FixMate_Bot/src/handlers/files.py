from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from src.states.report_states import ReportForm

files = Router()

@files.callback_query(F.data == 'upload_report')
async def upload_report_callback(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Пожалуйста, пришлите ваш пример отчёта (текстом или файлом).")
    await state.set_state(ReportForm.waiting_for_example)

@files.message(ReportForm.waiting_for_example)
async def process_example(message: Message, state: FSMContext):
    await state.update_data(example=message.text)
    await message.answer("Пример успешно загружен! Теперь пришлите ТЗ.")