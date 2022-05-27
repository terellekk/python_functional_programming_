# def quick_meal():
#     a = ['Indomie', 'Egg', 'Onion', 'Tomato', 'Sausage']
#     for i in a:
#         return (i)
#     a.append('Suya')
#     return (a)
# g = quick_meal()
# print(g)
# # def quick_meal():
# #     a = ['Indomie', 'Egg', 'Onion', 'Tomato', 'Sausage']
# #     for i in a:
# #         print(i)
# #     a.append('Suya')
# #     print (a)
# # quick_meal()


from logging import root


def cube_root(num):
    answer = num ** (1/3)
    return answer

def main_interface():
    print('Good morning. pls find the cuberoot by providing your number')
    num = int(input('Enter your number'))
    result = cube_root(num)
    print(f'result is {result}')

main_interface()
square root
add