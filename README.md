# AIPrototype24
AI Prototyping 2024 Pattaratron Gonmanee
### เป้าหมายในรายวิชา
- สร้าง sever สําหรับเพิ่มและแก้ไข ข้อมูลในการใช้งาน intent ของ Google Dialogflow
- สร้าง sever ที่สามารถตอบคําถาม นอกเหนือจาก intent ที่กําหนดไว้ โดยใช้วิธีการเชื่อมต่อกับ LLM
# 02/12/2567
## Command Line พื้นฐานบน Terminal
### 1. ระบุตำแหน่งปัจจุบันที่เราอยู่ในระบบ 
```
pwd
```
### 2. list ทุกๆ file/folder ที่อยู่ใน folder ปัจจุบัน 
``` 
ls
```
```
ls -l
```
```
ls -ltr #บอกรายละเอียดไฟล์อย่างละเอียด
```
### 3. สร้าง Folder
``` 
mkdir ชื่อของโฟลเดอร์
```
### 4. Change directory 
```
cd 
```
```
cd .. #ถอยกลับออกจากโฟลเดอร์ปัจจุบัน 1 ครั้ง
cd ../.. #ออกจากโฟลเดอร์ปัจจุบัน 2 ครั้ง
```
```
cd .xxx/yyy/zzz #เปลี่ยน directory แบบระบุปลายทาง
```
```
cd filename/ xxx #กรณีที่ชื่อไฟล์มี spacebar คั่น Ex. Class 4 ต้องพิมพ์ `cd Class/ 4`
```
### 5. Create file 
``` 
vi
vi {filename}  #สร้างและเปิดไฟล์
vi {filename.py} #python 
  #กด i เพื่อแก้ไข
  #กด esc + :wq (exit & save)
  #กด esc + :q! (exit but don't save)
```
### 6. Open file
```
cat filename #เวลาเราสั่งไม่จำเป็นต้องเข้าไปอยู่ใน folder นั้นๆ
```
### 7. Move file 
```
mv {ที่อยู่ต้นทางของ file/folder ที่ต้องการย้าย} {ที่อยู่ปลายทางที่ต้องการที่จะย้าย file/folder ไป}
mv file name .location
mv .xxxxx .zzzzzz #เป็นวิธีการเปลี่ยนชื่อรูปแบบหนึ่ง #Ex. mv ชื่อเก่า ชื่อใหม่
```
### 8. Copy file
```
cp {ที่อยู่ต้นทางของ file/folder ที่ต้องการคัดลอก} {ที่อยู่ปลายทางที่ต้องการที่จะคัดลอก file/folder ไป}
cp .zzzzzzz . #คัดลอกไฟล์มาที่โฟลเดอร์ปัจจุบัน
```
### 9. Manual page
```
man #ดูเอกสารคำสั่งและโปรแกรมต่าง ๆ ในรูปแบบ "หน้าคู่มือ" 
man ls #ใช้ดูรายการไฟล์ #ใช้ได้กับทุกคำสั่ง ที่เขาเขียน Instruction มาให้
```
### 10. Delete file
```
rm # ลบไฟล์
rm -r #.ให้มัน recursive ลบทุกไฟล์ที่มีอยู่ในโฟลเดอร์ เพื่อลบทั้งโฟลเดอร์
```
### 11. Check Systems Preference
```
htop #เอาไว้ดูว่ามี RAM อยู่เท่าไหร่ ดูการใช้งานของเครื่อง # ต้อง Install ก่อน
```
# 11/12/2567
## Virtual Machine

### 1. การเข้า Server ด้วย `ssh ย่อมาจาก Secure Shell` `#คิดเหมือนเปลือกหอย ค่อยๆ หุ้ม ค่อยๆ เข้า`
```
ssh username@IPaddress
```

### 2. เพิ่ม `User` เพื่อนให้เข้า server ของเราได้
```
sudo adduser friendusername
```

### 3. ใช้ดูการเคลื่อนไหวใน server ของเรา
```
htop
```

### 4. ย้าย group
```
sudo usermod ชื่อเพื่อน ชื่อเรา #ชื่อเพื่อน = group ชื่อเรา = folder
```
```
sudo groups ชื่อเรา #เช็คว่ามีใครอยู่ใน server
```

### 5. เพิ่มเพื่อนให้เป็น SuperUser Do `sudo`
```
sudo adduser ชื่อเพื่อน sudo 
```
# 24/12/2567
## Ubuntu on Cloud VM
## 1. Create VM 
เข้า Portal Azure >>> Education >>> VM >>> Create a virtual machine

## 2. Login & Logout
```
ssh username@IP #login
exit #logout /// จบ section
```

## 3. ออกจาก function ex. python
```
exit()
```

## 4. scp = secure copy 

- รูปแบบ
  ```
  scp {path ต้นทาง} {path ปลายทาง}
  ```

- ส่งไฟล์จากเครื่องเราไปบน Cloud (ต้องรันบนเครื่องเรา)
  ```
  scp ./xxx nnnt@IP:~/xxx/xxx/. Ex. scp ./testcode.py nnnt@4.221.171.101:~/code/.
  scp -r testfolder1/ nnnt@IP:~/nnnt/. # cp folder in PC to Cloud
  ```

- ดึงไฟล์จาก cloud มาเครื่องเรา (ต้องรันบนเครื่องเรา)
  ```
  scp nnnt@IP:/xxx/xxx/yyy.py /home/nnnt
  scp nnnt@4.221.171.101:/home/nnnt/code2/newtest.py /Users/macbookair # move file from folder name code2  on nnnt Cloud to PC
  ```

## 5. Session
```
screen -S {screen name} #สร้าง
```
```
screen -R #กระโดดกลับเข้่าไปที่ screen
```
- กด control A+D ออกจาก session
- กด control A+K+y ออกและลบ session

## 6. Github
  - Save code on github
  ```
  git clone https://github.com/Pattaratron/AIPrototype24.git
  git add testcloudvm.py
  git commit -m "test cloud server"
  git push
  ```
  - Setting owner Github (ทำครั้งเดียว)
  ```
  git config --global user.name "Ratchanontt"
  git config --global user.email "ratchanont.t@kkumail.com"
  ```
