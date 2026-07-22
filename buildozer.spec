[app]

title = Мой цифровой питомец
package.name = digitalpet
package.domain = org.creativika

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt
source.exclude_dirs = tests,docs,.github,__pycache__,.venv,.git

version = 1.0.0
requirements = python3,kivy==2.3.1

icon.filename = assets/icon.png
presplash.filename = assets/presplash.png
orientation = portrait
fullscreen = 0

# Актуальные параметры Android для python-for-android v2026.05.09.
android.api = 36
android.minapi = 23
android.ndk = 29
android.archs = arm64-v8a
android.private_storage = True
android.enable_androidx = True
android.accept_sdk_license = True

# Зафиксированная стабильная версия сборщика Android.
p4a.branch = v2026.05.09

[buildozer]
log_level = 2
warn_on_root = 1
