# COVID-19 Line Notify
เป็นโครงการ Python ที่ส่ง Line notification พร้อมสถิติ COVID-19 ล่าสุดในประเทศไทย ทุกวัน เวลา 07.40 น. การแจ้งเตือนทางไลน์ประกอบด้วยจำนวนเคสใหม่, เคสทั้งหมด, การกู้คืนทั้งหมด และความแตกต่างของจำนวนเคสจากวันก่อนหน้า

## Libraries
* requests
* schedule
* datetime
* API Used

## API Used
* https://covid19.ddc.moph.go.th/api/Cases/today-cases-all

## Line Notify API
โปรเจ็กต์นี้ใช้ Line Notify API เพื่อส่งการแจ้งเตือนไปยังแชทไลน์ หากต้องการใช้ API คุณต้องสร้างโทเค็นการเข้าถึงจากเว็บไซต์ Line Notify (https://notify-bot.line.me/en/) 
และรวมไว้ในส่วนหัวของคำขอ

## วิธีดำเนินโครงการ
เพื่อดำเนินโครงการ:

1.คัดลอกโค้ดลงใน Python IDE หรือโปรแกรมแก้ไขข้อความ

2.แทนที่โทเค็นการเข้าถึง Line Notify ด้วยของคุณเอง

3.เรียกใช้ code 

4.โปรเจ็กต์จะทำงานอยู่เบื้องหลัง และจะมีการแจ้งเตือนทาง Line ทุกวัน เวลา 07:40 น.

## บทสรุป
โครงการนี้เป็นวิธีที่ง่ายและมีประสิทธิภาพในการติดตามสถิติล่าสุดของ COVID-19 ในประเทศไทย ด้วย Line Notify คุณสามารถรับการแจ้งเตือนโดยตรงไปยังแชท Line ของคุณ 
ทำให้ง่ายต่อการรับทราบข้อมูลโดยไม่ต้องตรวจสอบข้อมูลจากแหล่งต่างๆ

## ตัวอย่าง COVID-19 Line Notify
![covide](https://user-images.githubusercontent.com/104154862/233909153-0b15cb6a-b722-457b-b9d9-af238c94d6f5.jpg)

# HentaiThai Line Notify
นี่คือสคริปต์ Python ที่ส่งชื่อและลิงก์ของหนังสือการ์ตูนโป๊ญี่ปุ่นจากเว็บไซต์ "https://hentaithai.com/" ผ่าน Line Notify API โดยสคริปต์นี้ถูกกำหนดเวลาให้ทำงานทุก 10 วินาทีและส่งข้อความพร้อม 5 ชื่อหนังสือการ์ตูนโป๊ญี่ปุ่นและลิงก์ที่สอดคล้องกัน

## วิธีการติดตั้ง
1.clone หรือดาวน์โหลดไฟล์ zip โปรเจคนี้

2.ติดตั้งแพ็คเกจที่จำเป็นด้วย requirement.txt

3.สร้างบัญชี Line Notify และรับโทเค็นการเข้าถึงจาก https://notify-bot.line.me/

4.แทนที่ค่าโทเค็นในสคริปต์ด้วยโทเค็นการเข้าถึงของคุณ

## วิธีการใช้
เข้าไปที่ doujin line
เรียกใช้ python main.py

สคริปต์จะทำงานเบื้องหลังและส่งการแจ้งเตือนไปยังบัญชี Line ของคุณทุก 10 วินาทีหรือตามการตั้งค่าของคุณ

## ประกาศ
สคริปต์นี้ได้รับการพัฒนาเพื่อวัตถุประสงค์การศึกษาเท่านั้น ผู้เขียนไม่ได้รับการสนับสนุนหรือสนับสนุนใด ๆ ในการใช้เนื้อหาของหนังสือการ์ตูนโป๊ญี่ปุ่น โปรดใช้ตามดุลยพินิจของคุณเอง

## ตัวอย่าง HentaiThai Line Notify
![hen](https://user-images.githubusercontent.com/104154862/233909148-0af8870a-380e-4440-9859-c571844d3f66.jpg)


