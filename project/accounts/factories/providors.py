
import random
import factory
from faker.providers import BaseProvider




class AlphanumericCode(BaseProvider):
    def alphanumeric_code(self):
        # Generate your product code logic here
        return "PROD" + "".join(str(random.randint(0, 9)) for _ in range(6))

class NationalityProvider(BaseProvider):
    def  national_id(self):
        # Generate your product code logic here
        return  "".join(str(random.randint(0, 9)) for _ in range(14))
class ArabicNameProvider(BaseProvider):
    def  arabic_name(self):
        arabic_mens_names = [
            "محمد", "علي", "أحمد", "عمر", "يوسف",
            "خالد", "حسن", "مصطفى", "حسام", "محمود",
            "سعيد", "طارق", "عبد الله", "عليّ", "ماجد",
            "جمال", "وليد", "مروان", "ناصر", "رشيد",
            "حسين", "سليمان", "عبدالرحمن", "فارس", "ياسر",
            "عليان", "رامي", "خضر", "طلال",
            "حازم", "أسامة", "منصور", "مالك", "نواف",  "شريف", "أيمن"
        ]
        arabic_names_same=[
            "أسامة","أسامه","اسامه","اسَامه","احمد","أحمد","أمين","امين","إياد","إياد","أكرم","اكرم"
        ]

        arabic_names = [ "نور", "إحسان","جهاد",",وسام","اسلام","أسلام","اسلام","احسان"]



        last=" ".join(random.choice(arabic_names_same) for _ in range(3))
        first=random.choice(arabic_names)
        return first+" "+last


class AddressProvider(BaseProvider):
    def  address(self):
        egyptian_village_names = [
            "الدلجا",
            "كفر الشيخ",
            "بركة السبع",
            "قلوص",
            "الشهداء",
            "سمسطا",
            "دمنهور",
            "كفر الشيخ الجديدة",
            "بدر",
            "برمبال",
            "كفر المنجوم",
            "النوبارية",
            "الرياض",
            "البيضاء",
            "الرزايقة",
            "قرية النيل",
            "دسوق",
            "كفر البطيخ",
            "أبو النمرس",
            "أبو حمص"
        ]

        return {
            'street':random.choice(egyptian_village_names),
            'city':random.choice(egyptian_village_names),
            'governorate':random.choice(egyptian_village_names),
        } 
    

factory.Faker.add_provider(AlphanumericCode)
factory.Faker.add_provider(NationalityProvider)
factory.Faker.add_provider(ArabicNameProvider)
factory.Faker.add_provider(AddressProvider)


class DoctorSpecializationProvider(BaseProvider):
    def  doctor_specialization(self):
        specializations= [
            "عظام",
            "جراحة",
            "جراحة عامة",
            "جراحة اطفال",
            "جراحة العيون",
            "جراحة الفم",
            "جراحة العظام",
            "جراحة الجهاز العضلي",
            "أورام",

        ]
        return random.choice(specializations)

factory.Faker.add_provider(DoctorSpecializationProvider)

class DaysProvider(BaseProvider):
    def  week_days(self):
        days= [
            "Saturday",
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
        ]
        return " ".join(random.sample(days, 3))

factory.Faker.add_provider(DaysProvider)


class PhoneProvider(BaseProvider):
    def  phone(self):
       
        return " ".join("".join(str(random.randint(0, 9)) for _ in range(11)))

factory.Faker.add_provider(PhoneProvider)