[app]
title = My Messenger
package.name = mymessenger
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Список библиотек. Добавил certifi для работы Firebase через HTTPS
requirements = python3,kivy==2.3.0,kivymd,pillow,requests,urllib3,certifi

orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
# Фиксируем стабильную версию NDK, чтобы не было ошибок распаковки
android.ndk = 23b
android.ndk_path = 
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
