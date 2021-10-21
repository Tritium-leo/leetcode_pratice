# Leetcode Personal Practice
+ 语言：Python3
+ 背景：此项目用于个人力扣的练习,可提供他人参考借鉴
+ 安装方式
    + pip install -r requirements.txt
+ 目录介绍:
    + _doing_job :未完成的题目
    + core ：核心
    + done_job：已完成的题目
    + tidy_job：整理后的已完成的目录
    + temp： 临时目录（日志等）
    + main.py : 提供 文件整理功能 即(tidy_job的整理)
  
+ 开始一个新任务
  + 在doing_job创建一个新文件 满足正则 xxx\d+.py EXP:[test_123.py]
  + 文件内部写入 任务的难度 # difficulty = ENUM[hard,middle,simple] EXP:[# difficulty = simple]
  + 完成后放入 done_job
  + 完全完成后 放入 warehouse_job
  + 执行 main.py
  + main.py 会去整理warehouse_job内部的任务