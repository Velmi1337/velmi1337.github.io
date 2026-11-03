#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
"""Generate crawlable, script-free English/Russian project pages."""
from pathlib import Path
from html import escape as e
import json

ROOT=Path(__file__).resolve().parents[1]
BASE='https://velmi1337.github.io'
GH='https://github.com/Velmi1337'
COPY={
'en':{
 'home':'Projects','lang':'Русский','code':'Source code','download':'Download on GitHub','docs':'Read the documentation','issues':'Report a problem','back':'All projects','footer':'Independent open-source projects by Velmi1337.','site_source':'Website source','skip':'Skip to content',
 'title':'Velmi1337 — CTSV Circle to Search & ALOL Arizona RP for Linux',
 'description':'Open-source tools by Velmi1337: CTSV launches Circle to Search without root on Android; ALOL manages Arizona RP on Linux with Wine or Proton. Downloads, setup and source code.',
 'hero':'Android search.<br>Linux gaming.','lead':'Two open-source tools by Velmi1337: launch Circle to Search with CTSV, or manage Arizona RP on Linux with ALOL.','explore':'Find your project','github':'View GitHub profile','eyebrow':'Small, focused, open source','projects_title':'Choose your tool','projects_subtitle':'Source code, releases and practical setup guides.',
 'ctsv_summary':'Circle to Search without root.','ctsv_text':'Open Google’s search from a Quick Settings tile, a configurable hold zone or a shortcut. Choose English or Russian.','ctsv_explore':'Explore CTSV','ctsv_platform':'Android 9+ · no root','ctsv_tags':['Quick Settings','Hold gestures','GPL-3.0-only'],
 'alol_summary':'Arizona RP, launched on Linux.','alol_text':'A native Rust and GTK 3 launcher to manage Arizona RP through Wine or Proton, with server profiles, mods and repair tools.','alol_explore':'Explore ALOL','alol_platform':'Linux · x86_64','alol_tags':['Wine / Proton','Arch / Fedora','Open source'],
 'start_title':'Start with a release.','start_steps':[('Choose your platform','CTSV is for Android. ALOL is for Linux on x86_64.'),('Download from the project’s GitHub','Release pages contain binaries and checksums. Each project documents its own setup requirements.'),('Help make it better','Found a reproducible problem? Open an issue with the app version, device or distribution, and steps to reproduce.')],
 'ctsv_title':'CTSV — Circle to Search without root for Android',
 'ctsv_description':'CTSV is an open-source Android launcher for Google Circle to Search. Use Quick Settings, a hold zone or automation. English/Russian interface, no root, configurable shade delay.',
 'ctsv_heading':'CTSV: Circle to Search without root.',
 'ctsv_intro':'Bring Google’s screen search within reach. Start from a tile, hold and release a small zone, or map your own shortcut.',
 'ctsv_alt':'CTSV Android settings showing Quick Settings setup and a configurable launch delay',
 'ctsv_requirement':'Requires the Google app, Google as your digital assistant, and Circle to Search availability for your device/account. CTSV cannot enable a feature Google has blocked.',
 'ctsv_setup_heading':'Set up your first search.',
 'ctsv_steps':['Install the APK from the latest GitHub release. Official updates use the same signing key.','Install or update Google, choose it as your digital assistant in Android settings, then test Launch Circle to Search.','Tap Add to Quick Settings and confirm Android’s prompt. Custom/older panels may need manual tile editing.','For a hold zone, enable it and choose standard overlay or accessibility mode. Hold for the configured duration, then release after the haptic cue.'],
 'triggers_heading':'Choose how it starts.','trigger_headers':['Trigger','Required access','When to use it'],
 'trigger_rows':[['Quick Settings tile','Neither hold-zone permission','A simple trigger with the lowest background overhead.'],['Standard hold zone','Display over other apps; foreground notification','A persistent touch target without accessibility access.'],['Accessibility hold zone','Enabled accessibility service','An alternative overlay mode; no window-content reading.'],['Automation shortcut','Your automation tool / firmware support','Launch app.ctsv/.TriggerActivity from a custom action.']],
 'ctsv_tuning_heading':'Tune the gesture, not your phone.',
 'ctsv_tuning':['Hold duration, width, left/center/right position, navigation offset, opacity and haptic feedback are configurable.','If search captures the shade or a blurred screen, increase the shade launch delay. The range is 200–3000 ms; 800 ms is the default. Try 1000–1500 ms for slower panel animations.','Successful requests do not show a toast. Diagnostics stay local. CTSV has no internet permission or analytics; Google handles the actual search.'],
 'ctsv_limits_heading':'Compatibility, honestly.',
 'ctsv_limits':'Android 9+ is the declared minimum; the automated emulator checks currently use Android 15. Actual CTS availability, closing behavior and vendor background restrictions need physical-device testing. The zone is separate from the system Home handle.',
 'ctsv_links':'Read the detailed setup, battery behavior, privacy notes and test scope in the project documentation. CTSV is independent of Google and phone manufacturers.',
 'alol_title':'ALOL — Arizona RP launcher for Linux, Wine and Proton',
 'alol_description':'ALOL (Arizona Launcher On Linux) is a native Rust/GTK 3 launcher for Arizona RP on Linux x86_64. Download Arch/CachyOS or Fedora packages and read the Wine/Proton setup guide.',
 'alol_heading':'ALOL: Arizona RP on Linux.',
 'alol_intro':'Manage the Windows game environment from a native Linux launcher: choose servers, keep nicknames per server, configure mods and repair common environment problems.',
 'alol_alt':'ALOL native Linux launcher with server selection, player nickname, game launch and settings',
 'alol_requirement':'For Linux x86_64. Game files and Windows components are not bundled. You need the official Arizona installer, an appropriate Wine/Proton environment and suitable graphics drivers.',
 'alol_setup_heading':'Get a game environment ready.',
 'alol_steps':['Download the appropriate package from the latest GitHub release: Arch/CachyOS package, Fedora RPM, or the documented alternative.','Install the package using the guide. Arch-based setups need multilib and appropriate 32/64-bit graphics drivers. Fedora packages document their Wine/winetricks requirements.','Download the installer from the official Arizona site and select the .exe in ALOL. Let the official launcher download or update game files.','Close the official launcher, choose your server and nickname, then launch through ALOL.'],
 'alol_features_heading':'What the launcher manages.',
 'alol_features':[('Servers and profiles','Choose a server and keep a separate nickname for each server.'),('Wine and Proton','Configure the game environment; consult the compatibility guide for the runtime and driver requirements.'),('Mods and options','Use the documented mod tools, custom files and game graphics/memory settings.'),('Repair and updates','Repair common text/font/environment issues with backups and manage launcher updates.')],
 'alol_limits_heading':'Read the requirements first.',
 'alol_limits':'Published packages target Linux x86_64, with instructions for Arch/CachyOS and Fedora 44+. Runtime and graphics compatibility vary. The launcher is independent of Arizona Games and does not include the game.',
 'alol_license':'Current development sources are Apache-2.0. Earlier published tags and archives, including 0.5.7, retain their stated MIT license. Check the license shipped with the version you redistribute.',
 'alol_demo':'The screenshot uses the project’s demonstration profile. It shows the interface, not a claim of a verified live game session.',
 'alol_community':'Project news: @alolinux on Telegram.',
 'feedback':'Have a specific question or bug?','feedback_text':'Read the setup guide first, then describe what you tried and what happened. Useful reports help improve the project.',
},
'ru':{
 'home':'Проекты','lang':'English','code':'Исходный код','download':'Скачать на GitHub','docs':'Открыть документацию','issues':'Сообщить о проблеме','back':'Все проекты','footer':'Независимые открытые проекты Velmi1337.','site_source':'Исходники сайта','skip':'Перейти к содержимому',
 'title':'Velmi1337 — CTSV: Circle to Search без root и ALOL: Arizona RP на Linux',
 'description':'Открытые проекты Velmi1337: CTSV запускает Circle to Search без root на Android, ALOL управляет Arizona RP на Linux через Wine или Proton. Скачивание, настройка и исходники.',
 'hero':'Поиск на Android.<br>Игры на Linux.','lead':'Два открытых проекта Velmi1337: запускайте Circle to Search через CTSV или управляйте Arizona RP на Linux через ALOL.','explore':'Выбрать проект','github':'Профиль GitHub','eyebrow':'Небольшие задачи. Открытый код.','projects_title':'Выберите свой инструмент','projects_subtitle':'Исходники, релизы и инструкции по настройке.',
 'ctsv_summary':'Circle to Search без root.','ctsv_text':'Запускайте поиск Google плиткой пункта управления, настраиваемой зоной удержания или ярлыком. Интерфейс на русском и английском.','ctsv_explore':'Подробнее о CTSV','ctsv_platform':'Android 9+ · без root','ctsv_tags':['Плитка в шторке','Удержание зоны','GPL-3.0-only'],
 'alol_summary':'Arizona RP на Linux.','alol_text':'Нативный лаунчер на Rust и GTK 3 для Arizona RP через Wine или Proton: серверы, никнеймы, моды и инструменты починки.','alol_explore':'Подробнее об ALOL','alol_platform':'Linux · x86_64','alol_tags':['Wine / Proton','Arch / Fedora','Открытый код'],
 'start_title':'Начните с релиза.','start_steps':[('Выберите платформу','CTSV предназначен для Android, ALOL — для Linux x86_64.'),('Скачайте с GitHub проекта','В релизах есть файлы и контрольные суммы. Для каждого проекта описаны собственные требования к настройке.'),('Помогите улучшить проект','Нашли воспроизводимую ошибку? Укажите версию, устройство или дистрибутив и шаги воспроизведения в issue.')],
 'ctsv_title':'CTSV — Circle to Search без root для Android',
 'ctsv_description':'CTSV — открытое Android-приложение для запуска Google Circle to Search плиткой, удержанием зоны или автоматизацией. Без root, с настройкой задержки и русским/английским интерфейсом.',
 'ctsv_heading':'CTSV: Circle to Search без root.',
 'ctsv_intro':'Поиск по экрану — под рукой. Запускайте его плиткой, удержанием и отпусканием небольшой зоны или собственным ярлыком.',
 'ctsv_alt':'Настройки CTSV на Android: добавление плитки в пункт управления и задержка запуска из шторки',
 'ctsv_requirement':'Нужны приложение Google, Google в роли цифрового помощника и доступность Circle to Search для устройства/аккаунта. CTSV не снимает запреты Google.',
 'ctsv_setup_heading':'Настройте первый поиск.',
 'ctsv_steps':['Установите APK из последнего релиза GitHub. Официальные обновления используют один ключ подписи.','Установите или обновите Google, выберите его цифровым помощником в Android и проверьте кнопку запуска CTS.','Нажмите «Добавить в пункт управления» и подтвердите запрос. На старых/нестандартных панелях добавьте плитку вручную.','Для зоны включите её и выберите обычный режим либо специальные возможности. Удерживайте заданное время и отпустите палец после виброотклика.'],
 'triggers_heading':'Выберите способ запуска.','trigger_headers':['Способ','Нужный доступ','Для чего'],
 'trigger_rows':[['Плитка пункта управления','Разрешения зоны не нужны','Простой запуск с минимальной фоновой нагрузкой.'],['Обычная зона','Поверх приложений; уведомление foreground-сервиса','Постоянная область касания без специальных возможностей.'],['Зона accessibility','Включённый сервис специальных возможностей','Альтернативный режим без чтения содержимого окон.'],['Ярлык автоматизации','Поддержка вашей программы / прошивки','Запуск компонента app.ctsv/.TriggerActivity.']],
 'ctsv_tuning_heading':'Настройте жест под себя.',
 'ctsv_tuning':['Меняются время удержания, ширина, положение слева/по центру/справа, отступ от навигации, прозрачность и виброотклик.','Если в поиск попадает шторка или остаётся размытие, увеличьте задержку: диапазон 200–3000 мс, по умолчанию 800 мс. Для медленной анимации попробуйте 1000–1500 мс.','Успешный запрос не вызывает всплывающее сообщение. Диагностика хранится локально. В CTSV нет разрешения на интернет и аналитики; сам поиск выполняет Google.'],
 'ctsv_limits_heading':'Совместимость без обещаний.',
 'ctsv_limits':'Заявленная минимальная версия — Android 9. Автоматические проверки сейчас идут на Android 15. Доступность CTS, возврат после закрытия и ограничения фона прошивки нужно проверять на телефоне. Зона не заменяет системную полоску «Домой».',
 'ctsv_links':'Подробные инструкции, описание фоновой работы, приватности и проверок доступны в репозитории. CTSV не связан с Google или производителями телефонов.',
 'alol_title':'ALOL — лаунчер Arizona RP для Linux, Wine и Proton',
 'alol_description':'ALOL (Arizona Launcher On Linux) — нативный лаунчер Arizona RP на Rust/GTK 3 для Linux x86_64. Пакеты Arch/CachyOS и Fedora, настройка Wine/Proton, моды и починка.',
 'alol_heading':'ALOL: Arizona RP на Linux.',
 'alol_intro':'Управляйте окружением Windows-игры из нативного Linux-лаунчера: выбирайте серверы, сохраняйте никнеймы, настраивайте моды и исправляйте типичные проблемы окружения.',
 'alol_alt':'Нативный Linux-лаунчер ALOL: выбор сервера, никнейм, запуск игры и настройки',
 'alol_requirement':'Для Linux x86_64. Игра и Windows-компоненты в пакет не входят. Нужны официальный установщик Arizona, подходящее окружение Wine/Proton и графические драйверы.',
 'alol_setup_heading':'Подготовьте игровое окружение.',
 'alol_steps':['Скачайте подходящий файл из последнего релиза GitHub: пакет Arch/CachyOS, Fedora RPM или описанный альтернативный вариант.','Установите пакет по инструкции. Для Arch-подобных систем нужны multilib и подходящие 32/64-битные драйверы; требования Wine/winetricks для RPM описаны в документации.','Скачайте установщик с официального сайта Arizona и выберите .exe в ALOL. Загрузите или обновите игру через официальный лаунчер.','Закройте официальный лаунчер, выберите сервер и никнейм, затем запускайте игру через ALOL.'],
 'alol_features_heading':'Что берёт на себя лаунчер.',
 'alol_features':[('Серверы и профили','Выбор сервера и отдельный никнейм для каждого.'),('Wine и Proton','Настройка окружения; требования к рантайму и драйверам описаны в руководстве совместимости.'),('Моды и параметры','Инструменты модов, свои файлы и настройки графики/памяти игры.'),('Починка и обновления','Исправление типичных проблем текста, шрифтов и окружения с резервными копиями; обновления лаунчера.')],
 'alol_limits_heading':'Сначала проверьте требования.',
 'alol_limits':'Опубликованные пакеты предназначены для Linux x86_64; есть инструкции для Arch/CachyOS и Fedora 44+. Совместимость зависит от рантайма и драйверов. ALOL независим от Arizona Games и не содержит игру.',
 'alol_license':'Текущие исходники разработки используют Apache-2.0. Ранее опубликованные теги и архивы, включая 0.5.7, сохраняют указанную в них MIT-лицензию. Проверяйте лицензию распространяемой версии.',
 'alol_demo':'Скриншот сделан с демонстрационным профилем: он показывает интерфейс, а не подтверждение живой игровой сессии.',
 'alol_community':'Новости проекта: @alolinux в Telegram.',
 'feedback':'Есть вопрос или ошибка?','feedback_text':'Сначала проверьте инструкцию, затем опишите свои действия и результат. Подробные сообщения помогают улучшать проект.',
}}

