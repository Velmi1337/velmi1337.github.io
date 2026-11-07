#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
"""Generate crawlable, script-free English/Russian project pages."""
from pathlib import Path
from html import escape as e
import json

ROOT=Path(__file__).resolve().parents[1]
BASE='https://velmi1337.github.io'
GH='https://github.com/Velmi1337'
COPY={'en': {'home': 'Projects',
        'lang': 'Русский',
        'code': 'Source code',
        'download': 'Download on GitHub',
        'docs': 'Read the documentation',
        'issues': 'Report a problem',
        'back': 'All projects',
        'footer': 'Independent open-source projects by Velmi1337.',
        'site_source': 'Website source',
        'skip': 'Skip to content',
        'title': 'Velmi1337 — CTSV for Android & ALOL for Arizona RP and Rodina RP on Linux',
        'description': 'Open-source projects by Velmi1337: CTSV for Circle to Search on Android and ALOL '
                       '1.0.0 for Arizona RP and Rodina RP on Linux. Material 3 Expressive, downloads and '
                       'guides.',
        'hero': 'Android search.<br>Linux gaming.',
        'lead': 'Two open-source tools by Velmi1337: Circle to Search on Android with CTSV, and Arizona RP '
                'or Rodina RP on Linux with ALOL.',
        'explore': 'Find your project',
        'github': 'View GitHub profile',
        'eyebrow': 'Small, focused, open source',
        'projects_title': 'Choose your tool',
        'projects_subtitle': 'Source code, releases and practical setup guides.',
        'ctsv_summary': 'Circle to Search without root.',
        'ctsv_text': 'Open Google’s search from a Quick Settings tile, a configurable hold zone or a '
                     'shortcut. Choose English or Russian.',
        'ctsv_explore': 'Explore CTSV',
        'ctsv_platform': 'Android 9+ · no root',
        'ctsv_tags': ['Quick Settings', 'Hold gestures', 'GPL-3.0-only'],
        'alol_summary': 'Arizona RP. Rodina RP. Linux.',
        'alol_text': 'ALOL 1.0.0 is the first stable release: a native Rust/GTK 3 launcher with Material 3 '
                     'Expressive, Wine/Proton, separate game settings and a reversible mod manager.',
        'alol_explore': 'Explore ALOL',
        'alol_platform': 'Linux · x86_64',
        'alol_tags': ['1.0.0 stable', 'Material 3 Expressive', 'Arizona + Rodina'],
        'start_title': 'Start with a release.',
        'start_steps': [('Choose your platform', 'CTSV is for Android. ALOL is for Linux on x86_64.'),
                        ('Download from the project’s GitHub',
                         'Release pages contain binaries and checksums. Each project documents its own setup '
                         'requirements.'),
                        ('Help make it better',
                         'Found a reproducible problem? Open an issue with the app version, device or '
                         'distribution, and steps to reproduce.')],
        'ctsv_title': 'CTSV — Circle to Search without root for Android',
        'ctsv_description': 'CTSV is an open-source Android launcher for Google Circle to Search. Use Quick '
                            'Settings, a hold zone or automation. English/Russian interface, no root, '
                            'configurable shade delay.',
        'ctsv_heading': 'CTSV: Circle to Search without root.',
        'ctsv_intro': 'Bring Google’s screen search within reach. Start from a tile, hold and release a '
                      'small zone, or map your own shortcut.',
        'ctsv_alt': 'CTSV Android settings showing Quick Settings setup and a configurable launch delay',
        'ctsv_requirement': 'Requires the Google app, Google as your digital assistant, and Circle to Search '
                            'availability for your device/account. CTSV cannot enable a feature Google has '
                            'blocked.',
        'ctsv_setup_heading': 'Set up your first search.',
        'ctsv_steps': ['Install the APK from the latest GitHub release. Official updates use the same '
                       'signing key.',
                       'Install or update Google, choose it as your digital assistant in Android settings, '
                       'then test Launch Circle to Search.',
                       'Tap Add to Quick Settings and confirm Android’s prompt. Custom/older panels may need '
                       'manual tile editing.',
                       'For a hold zone, enable it and choose standard overlay or accessibility mode. Hold '
                       'for the configured duration, then release after the haptic cue.'],
        'triggers_heading': 'Choose how it starts.',
        'trigger_headers': ['Trigger', 'Required access', 'When to use it'],
        'trigger_rows': [['Quick Settings tile',
                          'Neither hold-zone permission',
                          'A simple trigger with the lowest background overhead.'],
                         ['Standard hold zone',
                          'Display over other apps; foreground notification',
                          'A persistent touch target without accessibility access.'],
                         ['Accessibility hold zone',
                          'Enabled accessibility service',
                          'An alternative overlay mode; no window-content reading.'],
                         ['Automation shortcut',
                          'Your automation tool / firmware support',
                          'Launch app.ctsv/.TriggerActivity from a custom action.']],
        'ctsv_tuning_heading': 'Tune the gesture, not your phone.',
        'ctsv_tuning': ['Hold duration, width, left/center/right position, navigation offset, opacity and '
                        'haptic feedback are configurable.',
                        'If search captures the shade or a blurred screen, increase the shade launch delay. '
                        'The range is 200–3000 ms; 800 ms is the default. Try 1000–1500 ms for slower panel '
                        'animations.',
                        'Successful requests do not show a toast. Diagnostics stay local. CTSV has no '
                        'internet permission or analytics; Google handles the actual search.'],
        'ctsv_limits_heading': 'Compatibility, honestly.',
        'ctsv_limits': 'Android 9+ is the declared minimum; the automated emulator checks currently use '
                       'Android 15. Actual CTS availability, closing behavior and vendor background '
                       'restrictions need physical-device testing. The zone is separate from the system Home '
                       'handle.',
        'ctsv_links': 'Read the detailed setup, battery behavior, privacy notes and test scope in the '
                      'project documentation. CTSV is independent of Google and phone manufacturers.',
        'alol_title': 'ALOL 1.0.0 — Arizona RP and Rodina RP on Linux · MD3E',
        'alol_description': 'The first stable ALOL release: Arizona RP and Rodina RP on Linux with Material '
                            '3 Expressive (MD3E), light/dark themes, Wine/Proton, mods, logs and launcher '
                            'updates.',
        'alol_heading': 'ALOL 1.0.0. Two games. One launcher.',
        'alol_intro': 'The first stable release brings Arizona RP and Rodina RP together on Linux. A '
                      'Material 3 Expressive interface keeps servers, game settings, mods and diagnostics '
                      'within reach.',
        'alol_alt': 'ALOL 1.0.0 Material 3 Expressive interface with Arizona RP and Rodina RP selection, '
                    'server and launch actions',
        'alol_requirement': 'For Linux x86_64. Game files and Windows components are not bundled. You need '
                            'the official Arizona installer, an appropriate Wine/Proton environment and '
                            'suitable graphics drivers.',
        'alol_setup_heading': 'Get a game environment ready.',
        'alol_steps': ['Download ALOL 1.0.0 for your platform: Arch/CachyOS, Fedora 44+, or the standalone '
                       'x86_64 executable.',
                       'Install using the guide. Choose light or dark appearance in Settings → Launcher.',
                       'Select the official Arizona Games installer in ALOL, then download the selected game '
                       'through the official launcher.',
                       'Close the official launcher, choose Arizona RP or Rodina RP and a server, then '
                       'launch. Arizona uses a saved nickname; Rodina asks for it in-game.'],
        'alol_features_heading': 'A new interface. A simpler routine.',
        'alol_features': [('Arizona RP and Rodina RP',
                           'Switch games with separate server choices, settings, mod catalogs and repair '
                           'targets. Arizona nicknames stay per-server; Rodina naming stays in-game.'),
                          ('Material 3 Expressive',
                           'Google Sans, light/dark themes, adaptive navigation and short settings '
                           'categories. Switches save instantly; Ctrl+Enter launches the game.'),
                          ('Mods with rollback',
                           'Browse the catalog, manage installed mods or add an archive. Inspect files and '
                           'dependencies before installation, then enable, disable or remove with file '
                           'restoration.'),
                          ('Useful operation logs',
                           'Search records, filter errors, pause updates, follow new lines, copy the visible '
                           'view and clear the current log and archive.'),
                          ('Wine, Proton and maintenance',
                           'Prepare fonts and components, keep Russian locale local to the game, repair '
                           'common issues with backups, and check for ALOL updates.')],
        'alol_limits_heading': 'Read the requirements first.',
        'alol_limits': 'Published packages target Linux x86_64, with instructions for Arch/CachyOS and '
                       'Fedora 44+. Runtime and graphics compatibility vary. The launcher is independent of '
                       'Arizona Games and does not include the game.',
        'alol_license': 'ALOL 1.0.0 code is Apache-2.0. Bundled Google Sans is OFL-1.1; the optional Wine '
                        'patch is LGPL-2.1-or-later with corresponding source. Earlier tags retain their own '
                        'licenses.',
        'alol_demo': 'The screenshot uses the project’s demonstration profile. It shows the interface, not a '
                     'claim of a verified live game session.',
        'alol_community': 'Release news and updates: @alolinux on Telegram.',
        'feedback': 'Have a specific question or bug?',
        'feedback_text': 'Read the setup guide first, then describe what you tried and what happened. Useful '
                         'reports help improve the project.'},
 'ru': {'home': 'Проекты',
        'lang': 'English',
        'code': 'Исходный код',
        'download': 'Скачать на GitHub',
        'docs': 'Открыть документацию',
        'issues': 'Сообщить о проблеме',
        'back': 'Все проекты',
        'footer': 'Независимые открытые проекты Velmi1337.',
        'site_source': 'Исходники сайта',
        'skip': 'Перейти к содержимому',
        'title': 'Velmi1337 — CTSV для Android и ALOL для Arizona RP и Родины RP на Linux',
        'description': 'Открытые проекты Velmi1337: CTSV для Circle to Search на Android и ALOL 1.0.0 для '
                       'Arizona RP и Родины RP на Linux. Material 3 Expressive, загрузки и инструкции.',
        'hero': 'Поиск на Android.<br>Игры на Linux.',
        'lead': 'Два открытых проекта Velmi1337: поиск на Android через CTSV и Arizona RP или Родина RP на '
                'Linux через ALOL.',
        'explore': 'Выбрать проект',
        'github': 'Профиль GitHub',
        'eyebrow': 'Небольшие задачи. Открытый код.',
        'projects_title': 'Выберите свой инструмент',
        'projects_subtitle': 'Исходники, релизы и инструкции по настройке.',
        'ctsv_summary': 'Circle to Search без root.',
        'ctsv_text': 'Запускайте поиск Google плиткой пункта управления, настраиваемой зоной удержания или '
                     'ярлыком. Интерфейс на русском и английском.',
        'ctsv_explore': 'Подробнее о CTSV',
        'ctsv_platform': 'Android 9+ · без root',
        'ctsv_tags': ['Плитка в шторке', 'Удержание зоны', 'GPL-3.0-only'],
        'alol_summary': 'Arizona RP. Родина RP. Linux.',
        'alol_text': 'ALOL 1.0.0 — первый стабильный релиз: нативный лаунчер на Rust/GTK 3 с Material 3 '
                     'Expressive, Wine/Proton, отдельными настройками игр и управлением модами с откатом.',
        'alol_explore': 'Подробнее об ALOL',
        'alol_platform': 'Linux · x86_64',
        'alol_tags': ['Стабильная 1.0.0', 'Material 3 Expressive', 'Arizona + Родина'],
        'start_title': 'Начните с релиза.',
        'start_steps': [('Выберите платформу', 'CTSV предназначен для Android, ALOL — для Linux x86_64.'),
                        ('Скачайте с GitHub проекта',
                         'В релизах есть файлы и контрольные суммы. Для каждого проекта описаны собственные '
                         'требования к настройке.'),
                        ('Помогите улучшить проект',
                         'Нашли воспроизводимую ошибку? Укажите версию, устройство или дистрибутив и шаги '
                         'воспроизведения в issue.')],
        'ctsv_title': 'CTSV — Circle to Search без root для Android',
        'ctsv_description': 'CTSV — открытое Android-приложение для запуска Google Circle to Search плиткой, '
                            'удержанием зоны или автоматизацией. Без root, с настройкой задержки и '
                            'русским/английским интерфейсом.',
        'ctsv_heading': 'CTSV: Circle to Search без root.',
        'ctsv_intro': 'Поиск по экрану — под рукой. Запускайте его плиткой, удержанием и отпусканием '
                      'небольшой зоны или собственным ярлыком.',
        'ctsv_alt': 'Настройки CTSV на Android: добавление плитки в пункт управления и задержка запуска из '
                    'шторки',
        'ctsv_requirement': 'Нужны приложение Google, Google в роли цифрового помощника и доступность Circle '
                            'to Search для устройства/аккаунта. CTSV не снимает запреты Google.',
        'ctsv_setup_heading': 'Настройте первый поиск.',
        'ctsv_steps': ['Установите APK из последнего релиза GitHub. Официальные обновления используют один '
                       'ключ подписи.',
                       'Установите или обновите Google, выберите его цифровым помощником в Android и '
                       'проверьте кнопку запуска CTS.',
                       'Нажмите «Добавить в пункт управления» и подтвердите запрос. На старых/нестандартных '
                       'панелях добавьте плитку вручную.',
                       'Для зоны включите её и выберите обычный режим либо специальные возможности. '
                       'Удерживайте заданное время и отпустите палец после виброотклика.'],
        'triggers_heading': 'Выберите способ запуска.',
        'trigger_headers': ['Способ', 'Нужный доступ', 'Для чего'],
        'trigger_rows': [['Плитка пункта управления',
                          'Разрешения зоны не нужны',
                          'Простой запуск с минимальной фоновой нагрузкой.'],
                         ['Обычная зона',
                          'Поверх приложений; уведомление foreground-сервиса',
                          'Постоянная область касания без специальных возможностей.'],
                         ['Зона accessibility',
                          'Включённый сервис специальных возможностей',
                          'Альтернативный режим без чтения содержимого окон.'],
                         ['Ярлык автоматизации',
                          'Поддержка вашей программы / прошивки',
                          'Запуск компонента app.ctsv/.TriggerActivity.']],
        'ctsv_tuning_heading': 'Настройте жест под себя.',
        'ctsv_tuning': ['Меняются время удержания, ширина, положение слева/по центру/справа, отступ от '
                        'навигации, прозрачность и виброотклик.',
                        'Если в поиск попадает шторка или остаётся размытие, увеличьте задержку: диапазон '
                        '200–3000 мс, по умолчанию 800 мс. Для медленной анимации попробуйте 1000–1500 мс.',
                        'Успешный запрос не вызывает всплывающее сообщение. Диагностика хранится локально. В '
                        'CTSV нет разрешения на интернет и аналитики; сам поиск выполняет Google.'],
        'ctsv_limits_heading': 'Совместимость без обещаний.',
        'ctsv_limits': 'Заявленная минимальная версия — Android 9. Автоматические проверки сейчас идут на '
                       'Android 15. Доступность CTS, возврат после закрытия и ограничения фона прошивки '
                       'нужно проверять на телефоне. Зона не заменяет системную полоску «Домой».',
        'ctsv_links': 'Подробные инструкции, описание фоновой работы, приватности и проверок доступны в '
                      'репозитории. CTSV не связан с Google или производителями телефонов.',
        'alol_title': 'ALOL 1.0.0 — Arizona RP и Родина RP на Linux · MD3E',
        'alol_description': 'Первый стабильный ALOL: Arizona RP и Родина RP на Linux, интерфейс Material 3 '
                            'Expressive (MD3E), светлая/тёмная тема, Wine/Proton, моды, журнал и обновления.',
        'alol_heading': 'ALOL 1.0.0. Две игры. Один лаунчер.',
        'alol_intro': 'Первый стабильный релиз объединяет Arizona RP и Родину RP на Linux. Интерфейс '
                      'Material 3 Expressive помогает быстро выбрать сервер, настроить игру, установить моды '
                      'и разобраться с ошибками.',
        'alol_alt': 'ALOL 1.0.0 с интерфейсом Material 3 Expressive: переключатель Arizona RP и Родины RP, '
                    'сервер и запуск игры',
        'alol_requirement': 'Для Linux x86_64. Игра и Windows-компоненты в пакет не входят. Нужны '
                            'официальный установщик Arizona, подходящее окружение Wine/Proton и графические '
                            'драйверы.',
        'alol_setup_heading': 'Подготовьте игровое окружение.',
        'alol_steps': ['Скачайте ALOL 1.0.0: пакет для Arch/CachyOS, Fedora 44+ или отдельный '
                       'x86_64-бинарник.',
                       'Установите по инструкции. Светлая и тёмная темы доступны в «Настройки → Лаунчер».',
                       'Выберите официальный установщик Arizona Games в ALOL, затем скачайте выбранную игру '
                       'через официальный лаунчер.',
                       'Закройте официальный лаунчер, выберите Arizona RP или Родину RP, сервер и запустите '
                       'игру. В Arizona ник сохраняется по серверам; в Родине он вводится внутри игры.'],
        'alol_features_heading': 'Новый интерфейс. Проще каждый день.',
        'alol_features': [('Arizona RP и Родина RP',
                           'Переключайте игры с отдельными серверами, настройками, каталогами модов и '
                           'восстановлением. Ники Arizona сохраняются по серверам; ник Родины вводится в '
                           'игре.'),
                          ('Material 3 Expressive',
                           'Google Sans, светлая/тёмная тема, адаптивная навигация и короткие разделы '
                           'настроек. Переключатели сохраняются сразу, Ctrl+Enter запускает игру.'),
                          ('Моды с откатом',
                           'Каталог, установленные моды и добавление архива — отдельно. Проверяйте файлы и '
                           'зависимости до установки, включайте, отключайте и удаляйте моды с '
                           'восстановлением файлов.'),
                          ('Понятный журнал',
                           'Ищите записи, фильтруйте ошибки, ставьте просмотр на паузу, следите за новыми '
                           'строками, копируйте видимое и очищайте журнал с архивом.'),
                          ('Wine, Proton и обслуживание',
                           'Подготовка шрифтов и компонентов, русская локаль только для игры, исправление '
                           'типичных проблем с резервными копиями и обновления ALOL.')],
        'alol_limits_heading': 'Сначала проверьте требования.',
        'alol_limits': 'Опубликованные пакеты предназначены для Linux x86_64; есть инструкции для '
                       'Arch/CachyOS и Fedora 44+. Совместимость зависит от рантайма и драйверов. ALOL '
                       'независим от Arizona Games и не содержит игру.',
        'alol_license': 'Код ALOL 1.0.0 — Apache-2.0. Google Sans — OFL-1.1, дополнительный патч Wine — '
                        'LGPL-2.1-or-later с полными изменёнными исходниками. Старые теги сохраняют свои '
                        'лицензии.',
        'alol_demo': 'Скриншот сделан с демонстрационным профилем: он показывает интерфейс, а не '
                     'подтверждение живой игровой сессии.',
        'alol_community': 'Новости и обновления проекта — @alolinux в Telegram.',
        'feedback': 'Есть вопрос или ошибка?',
        'feedback_text': 'Сначала проверьте инструкцию, затем опишите свои действия и результат. Подробные '
                         'сообщения помогают улучшать проект.'}}

