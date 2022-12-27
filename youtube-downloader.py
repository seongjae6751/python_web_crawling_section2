import pytube
import os
import subprocess

# 다운 받을 동영상 URL 물어보기
URL = input("다운 받을 영상의 링크를 입력하시오")
yt = pytube.YouTube(URL)
videos = yt.streams.all()

# print('videos', videos)

for i in range(len(videos)) :
    print(i, ' , ', videos[i])

cNum = int(input("다운 받을 화질은?(0~21 입력)"))

down_dir = "C:\youtube"

videos[4].download(down_dir)
newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName) 
])

print("동영상 다운로드 및 mp3 변환 완료! ")

# 1.conda create --name(-n) test python=3.6
# 2.conda info –-envs
# 3,activate, deactivate
# 4.conda update conda
# 5.conda list
# 6.pip install –ignore-installed tensorflow(simplejson)
# 7.pip uninstall tensorflow(simplejson)
# 8.conda remove –name(-n) test --all
# 9.conda clean –all(-a)