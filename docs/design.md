# Material 3 Expressive / Материальный выразительный дизайн

The website uses HTML, CSS and small progressive JavaScript enhancements inspired by Google's Material 3 Expressive. It is a web implementation, not the Android Compose component library or an imported Figma document.

## Design references

- [Material 3](https://m3.material.io/)
- [Color roles](https://m3.material.io/styles/color/roles)
- [Motion specifications](https://m3.material.io/styles/motion/overview/specs)
- [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3)
- [Official design kit](https://www.figma.com/community/file/1035203688168086460/material-3-design-kit)

Four seed colors are converted into light/dark tonal palettes by Google's `@material/material-color-utilities` using `SchemeTonalSpot`. The interface uses semantic surface/container/on-color roles, expressive rounded shapes, connected controls, large variable typography and the documented expressive spatial/effects easing curves. Desktop navigation becomes bottom navigation on small screens.

Appearance preferences stay in localStorage on the device. There is no analytics, polling, remote font request or runtime GitHub API request. Core content and navigation work without JavaScript. Reveal animations run once; reduced-motion preferences disable movement. Modal controls use native dialog semantics and keyboard dismissal.

## Sources and licenses

- Website code and copy: GPL-3.0-only, root `LICENSE`.
- Google Sans Flex and Roboto Flex are self-hosted, obtained from [expressive-profile](https://github.com/metawka/expressive-profile). Their exact OFL notices are in `assets/fonts/`.
- Cookie/flower shape inspiration: expressive-profile, MIT, see `LICENSES/MIT-Expressive-Profile.txt`.
- Rounded Material Symbols: Google, Apache-2.0, see `LICENSES/Apache-2.0.txt`. Sprite paths come from `@material-symbols/svg-400` 0.48.2.
- Avatar: the author's existing public GitHub avatar. Product screenshots and ALOL notices retain their original attribution, described in the README.
- Build dependencies retain their upstream license notices in the distributed npm packages. Dependencies are used at build time only.

## Verification

All six routes were checked in Chromium at 1440, 1024, 768, 390 and 360 CSS pixels. Checks cover responsive overflow, canonical URLs, current navigation, theme/color persistence, language switching, reduced motion and content with JavaScript disabled. Browser checks do not replace testing with every assistive technology or device.

## Русский

Сайт полностью переработан по принципам Material 3 Expressive: смысловые роли цвета, четыре палитры со светлой и тёмной темой, выразительные формы, крупная типографика, адаптивная навигация и анимации по спецификации Google. Для веба используются HTML/CSS; Android Compose и файл Figma не встроены в сайт.

Текст и ссылки работают без JavaScript. Скрипт добавляет выбор оформления и короткие анимации. Настройки сохраняются только в браузере; аналитики, фонового опроса и внешней загрузки шрифтов нет. При включённом уменьшении движения анимации отключаются.

Ссылки на официальные материалы и лицензии всех заимствованных ресурсов приведены выше. Проверены шесть страниц на пяти размерах экрана, смена языка и оформления, сохранение настроек и работа без JavaScript.