def route(lang,project=''):
 return ('/ru/' if lang=='ru' else '/')+(project+'/' if project else '')


# Material 3 Expressive presentation; existing bilingual product copy remains above.
UI={
'en':{'home':'Home','appearance':'Appearance','appearance_help':'Make this space yours. Your choices stay in this browser.','theme':'Theme','auto':'System','light':'Light','dark':'Dark','colors':'Accent color','lavender':'Lavender','mint':'Mint','sky':'Sky','rose':'Rose','close':'Close appearance settings','hero':'Android.<br>Linux.<br><span>More you.</span>','eyebrow':'Independent projects by Velmi1337','hello':'Hi, I’m','creator':'Vibe-code developer. Making little tools for everyday possibilities.','profile':'Expressive profile','project_eyebrow':'Made to be used','project_count':'Two platforms. Two open-source projects.','footer_cta':'Try a project.<br>Make it better.','footer_text':'A device report, a reproducible bug, a useful idea. Open source gets better together.','feedback':'Find a project','design':'Design & credits','setup':'Getting started','learn_more':'Explore project'},
'ru':{'home':'Главная','appearance':'Оформление','appearance_help':'Настройте сайт под себя. Выбор сохраняется только в этом браузере.','theme':'Тема','auto':'Системная','light':'Светлая','dark':'Тёмная','colors':'Акцентный цвет','lavender':'Лаванда','mint':'Мята','sky':'Небо','rose':'Роза','close':'Закрыть настройки оформления','hero':'Android.<br>Linux.<br><span>По-твоему.</span>','eyebrow':'Независимые проекты Velmi1337','hello':'Привет, я','creator':'Вайбкод-разработчик. Делаю небольшие инструменты для повседневных задач.','profile':'Expressive-профиль','project_eyebrow':'Чтобы пользоваться','project_count':'Две платформы. Два открытых проекта.','footer_cta':'Попробуйте.<br>Помогите улучшить.','footer_text':'Проверка на устройстве, понятный баг, полезная идея. Открытые проекты становятся лучше вместе.','feedback':'Выбрать проект','design':'Дизайн и авторство','setup':'Первый запуск','learn_more':'О проекте'},
}