def route(lang,project=''):
 return ('/ru/' if lang=='ru' else '/')+(project+'/' if project else '')

def head(lang,project=''):
 c=COPY[lang];url=BASE+route(lang,project);title=c[project+'_title'] if project else c['title'];desc=c[project+'_description'] if project else c['description']
 image=BASE+'/assets/'+('ctsv-'+lang+'.png' if project=='ctsv' else 'alol.png' if project=='alol' else 'social.png')
 alternates=''.join(f'<link rel="alternate" hreflang="{lng}" href="{BASE+route(lng,project)}">' for lng in ['en','ru'])+f'<link rel="alternate" hreflang="x-default" href="{BASE+route("en",project)}">'
 if project:
  schema={'@context':'https://schema.org','@type':'SoftwareApplication','name':project.upper(),'url':url,'description':desc,'operatingSystem':'Android' if project=='ctsv' else 'Linux','applicationCategory':'UtilitiesApplication' if project=='ctsv' else 'GameApplication','downloadUrl':GH+'/'+project.upper()+'/releases/latest','isAccessibleForFree':True,'author':{'@type':'Person','name':'Velmi1337','url':GH},'license':GH+'/'+project.upper()+'/blob/main/LICENSE'}
 else:
  schema={'@context':'https://schema.org','@type':'WebSite','name':'Velmi1337 projects','url':url,'inLanguage':lang,'description':desc}
 return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(title)}</title>
