[app]
title = My Messenger
package.name = mymessenger
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# ВОТ ЭТА СТРОКА ДОЛЖНА БЫТЬ ТАКОЙ (БЕЗ РЕШЕТКИ В НАЧАЛЕ)
version = 0.1

requirements = python3,kivy==2.3.0,kivymd,pillow,requests

orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