def icon(name):
 return f'<svg class="icon" aria-hidden="true" focusable="false"><use href="/assets/icons.svg#{name}"></use></svg>'

def bloom(cx=120,cy=120,radius=112,petals=12,depth=.06):
 import math
 return 'M'+' L'.join(f'{cx+radius*(1-depth+depth*math.cos(petals*2*math.pi*n/180))*math.cos(2*math.pi*n/180-math.pi/2):.2f} {cy+radius*(1-depth+depth*math.cos(petals*2*math.pi*n/180))*math.sin(2*math.pi*n/180-math.pi/2):.2f}' for n in range(180))+' Z'

def shape_decoration():
 return f'<svg class="shape-decoration" viewBox="0 0 240 240" aria-hidden="true"><path d="{bloom(petals=8,depth=.12)}"/></svg>'

def avatar(lang):
 return f'<svg class="avatar-bloom" viewBox="0 0 240 240" role="img" aria-label="GitHub avatar: Velmi1337"><defs><clipPath id="avatar-clip"><path d="{bloom()}"/></clipPath></defs><path d="{bloom(radius=119)}" fill="var(--md-sys-color-primary)"/><image href="/assets/avatar.png" x="8" y="8" width="224" height="224" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip)"/></svg>'

def head(lang,project=''):
 c=COPY[lang];u=UI[lang];url=BASE+route(lang,project);title=c[project+'_title'] if project else c['title'];desc=c[project+'_description'] if project else c['description']
 image=BASE+'/assets/social.png'
 alternates=''.join(f'<link rel="alternate" hreflang="{lng}" href="{BASE+route(lng,project)}">' for lng in ['en','ru'])+f'<link rel="alternate" hreflang="x-default" href="{BASE+route("en",project)}">'
 if project:
  schema={'@context':'https://schema.org','@type':'SoftwareApplication','name':project.upper(),'url':url,'description':desc,'operatingSystem':'Android' if project=='ctsv' else 'Linux','applicationCategory':'UtilitiesApplication' if project=='ctsv' else 'GameApplication',**({'softwareVersion':'1.0.0'} if project=='alol' else {}), 'downloadUrl':GH+'/'+project.upper()+'/releases/latest','isAccessibleForFree':True,'author':{'@type':'Person','name':'Velmi1337','url':GH},'license':GH+'/'+project.upper()+'/blob/main/LICENSE'}
 else:schema={'@context':'https://schema.org','@type':'WebSite','name':'Velmi1337 projects','url':url,'inLanguage':lang,'description':desc}
 boot='''(()=>{try{const m=localStorage.getItem('velmi-md3-mode'),p=localStorage.getItem('velmi-md3-palette');document.documentElement.dataset.mode=['light','dark','auto'].includes(m)?m:'auto';document.documentElement.dataset.palette=['lavender','mint','sky','rose'].includes(p)?p:'lavender'}catch{}})();'''
 html=f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(title)}</title><script>{boot}</script>
