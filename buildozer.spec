[app]
title = CrypterAES
package.name = crypteraes
package.domain = org.example
version = 1.0.0
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy,openssl,cryptography
icon.filename = %(source.dir)s/CryptAES.jpg
orientation = portrait
fullscreen = 0

# --- Android configuration ---
p4a.bootstrap = sdl2
android.archs = arm64-v8a,armeabi-v7a
android.api = 33
android.minapi = 23
android.ndk = 25b
android.ndk_path = /home/test/.buildozer/android/platform/android-ndk-r25b
android.sdk_path = /home/test/.buildozer/android/platform/android-sdk
android.private_storage = True
android.copy_libs = True
android.ndk_api = 23
android.entrypoint = org.kivy.android.PythonActivity
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
debug = 1
use_venv = True
logcat = True
android.build_tools_version = 33.0.2

# --- critical dependency linkers ---
android.add_libs_armeabi_v7a = libpthread.so
android.add_libs_arm64_v8a = libpthread.so
