# 1. Դեկորատորներ (Decorators)
# 1.	Timer Decorator: Գրիր դեկորատոր, որը չափում և տպում է ֆունկցիայի կատարման տևողությունը (օգտագործիր time մոդուլը)։
# from time import time
# import time

# def decorator(func):
#     def inner(*args, **kwargs):
#         now = time.time()
#         x = func(*args, **kwargs)
#         later = time.time()
#         print(later-now)
#         return x
#     return inner

# @decorator
# def printer(a):
#     print(f"hello {a}")

# printer("halo")

# 2.	Logger Decorator: Ստեղծիր դեկորատոր, որը ֆունկցիան կանչելիս տպում է դրա անունը և փոխանցված արգումենտները։

# def logger(func):
#     def inner(*args, **kwargs):
#         print(func.__name__)
#         print(*args)
#         print(*kwargs)
#         x = func(*args, **kwargs)
#         return x
#     return inner

# @logger
# def func(a, **kwargs):
#     print(a, *kwargs)

# func(123, x = 10)

# 3.	Auth Decorator: Գրիր դեկորատոր, որը ստուգում է օգտատիրոջ կարգավիճակը (օրինակ՝ is_admin փոփոխականը) և թույլ է տալիս կանչել ֆունկցիան միայն True-ի դեպքում։

# def auth(func):
#     def inner(*args, **kwargs):
#         if not is_admin:
#             return "no"
#         x = func(*args, **kwargs)
#         return x
#     return inner
# is_admin = False
# @auth
# def printer(a):
#     print(f"hello {a}")

# printer("halo")



# 4.	Retry Decorator: Ստեղծիր դեկորատոր, որը սխալի (Exception) դեպքում փորձում է նորից կանչել ֆունկցիան մինչև 3 անգամ։

# def retry(func):
#     def inner(*args, **kwargs):
#         x = None
#         try:
#             x = func(*args, **kwargs)
#         except Exception:
#             print("error1")
#             try:
#                 x = func(*args, **kwargs)
#             except Exception:
#                 print("error2")
#                 try:
#                     x = func(*args, **kwargs)
#                 except Exception:
#                     print("too many errors")
#         return x
#     return inner
            

# @retry
# def printer(a):
#     prit(f"hello {a}")

# printer("halo")

# 5.	Result Formatter: Գրիր դեկորատոր, որը ֆունկցիայի վերադարձրած արժեքը (տեքստը) դարձնում է մեծատառ (uppercase)։



# 2. Պարամետրերով դեկորատորներ (Decorators with Arguments)
# 1.	Repeat Decorator: Գրիր դեկորատոր, որն ընդունում է n թիվը և կանչում է տվյալ ֆունկցիան n անգամ։
# 2.	Access Level: Ստեղծիր դեկորատոր, որն ընդունում է required_role (օրինակ՝ "admin" կամ "guest") և ստուգում է՝ արդյոք օգտատերը ունի այդ իրավունքը։
# 3.	Rate Limiter: Գրիր դեկորատոր, որն ընդունում է վայրկյանների քանակ և թույլ չի տալիս ֆունկցիան կանչել ավելի հաճախ, քան նշված ժամանակն է։
# 4.	Prefix Decorator: Ստեղծիր դեկորատոր, որն ընդունում է տեքստային պրեֆիքս և ավելացնում է այն ֆունկցիայի վերադարձրած արժեքին։
# 3. Կլասներ (Classes)
# Կլասների կառուցվածքի և ինկապսուլյացիայի վարժություններ։
# 1.	Student Registry: Ստեղծիր Student կլաս՝ անուն, ազգանուն և գնահատականների ցուցակ հատկանիշներով։ Ավելացրու մեթոդ միջին գնահատականը հաշվելու համար։
# 2.	Rectangle Class: Ստեղծիր կլաս, որն ունի երկարություն և լայնություն։ Ավելացրու @property դեկորատորը մակերեսը հաշվելու համար։
# 3.	Encapsulation: Ստեղծիր User կլաս, որտեղ գաղտնաբառը (__password) կլինի private։ Գրիր մեթոդներ այն փոխելու համար միայն հին գաղտնաբառը ճիշտ ներմուծելու դեպքում։
class User:
    def __init__(self, password):
        self.__password = password