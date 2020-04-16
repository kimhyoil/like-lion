from faker import Faker

myfake = Faker()

# 영구적인 가짜 데이터
myfake.seed(1)

myfake.name()
myfake.address()
myfake.text()
myfake.state()
myfake.sentence()
myfake.random_number()