<meta name="description" content="{e(desc,quote=True)}"><meta name="robots" content="index,follow"><meta name="theme-color" content="#65558f"><link rel="canonical" href="{url}">{alternates}
<meta property="og:type" content="website"><meta property="og:site_name" content="Velmi1337"><meta property="og:title" content="{e(title,quote=True)}"><meta property="og:description" content="{e(desc,quote=True)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{image}"><meta property="og:locale" content="{'ru_RU' if lang=='ru' else 'en_US'}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title,quote=True)}"><meta name="twitter:description" content="{e(desc,quote=True)}"><meta name="twitter:image" content="{image}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="/assets/fonts/GoogleSansFlex-subset.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/assets/tokens.css"><link rel="stylesheet" href="/assets/style.css"><script src="/assets/site.js" defer></script><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head><body><a class="skip" href="#main">{c['skip']}</a><aside class="rail"><a class="rail-mark state-layer" href="{route(lang)}" aria-label="Velmi1337 — {u['home']}">V.</a><nav aria-label="{'Main navigation' if lang=='en' else 'Основная навигация'}">'''
 for key,label,glyph in [('',u['home'],'home'),('ctsv','CTSV','android'),('alol','ALOL','computer')]:
  current=' aria-current="page"' if key==project else ''
  html+=f'<a class="rail-item" href="{route(lang,key)}"{current}><span class="nav-indicator state-layer">{icon(glyph)}</span><span>{label}</span></a>'
 html+=f'''</nav><a class="rail-bottom icon-button state-layer" href="{GH}" aria-label="GitHub">{icon('code')}</a></aside><div class="site"><div class="wrap"><header class="top"><a class="brand" href="{route(lang)}"><span class="brand-dot" aria-hidden="true"></span>Velmi1337</a><div class="top-actions"><a class="language state-layer" lang="{'ru' if lang=='en' else 'en'}" hreflang="{'ru' if lang=='en' else 'en'}" href="{route('ru' if lang=='en' else 'en',project)}">{icon('language')}{c['lang']}</a><button class="icon-button state-layer" type="button" data-js data-open-appearance aria-label="{u['appearance']}" title="{u['appearance']}">{icon('palette')}</button></div></header>'''
 return html

