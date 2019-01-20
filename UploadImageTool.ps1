for ($i=1; $i -le 3; $i++) {$i,"`n"}

for ($i=1; $i -le 3; $i++) {$i,"`n"  
#start-process GenerateDownLoadImageRequest.py $i
#start-process DownloadImage.py
#start-process FromWorkComputer3.py $i
start-process FromWorkComputer3.py 1
start-process executeFile.py
}