[app]
# Название твоего мессенджера
title = SQUARI
# Название пакета (без пробелов)
package.name = mymessenger
# Твое имя или ник
package.domain = org.test

# Исходники (все файлы .py и .kv в папке)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# ВАЖНО: Перечисли здесь библиотеки из твоего requirements.txt через запятую
# Я добавил стандартные для Kivy + requests для сети
requirements = python3,kivy==2.3.0,kivymd,pillow

# Ориентация экрана
orientation = portrait

# (bool) Оставлять ли экран включенным (полезно для мессенджера)
android.wakelock = True

# Разрешения для Android (Интернет обязателен для мессенджера)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Архитектура (для современных телефонов лучше оставить arm64-v8a)
android.archs = arm64-v8a

[buildozer]
# Уровень логирования (2 — чтобы видеть ошибки, если сборка упадет)
log_level = 2
warn_on_root = 1