def appearance(lang):
 u=UI[lang]
 modes=''.join(f'<button class="state-layer" type="button" data-set-mode="{name}" aria-pressed="false">{icon(glyph)}<span>{u[label]}</span></button>' for name,label,glyph in [('auto','auto','settings_brightness'),('light','light','light_mode'),('dark','dark','dark_mode')])
 seeds={'lavender':'#6750A4','mint':'#006C4C','sky':'#00639B','rose':'#984061'}
 colors=''.join(f'<button type="button" data-set-palette="{key}" aria-label="{u[key]}" title="{u[key]}" aria-pressed="false" style="--swatch:{value}">{icon("check")}</button>' for key,value in seeds.items())
 return f'''<dialog id="appearance" aria-labelledby="appearance-title"><div class="dialog-top"><h2 id="appearance-title">{u['appearance']}</h2><button class="icon-button state-layer" type="button" data-close-appearance aria-label="{u['close']}">{icon('close')}</button></div><fieldset><legend>{u['theme']}</legend><div class="segmented">{modes}</div></fieldset><fieldset><legend>{u['colors']}</legend><div class="swatches">{colors}</div></fieldset><p class="dialog-help">{u['appearance_help']}</p></dialog>'''

def foot(lang):
 c=COPY[lang];u=UI[lang]
 return f'''<footer class="footer"><span>{c['footer']}</span><div class="footer-links"><a href="{GH}">GitHub</a><a href="{GH}/velmi1337.github.io/blob/main/docs/design.md">{u['design']}</a><a href="{GH}/velmi1337.github.io">{c['site_source']}</a></div></footer></div></div>{appearance(lang)}</body></html>'''

