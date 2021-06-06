# function 函式/功能

# function是用來{收納}程式碼的
# 他是個功能

def wash(dry=False, water=8):
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')

wash(True) #使用function
wash(water=5)

def say_hi():
    print('hi!!!')

say_hi()

def add(x=0, y=0): #寫參數的時候，等號左右不用空格  ;如果沒有預設值，那在使用函式就一定要給值
    print(x + y)

add(4, 10)
add()
add(y=5)

def add2(x, y):  #function如果有return，就可以把function執行的結果給存下來
    return x + y

result = add2(3,4)
print(result)

# def average(numbers):
#     avg = sum(numbers) / len(numbers)
#     return avg

def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 2, 3]))
print(average([10, 99, 12]))




