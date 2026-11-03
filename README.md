# Velmi1337 projects — CTSV and ALOL

**Public site:** https://velmi1337.github.io/

Static English/Russian pages for two existing projects:

- [CTSV](https://github.com/Velmi1337/CTSV): a root-free Circle to Search launcher for Android.
- [ALOL](https://github.com/Velmi1337/ALOL): an Arizona RP launcher for Linux x86_64.

## Structure

| English | Русский |
| --- | --- |
| `/` | `/ru/` |
| `/ctsv/` | `/ru/ctsv/` |
| `/alol/` | `/ru/alol/` |

Core content is rendered in HTML, without client-side JavaScript, external fonts, tracking or analytics.
Each language/page has its own title, description, canonical address, language alternates and social metadata.
The sitemap lists all six pages. Structured data describes the actual apps without invented ratings or download counts.

## Update and preview

```bash
python3 tools/build_site.py
python3 -m http.server 8765 --bind 127.0.0.1
```

Edit the bilingual copy in `tools/build_site.py`, rebuild the HTML and commit the generated files.
CSS is in `assets/style.css`. Download buttons point to the project's latest GitHub release to avoid stale binary links.
The website is published through GitHub Pages from `main` / repository root, with `.nojekyll`.

## Discovery

See [docs/discovery.md](docs/discovery.md) for the remaining Google Search Console step and a practical posting/feedback plan.
Publication makes the pages available to crawlers; indexing and search position are not guaranteed.
The root hex-named text file is a **public IndexNow ownership key**, not a private credential.
`docs/indexnow.json` holds the URL submission payload for participating search engines; Google Search Console is a separate step.

## License and assets

Website text/layout/generator: GPL-3.0-only, see [LICENSE](LICENSE).
CTSV screenshots come from the GPL-3.0-only [CTSV repository](https://github.com/Velmi1337/CTSV).
ALOL logo/screenshot come from [ALOL](https://github.com/Velmi1337/ALOL), copyright 2026 ALOL contributors, author Velmi1337.
They retain applicable Apache-2.0 notices; see [LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt)
and the preserved [ALOL NOTICE](assets/NOTICE.ALOL).
The source images are copied unchanged. Documentation/screenshots show interfaces and do not invent tested live searches or game sessions.
No endorsement by Google, phone manufacturers or Arizona Games is implied.

## Русский

Статические страницы CTSV и ALOL на русском и английском: https://velmi1337.github.io/ru/.
Для каждой страницы есть собственные заголовок, описание, canonical/hreflang и метаданные для ссылок.
Текст доступен без JavaScript. Аналитики и внешних шрифтов нет.

Для обновления отредактируйте `tools/build_site.py`, выполните генератор и отправьте изменения в `main`.
Исходные скриншоты и логотипы сохранены без изменений; лицензии и авторство перечислены выше.
Обход и индексация поисковиками не гарантируются. Следующие шаги — в [инструкции](docs/discovery.md).
