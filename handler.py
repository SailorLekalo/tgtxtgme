import player
import duel
import random
from aiogram import Router, Bot, Dispatcher, F
from aiogram.filters import Command, StateFilter, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from keyboards import fight_kb, base_kb

router = Router()
dp = Dispatcher()

class stances(StatesGroup):
    berserk = State()
    agression = State()
    ready = State()
    restraint = State()
    serenity = State()

class condition(StatesGroup):
    in_fight = State()
    not_in_fight = State()

@router.message(Command("challenge"), StateFilter(condition.not_in_fight))
async def challenge_fight(message: Message, command: CommandObject, state: FSMContext, bot: Bot, dp: Dispatcher):
    if command.args:
        enemy_id = int(command.args)

        text = f"Вызов игроку {enemy_id} брошен."
        await message.answer(text=text)

        text = f"Вам бросил вызов игрок {message.from_user.first_name}. Начинаем бой..."
        await bot.send_message(chat_id=enemy_id, text=text)

        # Отправляем врагу в контекст свой ID
        fsm: FSMContext = dp.fsm.resolve_context(bot=bot, user_id=enemy_id, chat_id=enemy_id)
        await fsm.set_state(condition.in_fight)
        await fsm.update_data(enemy_id=message.from_user.id)

        # Сохраняем в своём контексте ID врага
        await state.set_state(condition.in_fight)
        await state.update_data(enemy_id=enemy_id)

        current_duel = await duel.create(message.from_user.id, enemy_id)
        if current_duel:
            await message.answer("Лобби файта создано успешно!")
            await bot.send_message(current_duel.defender, f"Лобби файта создано успешно!")

@router.message(Command("challengebot"), StateFilter(condition.not_in_fight))
async def challenge_fight(message: Message, command: CommandObject, state: FSMContext, bot: Bot, dp: Dispatcher):
    enemy_id = int(command.args)
    enemy = player.FindPlayerById(enemy_id)
    you = player.FindPlayerById(message.from_user.id)
    text = f"Вызов игроку {enemy.nickname} брошен."

    stance = "testStance"

    await message.answer(text=text)
    await state.set_state(condition.in_fight)
    current_duel = await duel.create(message.from_user.id, enemy_id)
    if current_duel:
        await message.answer("Лобби файта создано успешно!")
        text = (
            f'{you.nickname} 🔸{you.level} | ❤️ ({you.health_points}/100)\n'
            f'╚🆚╗\n'
            f'{enemy.nickname} 🔸{enemy.level} | ❤️ ({enemy.health_points}/100)\n'
            f'\n'
            f'\n'
            f'{stance}'
        )
        markup = fight_kb
        await message.answer(text=text, reply_markup=markup)

@router.message(F.text == 'Сбежать', StateFilter(condition.in_fight))
async def run(message: Message, state: FSMContext):

    #Сюда формула, которая ответственна за определение вероятности на побег от 0 до 100.
    running_chance = 70

    if (running_chance>random.randint(0,100)):
        markup = base_kb
        await state.set_state(condition.not_in_fight)

        duel.close(player.FindPlayerById(message.from_user.id).infight)
        await message.answer(text="Вы успешно сбежали", reply_markup=markup)
    else:
        #await bot.send_message(chat_id=enemy_id, text=text)
        await message.answer("Вы не смогли сбежать.")


@router.message(Command("accept"), StateFilter(condition.not_in_fight))
async def accept_fight(message: Message, bot: Bot, dp: Dispatcher, state: FSMContext, player: player, i18n):
    pass


#техническая команда, чтобы выдать игроку condition.not_in_fight. Следует потом выдавать этот кондишн игроку как-нибудь ещё.
@router.message(Command("unfight"))
async def unfight(message: Message, state: FSMContext):
    await state.set_state(condition.not_in_fight)