@echo off
echo Backup using Git
"c:\program files\git\bin\sh.exe" --login -i -c "git status"
rem @echo use git add <file>
rem @echo use git commit -m
echo use "git push origin master" for remote GitHub repo
"c:\program files\git\bin\sh.exe" --login -i 
