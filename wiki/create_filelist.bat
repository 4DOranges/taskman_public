@echo off
chcp 65001
setlocal enableextensions enabledelayedexpansion
set concat=
for %%x in (%*) do set concat=!concat! %%x
set concat=%concat:~1%
copy /Y "new_pages\%concat%.txt" iofile.txt 