def btn(url,text,secondary=False,glyph='arrow_outward',large=False):
 return f'<a class="button state-layer{" secondary" if secondary else ""}{" large" if large else ""}" href="{url}">{icon(glyph)}<span>{e(text)}</span></a>'

def screenshot(lang,project):
 c=COPY[lang];src='ctsv-'+lang+'.png' if project=='ctsv' else 'alol.png?v=1.0.0';kind='phone' if project=='ctsv' else 'desktop';w,h=(1080,1920) if project=='ctsv' else (960,740)
 return f'<div class="shot {kind}">{shape_decoration()}<img src="/assets/{src}" alt="{e(c[project+"_alt"],quote=True)}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>'
def paragraph(text):return '<p>'+e(text)+'</p>'
def documentation(lang,project):return GH+'/'+project.upper()+'/blob/main/'+('README_ru.md' if project=='ctsv' and lang=='ru' else 'README_EN.md' if project=='alol' and lang=='en' else 'README.md')
def numbered_steps(items):return '<ol class="start-list">'+''.join('<li><span class="step-number" aria-hidden="true"></span><div>'+e(step)+'</div></li>' for step in items)+'</ol>'

def home(lang):
 c=COPY[lang];u=UI[lang]
 html=head(lang)+f'''<main id="main"><section class="hero"><div><div class="eyebrow">{icon('code')}{u['eyebrow']}</div><h1>{u['hero']}</h1><p class="lead">{c['lead']}</p><div class="actions">{btn('#projects',c['explore'],glyph='apps',large=True)}{btn(GH,c['github'],True,glyph='code',large=True)}</div></div><div class="hero-art"><div class="identity-card">{avatar(lang)}<div class="identity-copy"><span>{u['hello']}</span><br><strong>Velmi1337</strong><p>{u['creator']}</p><a class="mini-link" href="{GH}">{u['profile']}{icon('arrow_outward')}</a></div></div><a class="hero-tile state-layer" href="{route(lang,'ctsv')}"><span class="tile-icon">{icon('search')}{icon('arrow_outward')}</span><strong>CTSV</strong><small>Android · Circle to Search</small></a><a class="hero-tile state-layer" href="{route(lang,'alol')}"><span class="tile-icon">{icon('terminal')}{icon('arrow_outward')}</span><strong>ALOL</strong><small>Linux · Arizona RP + Rodina RP</small></a></div></section><section id="projects"><div class="section-title reveal"><div><div class="eyebrow">{icon('favorite')}{u['project_eyebrow']}</div><h2>{c['projects_title']}</h2></div><p class="small">{u['project_count']}</p></div>'''
 for project in ['ctsv','alol']:
  glyph='search' if project=='ctsv' else 'terminal'
  html+=f'''<article class="project {project} reveal"><div class="project-copy"><div class="project-top"><span class="app-icon">{icon(glyph)}</span><div><div class="project-name">{project.upper()}</div><span class="small">{c[project+'_platform']}</span></div></div><h2>{c[project+'_summary']}</h2><p class="lead">{c[project+'_text']}</p><div class="tags">{''.join('<span>'+e(tag)+'</span>' for tag in c[project+'_tags'])}</div><div class="actions">{btn(route(lang,project),u['learn_more'],glyph='arrow_forward')}{btn(GH+'/'+project.upper()+'/releases/latest',c['download'],True,glyph='download')}</div></div>{screenshot(lang,project)}</article>'''
 steps=''.join('<li><span class="step-number" aria-hidden="true"></span><div><strong>'+e(title)+'</strong><p>'+e(text)+'</p></div></li>' for title,text in c['start_steps'])
 html+=f'''</section><section class="start-section reveal"><div><div class="eyebrow">{icon('touch_app')}{u['setup']}</div><h2>{c['start_title']}</h2></div><ol class="start-list">{steps}</ol></section><section class="closing reveal"><div><h2>{u['footer_cta']}</h2><p>{u['footer_text']}</p></div><div class="actions">{btn('#projects',u['feedback'],glyph='arrow_forward')}</div></section></main>'''+foot(lang)
 return html

