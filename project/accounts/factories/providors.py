
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
class AddressStreetProvider(BaseProvider):
    def  street_name(self):
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

        return random.choice(egyptian_village_names)
class AddressCityProvider(BaseProvider):
    def  city(self):
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

        return random.choice(egyptian_village_names)

class AddressGovernorateProvider(BaseProvider):
    def  state(self):
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

        return random.choice(egyptian_village_names)
    

factory.Faker.add_provider(AlphanumericCode)
factory.Faker.add_provider(NationalityProvider)
factory.Faker.add_provider(ArabicNameProvider)
factory.Faker.add_provider(AddressStreetProvider)
factory.Faker.add_provider(AddressCityProvider)
factory.Faker.add_provider(AddressGovernorateProvider)

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