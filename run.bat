 @echo off

echo "ɾ��NSGA2.OUT\"
rmdir /s/q TxtInOut\NSGA2.OUT
pause

echo "����In��Default\TxtInOut\"
xcopy TxtInOut\Backup\*.* TxtInOut\/s /e /c /y /h /r /q
pause

:: required

python run.py

pause