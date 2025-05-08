Persian = {
    'English': 'فارسی',
    'Choose language': 'زبان خود را انتخاب کنید',
    'Please enter password:': 'رمز خود را وارد کنید:',
    'Submit': 'ثبت',
    'Get Cash': 'برداشت وجه',
    'Money Transfer': 'انتقال وجه',
    'Change Password': 'تغییر رمز',
    'Account Balance': 'موجودی حساب',
    'Mission Accomplished Successfully!': 'عملیات با موفقیت انجام شد!',
    'Goodbye': 'خدانگهدار',
    'New Mission': 'عملیات جدید',
    'Enter New Password:': 'رمز جدید را وارد کنید:',
    'Confirm': 'تایید',
    'Enter the desired amount:': 'مبلغ مورد نظر را وارد کنید:',
    'Enter the destination card number:': 'شماره کارت مقصد را وارد کنید:',
    'Your bank account balance:': 'موجودی حساب شما:',
    'Your balance is not enough!': 'موجودی حساب کافی نیست!',
    'Mission Failed!': 'عملیات با شکست مواجه شد!'
}

class Text:
    def __init__(self):
        self.__language = 'en'

    def __call__(self, string: str) -> str:
        if self.__language == 'en' or string not in Persian:
            return string
        return Persian[string]

    def change_to_persian(self):
        self.__language = 'fa'

    def change_to_english(self):
        self.__language = 'en'

