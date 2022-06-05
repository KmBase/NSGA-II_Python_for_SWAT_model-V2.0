 @echo off

echo "É¾³ýNSGA2.OUT\"
rmdir /s/q TxtInOut\NSGA2.OUT
pause

echo "¸´ÖÆInµ½Default\TxtInOut\"
xcopy TxtInOut\Backup\*.* TxtInOut\/s /e /c /y /h /r /q
pause

:: required

python run.py

pause