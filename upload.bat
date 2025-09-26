@echo off
echo 正在上传更改到 GitHub...
cd /d "C:\github\first-python-project"
git add .
git commit -m "自动提交: %date% %time%"
git push origin main
echo 上传完成!
pause