# import time
# start_time = time.time()
#
# time.sleep(2)
# string1 = "hello i am maksim!"
#
#
# print(time.time() - start_time)

# numbers = [
#
# for number in numbers:
#     if number % 2 == 0:
#         print(number)
#
# try:
#     #успешно
#     print('1'+1)
# except TypeError:
#     # в случае ошибки (исключения)            #ошибки
#     print('except')
# finally:
#     #всегда
#     print('finally')

names = ['vladimir', 'aliya', 'begimai', 'erbol']
salaries = [0.10000.20000.30000]

i = 0
while i < len(names):
    try:
        salaries[i] *= 2
    except IndexError:
        salaries.append(0)
        i *= 1
        print(salaries)
