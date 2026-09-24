debt = input("آیا دانشجو بدهی مالی دارد؟ 1 = بله , 0 = خیر: ")
while debt not in ["0", "1"]:
    print("لطفا عدد مناسب را وارد کنید (0 یا 1).")
    debt = input("آیا دانشجو بدهی مالی دارد؟ 1 = بله , 0 = خیر: ")
debt = int(debt)

if debt == 1:
    print("غیر مجاز است - علت: بدهی")
else:
    avg = float(input("معدل کل: "))
    if avg < 15:
        print("غیر مجاز است-علت:معدل کمتر از 15")
    else:
        per1 = float(input("نمره ی پیش نیاز 1: "))
        per2 = float(input("نمره ی پیش نیاز 2: "))
        per3 = float(input("نمره پیش نیاز 3: "))

        if 15 <= avg < 17 and (per1 + per2 + per3) < 45:
            print("غیر مجاز است-علت:مجموع نمرات پیش نیاز کمتر از 45")
        else:
            total_units = int(input("تعداد کل واحد های پاس شده: "))
            if total_units < 95:
                print("غیر مجاز است-علت:کمتر از 95 واحد پاس")
            else:
                failed = int(input("تعداد درس های افتاده: "))

                if 95 <= total_units <= 110 and failed > 0:
                    print("غیر مجاز-علت:یک درس باقی مانده")
                elif total_units > 110 and failed > 1:
                    print("غیر مجاز-علت:بیش از 1 درس افتاده")
                else:
                    terms = int(input("تعداد ترم های گذرانده: "))

                    if terms < 5:
                        print("غیر مجاز-علت:تعداد بالای ترم")
                    elif terms > 8 and avg < 16:
                        print("غیر مجاز است- علت:معدل کمتر از 16")
                    else:
                        job = input("آیا شاغل هستید؟ 1 = بله , 0 = خیر: ")
                        while job not in ["0", "1"]:
                            print("لطفا عدد مناسب را وارد کنید (0 یا 1).")
                            job = input("آیا شاغل هستید؟ 1 = بله , 0 = خیر: ")
                        job = int(job)

                        if job == 1:
                            print("فقط مجاز به اخذ 2 درس میباشید")
                        else:
                            print("مجاز به اخذ 3 درس میباشید")