def detail(lang,project):
 c=COPY[lang];u=UI[lang];repo=GH+'/'+project.upper();glyph='android' if project=='ctsv' else 'computer'
 html=head(lang,project)+f'''<main id="main"><div class="breadcrumb"><a href="{route(lang)}">{c['back']}</a>{icon('arrow_forward')}<span>{project.upper()}</span></div><section class="detail-hero"><div><div class="eyebrow">{icon(glyph)}{c[project+'_platform']}</div><h1>{c[project+'_heading']}</h1><p class="lead">{c[project+'_intro']}</p><div class="actions">{btn(repo+'/releases/latest',('Скачать 1.0.0' if lang=='ru' else 'Download 1.0.0') if project=='alol' else c['download'],glyph='download',large=True)}{btn(repo,c['code'],True,glyph='code')}</div><p class="small">{c[project+'_requirement']}</p></div>{screenshot(lang,project)}</section><section class="article columns reveal"><div><div class="eyebrow">{icon('touch_app')}{u['setup']}</div><h2>{c[project+'_setup_heading']}</h2></div><div>{numbered_steps(c[project+'_steps'])}{btn(documentation(lang,project),c['docs'],True,glyph='arrow_forward')}</div></section>'''
 if project=='ctsv':
  html+=f'''<section class="article reveal"><h2>{c['triggers_heading']}</h2><div class="table-wrap"><table><thead><tr>{''.join('<th scope="col">'+e(h)+'</th>' for h in c['trigger_headers'])}</tr></thead><tbody>{''.join('<tr>'+''.join('<td>'+e(cell)+'</td>' for cell in row)+'</tr>' for row in c['trigger_rows'])}</tbody></table></div></section><section class="article columns reveal"><h2>{c['ctsv_tuning_heading']}</h2><div class="feature-list">{''.join('<div class="feature-row">'+paragraph(p)+'</div>' for p in c['ctsv_tuning'])}</div></section><section class="article columns reveal"><h2>{c['ctsv_limits_heading']}</h2><div>{paragraph(c['ctsv_limits'])}<div class="notice">{icon('info')}{paragraph(c['ctsv_links'])}</div></div></section>'''
 else:
  html+=f'''<section class="article columns reveal"><h2>{c['alol_features_heading']}</h2><div class="feature-list">{''.join('<div class="feature-row"><h3>'+e(title)+'</h3>'+paragraph(text)+'</div>' for title,text in c['alol_features'])}</div></section><section class="article columns reveal"><h2>{c['alol_limits_heading']}</h2><div>{paragraph(c['alol_limits'])}<div class="notice">{icon('info')}{paragraph(c['alol_license'])}</div><p class="small">{e(c['alol_demo'])}</p><p><a href="https://t.me/alolinux">{c['alol_community']}</a></p></div></section>'''
 html+=f'''<section class="closing reveal"><div><h2>{c['feedback']}</h2><p>{c['feedback_text']}</p></div><div class="actions">{btn(repo+'/issues',c['issues'],glyph='forum')}</div></section></main>'''+foot(lang)
 return html

