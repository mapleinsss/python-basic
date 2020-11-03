# 在字符串模板中使用 key
temp = '书名是：%(name)s,价格是%(price)010.2f,出版社是:%(publish)s'
book = {'name': '深入python学习', 'price': 22, 'publish': '机械工业出版社'}
print(temp % book)  # 书名是：深入python学习,价格是0000022.00,出版社是:机械工业出版社
