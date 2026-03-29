const TelegramBot = require('node-telegram-bot-api');
const axios = require('axios');

// 🔐 ВСТАВ СЮДИ СВІЙ НОВИЙ ТОКЕН
const TOKEN = '8717329314:AAGo2P9dXE6WT4xygLrrzK-pAytT0Ix-_eM';

// 📊 Твій Google Apps Script URL
const GOOGLE_URL = 'https://script.google.com/macros/s/AKfycbzecpCxyABxFy6H4A76BjK-fnQe2Tj6HbJRh55juHRqfz2OcdJ4ZdkMms_oP2xfhkvOfw/exec';

const bot = new TelegramBot(TOKEN, { polling: true });

bot.on('message', async (msg) => {
  const chatId = msg.chat.id;

  // Беремо дані користувача
  const data = {
    user_id: msg.from.id,
    username: msg.from.username || 'no_username',
    text: msg.text || ''
  };

  try {
    // Відправка в Google Sheets
    await axios.post(GOOGLE_URL, data);

    // Відповідь користувачу
    bot.sendMessage(chatId, '☀️ Прийнято! Дані записані');
  } catch (error) {
    console.error(error);
    bot.sendMessage(chatId, '❌ Помилка запису');
  }
});