if __name__=='__main__':
 for lang in ['en','ru']:
  for project in ['','ctsv','alol']:
   path=ROOT/route(lang,project).lstrip('/')/'index.html';path.parent.mkdir(parents=True,exist_ok=True)
   path.write_text(home(lang) if not project else detail(lang,project))
 urls=[BASE+route(lang,project) for lang in ['en','ru'] for project in ['','ctsv','alol']]
 (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+url+'</loc></url>\n' for url in urls)+'</urlset>\n')
 (ROOT/'sitemap.txt').write_text('\n'.join(urls)+'\n', encoding='utf-8')
 (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+BASE+'/sitemap.xml\nSitemap: '+BASE+'/sitemap.txt\n', encoding='utf-8')
 (ROOT/'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="16" fill="#e9ddff"/><path d="M12 13 24 36 36 13" fill="none" stroke="#65558f" stroke-width="5" stroke-linejoin="round"/></svg>')
 (ROOT/'404.html').write_text(head('en').replace('name="robots" content="index,follow"','name="robots" content="noindex,follow"')+'<main id="main" class="not-found"><div class="eyebrow">404</div><h1>Page not found.<br>Страница не найдена.</h1><div class="actions">'+btn('/','Projects')+btn('/ru/','Проекты',True)+'</div></main>'+foot('en'))
 print('Generated six bilingual Material 3 Expressive pages and 404')
