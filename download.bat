@echo off
echo 正在从 GitHub 下载更新...
cd /d "C:\github\first-python-project"
git pull origin main
echo 下载完成!
pause