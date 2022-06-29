#pip3 install --upgrade python-gitlab
#pip3 install git+https://gitlab.com/python-gitlab/python-gitlab.git
#pip3 install requests"

#!/usr/bin/python3.8

import os
import sys
import traceback

import gitlab
import requests

url="https://gitlab-digital.tele2.kz"
private_token="jinYi2p3oeNixWHXAu7L"


#Укакзать надо путь до группы в котором хочешь создать проект и имя апроекта
group_path="devops/projects/tele2/huaweicloud/test/panfilova"
project_name="askar-test-123"


#Аутентификация в гитлабе
try:
    gl = gitlab.Gitlab(url, private_token)
    print("Success authentication in the Gitlab")
except:
    print("Attention!, can not authenticate in the Gitlab")


# to create project in the group
try:
    group_id = gl.groups.list(search=str(group_path))[0].id
    project = gl.projects.create({'name': str(project_name), 'namespace_id': group_id, "initialize_with_readme": "true"})
    print("Success to create repository")
except:
    print("We have some problem with create repo")