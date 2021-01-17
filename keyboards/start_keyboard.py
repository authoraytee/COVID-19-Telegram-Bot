from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


inline_kb_full = InlineKeyboardMarkup(row_width=1)
inline_kb_full.add(
    InlineKeyboardButton('1. Global Stats', callback_data='world_stat'),
    InlineKeyboardButton('2. Detailed info', callback_data='detailed_info'),
    InlineKeyboardButton('3. Latest news', callback_data='news'),
    InlineKeyboardButton('4. TOP-20', callback_data='top_20'),
    InlineKeyboardButton('5. My Country', callback_data='my_country'),
    InlineKeyboardButton('6. FAQ about COVID-19', callback_data='faq'),
    InlineKeyboardButton('--- Get Help ---', callback_data='help'),
    InlineKeyboardButton('--- About Bot ---', callback_data='about'),
)

