[app]
title = Cắm Câu Cá Lóc
package.name = fishinggame
package.domain = com.vn
version = 1.0
source.dir = .
source.include_exts = py,png,jpg,jpeg,json,txt

requirements = python3,pygame==2.5.2

orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

presplash.filename = presplash.png
icon.filename = icon.png

build_type = debug

[buildozer]
log_level = 2
