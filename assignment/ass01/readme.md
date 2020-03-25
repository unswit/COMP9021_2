# 说明

当前脚本只支持Mac和学校的CSE机房环境    

执行方式：

    # 说明
    # dengdeng_comp9021_ass01_test 为可执行的脚本文件
    # roman_arabic.py 你自己编写的py文件
    # commands_and_expected_outputs.txt 给定的txt测试文件
    ./dengdeng_comp9021_ass01_test roman_arabic.py commands_and_expected_outputs.txt
    
提示没有权限的问题

    # 执行赋权限的命令
    chmod 777 dengdeng_comp9021_ass01_test
    
上传脚本文件到学校的CSE机房环境
    
    Windows及Mac的用户可以采用自己给自己发送邮件的方式，通过远程Vlab的方式下载邮件里面的脚本并测试执行
    
    Mac或者Linux的用户，也可以采用下面的脚本来执行上传
    scp dengdeng_comp9021_ass01_test roman_arabic.py commands_and_expected_outputs.txt yourzid@cse.unsw.edu.au:~/Documents
    其中：yourid 换成你自己的zid
    输入密码以后，在你的CSE机房环境的Documents会看到相应的文件，执行一开始的测试即可