<meta name="description" content="{e(desc,quote=True)}"><meta name="robots" content="index,follow"><meta name="theme-color" content="#182b2b"><link rel="canonical" href="{url}">{alternates}
<meta property="og:type" content="website"><meta property="og:site_name" content="Velmi1337"><meta property="og:title" content="{e(title,quote=True)}"><meta property="og:description" content="{e(desc,quote=True)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{image}"><meta property="og:locale" content="{'ru_RU' if lang=='ru' else 'en_US'}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title,quote=True)}"><meta name="twitter:description" content="{e(desc,quote=True)}"><meta name="twitter:image" content="{image}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/style.css"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head><body><a class="skip" href="#main">{c['skip']}</a><div class="wrap"><header class="top"><a class="brand" href="{route(lang)}">Velmi<span>1337</span></a><nav aria-label="{'Project navigation' if lang=='en' else 'Навигация проектов'}"><a href="{route(lang,'ctsv')}">CTSV</a><a href="{route(lang,'alol')}">ALOL</a><a href="{GH}">GitHub ↗</a></nav><a class="language" lang="{'ru' if lang=='en' else 'en'}" hreflang="{'ru' if lang=='en' else 'en'}" href="{route('ru' if lang=='en' else 'en',project)}">{c['lang']}</a></header>'''

def foot(lang):
 c=COPY[lang]
 return f'''<footer class="footer"><span>{c['footer']}</span><div><a href="{GH}">GitHub</a><a href="{GH}/velmi1337.github.io">{c['site_source']}</a></div></footer></div></body></html>'''

def btn(url,text,secondary=False):return f'<a class="button{" secondary" if secondary else ""}" href="{url}">{e(text)} <span aria-hidden="true">↗</span></a>'
def screenshot(lang,project):
 c=COPY[lang];src='ctsv-'+lang+'.png' if project=='ctsv' else 'alol.png';kind='phone' if project=='ctsv' else 'desktop';w,h=(1080,1920) if project=='ctsv' else (900,843)
 return f'<div class="shot {kind}"><img src="/assets/{src}" alt="{e(c[project+"_alt"],quote=True)}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>'
def paragraph(text):return '<p>'+e(text)+'</p>'
def documentation(lang,project):return GH+'/'+project.upper()+'/blob/main/'+('README_ru.md' if project=='ctsv' and lang=='ru' else 'README_EN.md' if project=='alol' and lang=='en' else 'README.md')

def home(lang):
 c=COPY[lang]
 html=head(lang)+f'''<main id="main"><section class="hero"><div><div class="eyebrow">{c['eyebrow']}</div><h1>{c['hero']}</h1><p class="lead">{c['lead']}</p><div class="actions">{btn('#projects',c['explore'])}{btn(GH,c['github'],True)}</div></div><div class="index"><a href="{route(lang,'ctsv')}"><span class="number">01</span><div><strong>CTSV</strong><small>{c['ctsv_platform']}</small></div><span aria-hidden="true">↗</span></a><a href="{route(lang,'alol')}"><span class="number">02</span><div><strong>ALOL</strong><small>{c['alol_platform']}</small></div><span aria-hidden="true">↗</span></a></div></section><section id="projects"><div class="section-title"><h2>{c['projects_title']}</h2><span class="small">{c['projects_subtitle']}</span></div>'''
 for project in ['ctsv','alol']:
  html+=f'''<article class="project {project}"><div class="project-copy"><span class="label">{c[project+'_platform']}</span><h2>{project.upper()}<br>{c[project+'_summary']}</h2><p class="lead">{c[project+'_text']}</p><div class="tags">{''.join('<span>'+e(tag)+'</span>' for tag in c[project+'_tags'])}</div><div class="actions">{btn(route(lang,project),c[project+'_explore'])}{btn(GH+'/'+project.upper()+'/releases/latest',c['download'],True)}</div></div>{screenshot(lang,project)}</article>'''
 html+=f'''</section><section class="steps"><h2>{c['start_title']}</h2><ol>{''.join('<li><strong>'+e(title)+'</strong><p>'+e(text)+'</p></li>' for title,text in c['start_steps'])}</ol></section></main>'''+foot(lang)
 return html

def detail(lang,project):
 c=COPY[lang];repo=GH+'/'+project.upper()
 html=head(lang,project)+f'''<main id="main"><section class="detail-hero"><div><div class="breadcrumb"><a href="{route(lang)}">{c['back']}</a> / {project.upper()}</div><span class="label">{c[project+'_platform']}</span><h1 style="margin-top:24px">{c[project+'_heading']}</h1><p class="lead">{c[project+'_intro']}</p><div class="actions">{btn(repo+'/releases/latest',c['download'])}{btn(repo,c['code'],True)}</div><p class="small">{c[project+'_requirement']}</p></div>{screenshot(lang,project)}</section><section class="article columns"><h2>{c[project+'_setup_heading']}</h2><div><ol>{''.join('<li>'+e(step)+'</li>' for step in c[project+'_steps'])}</ol>{btn(documentation(lang,project),c['docs'],True)}</div></section>'''
 if project=='ctsv':
  html+=f'''<section class="article"><h2>{c['triggers_heading']}</h2><div class="table-wrap"><table><thead><tr>{''.join('<th scope="col">'+e(h)+'</th>' for h in c['trigger_headers'])}</tr></thead><tbody>{''.join('<tr>'+''.join('<td>'+e(cell)+'</td>' for cell in row)+'</tr>' for row in c['trigger_rows'])}</tbody></table></div></section><section class="article columns"><h2>{c['ctsv_tuning_heading']}</h2><div>{''.join(paragraph(p) for p in c['ctsv_tuning'])}</div></section><section class="article columns"><h2>{c['ctsv_limits_heading']}</h2><div>{paragraph(c['ctsv_limits'])}<div class="notice">{e(c['ctsv_links'])}</div></div></section>'''
 else:
  html+=f'''<section class="article columns"><h2>{c['alol_features_heading']}</h2><div>{''.join('<h3 style="margin-top:24px">'+e(title)+'</h3>'+paragraph(text) for title,text in c['alol_features'])}</div></section><section class="article columns"><h2>{c['alol_limits_heading']}</h2><div>{paragraph(c['alol_limits'])}{paragraph(c['alol_license'])}<p class="small">{e(c['alol_demo'])}</p><p><a href="https://t.me/alolinux">{c['alol_community']}</a></p></div></section>'''
 html+=f'''<section class="article columns"><h2>{c['feedback']}</h2><div>{paragraph(c['feedback_text'])}<div class="actions">{btn(repo+'/issues',c['issues'],True)}{btn(documentation(lang,project),c['docs'],True)}</div></div></section></main>'''+foot(lang)
 return html

if __name__=='__main__':
 for lang in ['en','ru']:
  for project in ['','ctsv','alol']:
   path=ROOT/route(lang,project).lstrip('/')/'index.html';path.parent.mkdir(parents=True,exist_ok=True)
   path.write_text(home(lang) if not project else detail(lang,project))
 urls=[BASE+route(lang,project) for lang in ['en','ru'] for project in ['','ctsv','alol']]
 (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+u+'</loc></url>\n' for u in urls)+'</urlset>\n')
 (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+BASE+'/sitemap.xml\n')
 (ROOT/'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="12" fill="#182b2b"/><path d="M12 12 24 36 36 12" fill="none" stroke="#a5edc5" stroke-width="5" stroke-linejoin="round"/></svg>')
 (ROOT/'404.html').write_text(head('en').replace('name="robots" content="index,follow"','name="robots" content="noindex,follow"')+'<main id="main" class="not-found"><div class="eyebrow">404</div><h1>Page not found.<br>Страница не найдена.</h1><div class="actions">'+btn('/','Projects')+btn('/ru/','Проекты',True)+'</div></main>'+foot('en'))
 print('Generated six localized pages, sitemap, robots and a 404 page')
