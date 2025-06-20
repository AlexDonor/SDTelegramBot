"""
Автор: Константин Одинцов
e-mail: kos5172@yandex.ru
Github: https://github.com/odintsovkos
Этот файл — часть SDTelegramBot.

SDTelegramBot — свободная программа: вы можете перераспространять ее и/или изменять ее на условиях Стандартной общественной лицензии GNU в том виде, в каком она была опубликована Фондом свободного программного обеспечения; либо версии 3 лицензии, либо (по вашему выбору) любой более поздней версии.

SDTelegramBot распространяется в надежде, что она будет полезной, но БЕЗО ВСЯКИХ ГАРАНТИЙ; даже без неявной гарантии ТОВАРНОГО ВИДА или ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННЫХ ЦЕЛЕЙ. Подробнее см. в Стандартной общественной лицензии GNU.

Вы должны были получить копию Стандартной общественной лицензии GNU вместе с этой программой. Если это не так, см. <https://www.gnu.org/licenses/>.
"""


from utils.sd_api import api_service

# True сохраняет сгенерированные файлы в папку "outputs/txt2img-images"
save_files = True

# Путь к папке для сохраненный изображений. Пример: "outputs/txt2img-images"
output_folder = 'outputs/txt2img-images'

# Включение дополнения ADetailer
adetailer_on = False


# Параметры по умолчанию
def get_default_params(tg_id):
    model = api_service.get_models_sd_api()
    upscalers = api_service.get_hr_upscaler_sd_api()
    params = {"user_id": tg_id,
              "model_name": model[0]['model_name'],
              "styles_list": '',
              "lora_list": '',
              "negative_prompt": '(deformed, distorted, disfigured:1.3), poorly drawn, [bad : wrong] anatomy,'
                                 '[extra | missing | floating | disconnected] limbs, [bad | ugly] face,'
                                 '(mutated hands and fingers:1.4), ugly, disgusting, blurry, amputation,'
                                 'jpeg artifacts, signature, watermark, username',
              "sampler_name": 'Euler a',
              "steps": 22,
              "width_height": '640x640',
              "cfg_scale": '7.0',
              "batch_count": 1,
              "enable_hr": 0,
              "hr_upscaler": upscalers[1]['name'],
              "hr_second_pass_steps": 12,
              "denoising_strength": 0.2,
              "hr_scale": 2}

    return params
