"""
Автор: Константин Одинцов
e-mail: kos5172@yandex.ru
Github: https://github.com/odintsovkos
Этот файл — часть SDTelegramBot.

SDTelegramBot — свободная программа: вы можете перераспространять ее и/или изменять ее на условиях Стандартной общественной лицензии GNU в том виде, в каком она была опубликована Фондом свободного программного обеспечения; либо версии 3 лицензии, либо (по вашему выбору) любой более поздней версии.

SDTelegramBot распространяется в надежде, что она будет полезной, но БЕЗО ВСЯКИХ ГАРАНТИЙ; даже без неявной гарантии ТОВАРНОГО ВИДА или ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННЫХ ЦЕЛЕЙ. Подробнее см. в Стандартной общественной лицензии GNU.

Вы должны были получить копию Стандартной общественной лицензии GNU вместе с этой программой. Если это не так, см. <https://www.gnu.org/licenses/>.
"""

# BUTTONS
# All cancel button
cancel = "◀️ Назад"

# Main menu
repeat = "🔄 Повторить"
repeat_with_seed = "🔄 Повторить с Seed"
model = "Модель"
styles = "Стили"
loras = "LoRa"
settings = "⚙️ Настройки"

# Settings menu
current_settings = "🛠 Текущие Настройки"
negative_prompt = "🙅 Negative Prompt"
sampler = "🎛 Sampler"
steps = "👣 Steps"
width_height = "📐 Width x Height"
cfg_scale = "🎚 CFG Scale"
batch_count = "👩‍👩‍👧‍👧 Batch count"
reset_settings = "📝 Сброс настроек"
restart_sd = "🆘 Перезапуск SD"
hr_settings = "🔍 HR Settings"
gen_settings = "⚙️ Настройки генерации"

# Hires settings menu
hr_on_off = "On/Off"
hr_upscaler = "Upscaler"
hr_steps = "Steps"
hr_denoising_strength = "Denoising Strength"
hr_upscale_by = "Upscale by"

# Other menu
confirm = "✅ Подтвердить"
disable_all = "🚫 Отключить все"

# Width x Height
wh_buttons = ["[1:1] 512x512", "[1:1] 768x768", "[1:1] 1024x1024", "[2:3] 512x768", "[3:2] 768x512", "[4:3] 768x576",
              "[3:4] 576x768", "[16:9] 768x432", "[9:7] 1152x896", "[7:9] 896x1152", "[19:13] 1216x832", 
              "[13:19] 832x1216", "[7:4] 1344x768", "[4:7] 768x1344", "[12:5] 1536x640", "[5:12] 640x1536"]
