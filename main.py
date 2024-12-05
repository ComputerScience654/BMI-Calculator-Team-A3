'''
นายปัญจพล รัตนประเสริฐ 465415241006
นายพงศ์สถิต  ตั้งบวรไพศาล 465415241021
CSS46541N
'''
def bmi_calculate():
    
    #แสดงชื่อโปรแกรม
    print("โปรแกรมคำนวณดัชนีมวลกาย BMI")
    
    #รับข้อมูลน้ำหนักและส่วนสูง
    weight = float(input("กรุณาระบุน้ำหนักของคุณ (กิโลกรัม): "))
    height_cm = float(input("กรุณาระบุส่วนสูงของคุณ (เซนติเมตร): "))
    
    #แปลงส่วนสูงจาก เซนติเมตร เป็น เมตร
    height_m = height_cm / 100
    
    #คำนวณBMI
    bmi = weight/(height_m ** 2)
    
    #แสดงค่าBMI
    print(f"ค่าดัชนีมวลกายของคุณคือ: {bmi:.2f}")
    
    #วิเคราะห์BMI
    if bmi < 18.5:
        print("ผลลัพธ์: น้ำหนักต่ำกว่าเกณฑ์ มีความเสี่ยงเกิดโรคขาดสารอาหาร")
    elif 18.5 <= bmi < 22.9:
        print("ผลลัพธ์: น้ำหนักสมส่วน มีโอกาสเกิดโรคแทรกซ้อนน้อยที่สุด")
    elif 23.0 <= bmi < 24.9:
        print("ผลลัพธ์: น้ำหนักเกินมาตรฐาน ภาวะน้ำหนักเกินระยะเริ่มต้น เริ่มมีโรคแทรกซ้อนเล็กน้อย")
    elif 25.0 <= bmi < 29.9:
        print("ผลลัพธ์: โรคอ้วนระดับที่1 ภาวะน้ำหนักเกินมาก มีโรคแทรกซ้อนในระยะอ้วนเริ่มต้น")
    else:
        print("ผลลัพธ์: โรคอ้วนระดับที่2 มีโอกาสเป็นโรคเบาหวานชนิดที่2 ความดันโลหิตสูง โรคหลอดเลือดสมอง โรคหลอดเลือดหัวใจ มะเร็งบางชนิด")
    
#เรียกใช้งานฟังก์ชั่น
bmi_calculate()
    
    
    
    
    
    