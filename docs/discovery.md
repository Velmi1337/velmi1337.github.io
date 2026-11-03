# Search discovery and first users / Поиск и первые пользователи

## English

### Google Search Console — requires the maintainer's Google account

1. Open https://search.google.com/search-console/ and add a **URL prefix** property for `https://velmi1337.github.io/`.
2. Choose the HTML-file or HTML-tag verification method. Download the file or copy the exact tag Google provides.
3. Publish that file at the site root, or add the provided tag to the generator's `<head>` and regenerate all pages. Never invent a verification code.
4. Verify ownership in Search Console.
5. Submit `https://velmi1337.github.io/sitemap.xml` in Sitemaps.
6. Inspect the home/project URLs and request indexing for a small number of important pages.

Search Console ownership cannot be completed just by creating a GitHub repository. It requires the actual verification token from the owner's Google session.
Do not share your password or session cookies. The public verification file/tag is sufficient for publishing it on the site.

Google describes crawling as taking days to weeks and does not guarantee indexing:
https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
Repeated requests do not make the process faster. A sitemap is a discovery aid, not a ranking guarantee.

### Two-week launch checklist

- Record a real 20–40 second CTSV demo on a phone with available Google CTS, including closing search and returning to the original app.
- Record an actual ALOL game-launch session on Linux, naming the distribution, runtime and driver setup.
- Use the bilingual announcement drafts in each project's `docs/promotion/ANNOUNCEMENTS.md`.
- Post manually only in communities whose rules allow such project announcements. State that you are the author; include requirements, limitations and a useful demonstration.
- Ask for reproducible device/distro reports instead of empty stars. Fix reported issues and update compatibility information based on actual tests.
- Review GitHub Insights → Traffic after a week. Visitor/clone data updates hourly and covers the latest 14 days; download counters are not active-user counts.

The initial goal is useful feedback and verified installs, not a promised number of views or rankings.
No community posts or external messages are sent by this repository.

## Русский

### Google Search Console — нужен Google-аккаунт владельца

1. Откройте https://search.google.com/search-console/ и добавьте ресурс **с префиксом URL**: `https://velmi1337.github.io/`.
2. Выберите подтверждение HTML-файлом или HTML-тегом. Скачайте файл или скопируйте точный тег из Google.
3. Разместите файл в корне сайта либо добавьте предоставленный тег в `<head>` генератора и пересоздайте страницы. Придумывать код подтверждения нельзя.
4. Подтвердите владение в Search Console.
5. В разделе Sitemap отправьте `https://velmi1337.github.io/sitemap.xml`.
6. Проверьте главную/страницы проектов и запросите индексацию нескольких важных адресов.

Создания репозитория недостаточно для подтверждения Search Console: нужен код из Google-сессии владельца.
Пароль и cookies передавать не нужно. Для размещения на сайте достаточно публичного файла/тега подтверждения.

Google указывает срок обхода от дней до недель и не гарантирует индексацию:
https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
Повторение запросов не ускоряет процесс. Sitemap помогает обнаружить страницы, но не гарантирует позиции.

### План на две недели

- Снимите реальный ролик CTSV на 20–40 секунд на телефоне с доступным CTS: запуск, поиск, закрытие и возврат в исходное приложение.
- Снимите настоящий запуск игры через ALOL на Linux с указанием дистрибутива, рантайма и драйверов.
- Возьмите русские/английские черновики из `docs/promotion/ANNOUNCEMENTS.md` каждого проекта.
- Размещайте вручную только там, где правила разрешают анонсы своих проектов. Укажите авторство, требования, ограничения и покажите работу.
- Просите воспроизводимые отчёты, а не пустые звёзды. Исправляйте ошибки и пополняйте сведения о совместимости реальными проверками.
- Через неделю проверьте GitHub Insights → Traffic. Посещения/клонирования обновляются ежечасно и показывают последние 14 дней; скачивания не равны активным пользователям.

Первый ориентир — полезные отзывы и подтверждённые установки. Число просмотров и позиции в поиске не обещаются.
Сообщения в сообщества и сторонним людям автоматически не отправляются.
