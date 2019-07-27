#!/usr/bin/env python3
#
# A library that allows to create an inline calendar keyboard.
# grcanosa https://github.com/grcanosa
#
"""
Base methods for calendar keyboard creation and processing.
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
import datetime
import calendar


def create_callback_data(action, year, month, day):
    """ Create the callback data associated to each button"""
    return ";".join([action, str(year), str(month), str(day)])


def separate_callback_data(data):
    """ Separate the callback data"""
    return data.split(";")


def create_calendar(bot, update, year=None, month=None):
    """
    Create an inline keyboard with the provided year and month
    :param int year: Year to use in the calendar, if None the current year is used.
    :param int month: Month to use in the calendar, if None the current month is used.
    :return: Returns the InlineKeyboardMarkup object with the calendar.
    """
    query = update.callback_query
    name = query.data
    print(name)

    # 'словарь, чтобы работали условия'
    cd_split = name.split(';')

    now = datetime.datetime.now()
    if year is None:
        year = now.year
    if month is None:
        month = now.month
    data_ignore = create_callback_data("IGNORE", year, month, 0)
    keyboard = []

    # First row - Month and Year
    row = []
    row.append(InlineKeyboardButton(calendar.month_name[month]+" "+str(year),
                                    callback_data=data_ignore))
    keyboard.append(row)
    # Second row - Week Days
    row = []
    for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]:
        row.append(InlineKeyboardButton(day,
                                        callback_data=data_ignore))
    keyboard.append(row)
    my_calendar = calendar.monthcalendar(year, month)

    serg_list = [3, 4, 5, 6, 7, 8, 9, 17, 18, 19, 20, 21, 22, 23]
    dima_list = [1, 2, 3, 4, 8, 9, 10, 11, 15, 16, 17, 18, 22, 23, 24, 25]
    vova_list = [5, 6, 7, 8, 12, 13, 14, 15, 25, 26, 27, 28, 29, 30, 31]

    # переменная убирает дни которые прошли
    active_days = int(now.strftime("%d"))

    if name == 'Сергей' or\
            cd_split[0] == 'PREV-MONTH_SERG' or\
            cd_split[0] == 'NEXT-MONTH_SERG' or\
            name == 'Выбрать другой день Сергей':
        for week in my_calendar:
            row = []
            for day in week:
                if month == now.month:
                    # для текущего месяца
                    if day < active_days:
                        # убирает дни которые прошли
                        row.append(InlineKeyboardButton(" ",
                                                        callback_data=data_ignore))
                    elif day >= active_days and day in serg_list:
                        row.append(InlineKeyboardButton(str(day),
                                                        callback_data=create_callback_data('DAY', year, month, day)))
                    else:
                        row.append(InlineKeyboardButton(" ",
                                                        callback_data=data_ignore))
                elif month < now.month:
                    # убирает месяцы которые прошли
                    row.append(InlineKeyboardButton(" ",
                                                    callback_data=data_ignore))
                else:
                    # для следующих месяцев
                    if day in serg_list:
                        row.append(InlineKeyboardButton(str(day),
                                                        callback_data=create_callback_data('DAY', year, month, day)))
                    else:
                        row.append(InlineKeyboardButton(" ",
                                                        callback_data=data_ignore))

            keyboard.append(row)
        # Last row - Buttons
        row = []
        row.append(InlineKeyboardButton("<", callback_data=create_callback_data('PREV-MONTH_SERG', year, month, day)))
        row.append(InlineKeyboardButton(" ", callback_data=data_ignore))
        row.append(InlineKeyboardButton(">", callback_data=create_callback_data('NEXT-MONTH_SERG', year, month, day)))
        keyboard.append(row)
    elif name == 'Дима' or\
            cd_split[0] == "PREV-MONTH_DIMA" or\
            cd_split[0] == "NEXT-MONTH_DIMA" or\
            name == 'Выбрать другой день Дима':
        for week in my_calendar:
            row = []
            for day in week:
                if month == now.month:
                    if day < active_days:
                        row.append(InlineKeyboardButton(" ",
                                                        callback_data=data_ignore))
                    elif day >= active_days and day in dima_list:
                        row.append(InlineKeyboardButton(str(day),
                                                        callback_data=create_callback_data("DAY", year, month, day)))
                    else:
                        row.append(InlineKeyboardButton(" ",
                                                        callback_data=data_ignore))
                elif month < now.month:
                    row.append(InlineKeyboardButton(" ",
                                                    callback_data=data_ignore))
                else:
                    if day in dima_list:
                        row.append(InlineKeyboardButton(str(day),
                                                        callback_data=create_callback_data("DAY", year, month, day)))
                    else:
                        row.append(InlineKeyboardButton(" ",
                                                        callback_data=data_ignore))
            keyboard.append(row)
        row = []
        row.append(InlineKeyboardButton("<", callback_data=create_callback_data("PREV-MONTH_DIMA", year, month, day)))
        row.append(InlineKeyboardButton(" ", callback_data=data_ignore))
        row.append(InlineKeyboardButton(">", callback_data=create_callback_data("NEXT-MONTH_DIMA", year, month, day)))
        keyboard.append(row)
    elif name == 'Вова' or\
            cd_split[0] == "PREV-MONTH_VOVA" or\
            cd_split[0] == "NEXT-MONTH_VOVA" or\
            name == 'Выбрать другой день Вова':
        for week in my_calendar:
            row = []
            for day in week:
                if month == now.month:
                    if day < active_days:
                        row.append(InlineKeyboardButton(" ",
                                                        callback_data=data_ignore))
                    elif day >= active_days and day in vova_list:
                        row.append(InlineKeyboardButton(str(day),
                                                        callback_data=create_callback_data("DAY", year, month, day)))
                    else:
                        row.append(InlineKeyboardButton(" ",
                                                        callback_data=data_ignore))
                elif month < now.month:
                    row.append(InlineKeyboardButton(" ",
                                                    callback_data=data_ignore))
                else:
                    if day in vova_list:
                        row.append(InlineKeyboardButton(str(day),
                                                        callback_data=create_callback_data("DAY", year, month, day)))
                    else:
                        row.append(InlineKeyboardButton(" ",
                                                        callback_data=data_ignore))
            keyboard.append(row)
        row = []
        row.append(InlineKeyboardButton("<", callback_data=create_callback_data("PREV-MONTH_VOVA", year, month, day)))
        row.append(InlineKeyboardButton(" ", callback_data=data_ignore))
        row.append(InlineKeyboardButton(">", callback_data=create_callback_data("NEXT-MONTH_VOVA", year, month, day)))
        keyboard.append(row)
    elif name == 'Тимур' or\
            cd_split[0] == "PREV-MONTH_TIMUR" or\
            cd_split[0] == "NEXT-MONTH_TIMUR" or\
            name == 'Выбрать другой день Тимур':
        for week in my_calendar:
            row = []
            for day in week:
                if month == now.month:
                    if day < active_days:
                        row.append(InlineKeyboardButton(" ",
                                                        callback_data=data_ignore))
                    else:
                        row.append(InlineKeyboardButton(str(day),
                                                        callback_data=create_callback_data("DAY", year, month, day)))
                elif month < now.month:
                    row.append(InlineKeyboardButton(" ",
                                                    callback_data=data_ignore))
                else:
                    if day == 0:
                        row.append(InlineKeyboardButton(" ",
                                                        callback_data=data_ignore))
                    else:
                        row.append(InlineKeyboardButton(str(day),
                                                        callback_data=create_callback_data("DAY", year, month, day)))
            keyboard.append(row)
        row = []
        row.append(InlineKeyboardButton("<", callback_data=create_callback_data("PREV-MONTH_TIMUR", year, month, day)))
        row.append(InlineKeyboardButton(" ", callback_data=data_ignore))
        row.append(InlineKeyboardButton(">", callback_data=create_callback_data("NEXT-MONTH_TIMUR", year, month, day)))
        keyboard.append(row)
    return InlineKeyboardMarkup(keyboard)


def process_calendar_selection(bot, update):
    """
    Process the callback_query. This method generates a new calendar if forward or
    backward is pressed. This method should be called inside a CallbackQueryHandler.
    :param telegram.Bot bot: The bot, as provided by the CallbackQueryHandler
    :param telegram.Update update: The update, as provided by the CallbackQueryHandler
    :return: Returns a tuple (Boolean,datetime.datetime), indicating if a date is selected
                and returning the date if so.
    """
    ret_data = (False, None)
    query = update.callback_query
    (action, year, month, day) = separate_callback_data(query.data)
    curr = datetime.datetime(int(year), int(month), 1)
    if action == 'IGNORE':
        bot.answer_callback_query(callback_query_id=query.id)
    elif action == 'DAY':
        bot.edit_message_text(text=query.message.text,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
        ret_data = True, datetime.datetime(int(year), int(month), int(day))
    elif action == 'PREV-MONTH_VOVA' or \
            action == 'PREV-MONTH_DIMA' or \
            action == 'PREV-MONTH_SERG' or\
            action == 'PREV-MONTH_TIMUR':
        pre = curr - datetime.timedelta(days=1)
        bot.edit_message_text(text=query.message.text,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              reply_markup=create_calendar(bot, update, int(pre.year), int(pre.month)))
    elif action == 'NEXT-MONTH_VOVA' or\
            action == 'NEXT-MONTH_DIMA' or\
            action == 'NEXT-MONTH_SERG' or \
            action == 'NEXT-MONTH_TIMUR':
        ne = curr + datetime.timedelta(days=31)
        bot.edit_message_text(text=query.message.text,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              reply_markup=create_calendar(bot, update, int(ne.year), int(ne.month)))
    else:
        bot.answer_callback_query(callback_query_id=query.id,
                                  text="Something went wrong!")
    return ret_data
