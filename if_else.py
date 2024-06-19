# ism=(input("assalomu alaykum ismingiz nima birodar ?\n>>>"))
# yosh=int(input(f"yoshingiz nechida {ism} ?\n>>>"))
# if yosh<=4 or yosh>60:
#     print(f"sizga kirish bepul {ism}")
# elif yosh<=18:
#     print(f"sizga kirish 10000 so'm {ism}")
# elif yosh>=18:
#     print(f"sizga kirish 20000 so'm {ism}")
# son=int(input("1-sonni kiriting\n>>>"))
# son1=int(input("2-sonni kiriting\n>>>"))
# if son==son1:
#     print("sonlar teng")
# elif son>son1:
#     print('1- son katta 2-sondan')
# elif son<son1:
#     print("1-son kichik 2-sondan")
# mahsulotlar=["taroq", "qaychi", "ruchka", "qalam", "o'irgich", "telefon", "sichqoncha", "kompyuter"]
# savat=[]
# for n in range(5):
#     savat.append(input(f"savatga {n+1}-mahsulotni kiriting\n>>>"))




#  for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#              print(f"dokonda {mahsulot} mahsulot bor")
#         else:
#              print(f"kechirasiz dokonda {mahsulot} mahsulot yoq") 





# mahsulotlar=["taroq", "qaychi", "ruchka", "qalam", "o'irgich", "telefon", "sichqoncha", "kompyuter"]
# savat=[]
# for n in range(5):
#     savat.append(input(f"savatga {n+1}-mahsulotni kiriting\n>>>"))


# bor_mahsulotlar=[]
# mavjud_emas=[]
# for mahsulot in savat:
#          if mahsulot in mahsulotlar:
#              bor_mahsulotlar.append(mahsulot)
#          else:
#              mavjud_emas.append(mahsulot)
# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# users=["ali", "vali", "g'ani", "aziz", "avaz"]
# login=input("yangi login tanlang\n>>>")
# if login.lower() in users:
#         print("boshqa login tanlang bu login band qilingan")
# else:
#         print("xush kelibsiz")
son = int(input("biror butun son kiriting\n>>>"))
boluv = range(2, 11)
for n in boluv:
    if not (son % n):
        print(n)