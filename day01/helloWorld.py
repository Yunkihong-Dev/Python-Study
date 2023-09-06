from random import *

# 주석


'''
여러 
문장 
주석
'''
print('hello World!')
date = randint(3,28);
print("오프라인 스터디 모임은 매월 " + str(date)+"일로 선정되었습니다.")


sentence = """
파이썬은
정말
쉬워요
"""

sentence2= "JAVA is easy"


print(sentence)
print(sentence.replace("쉬워요","어려워요"))

print(f"내 생각에{sentence}")


index1 = sentence.index("파이썬")
index2 = sentence.find("자바")
print(index1)
print(index2)

print(sentence2.upper())
print(sentence2.lower())


# url = "http://naver.com"
# splittedUrl = url.split('//')[1].split('.')[0]
# print(splittedUrl[:3]+str(len(splittedUrl))+str(splittedUrl.count("e"))+"!")

url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
# print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))+"!"

print("{0}의 비밀번호는 {1} 입니다.".format(url,password))


subway = ["하하","김밥천국","김종국"]
 
print(subway)
print(subway.index("김종국"))
print(subway.pop())
print(subway)

subway.insert(1,"정형돈")
print(subway)
subway.append("유재석")
print(subway)
subway.sort();
print(subway)
subway.reverse();
print(subway)
subway.clear();
print(subway)


cabinet = {3:"유재석", 100:"런닝맨"}
print(cabinet[3])

print(cabinet.get(4))

if 3 in cabinet:
    print("있어")
else:
    print("없어")


cabinet["A-3"]="차차차"

print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()