import boto3
s3 = boto3.client('s3')

# Сохранение файла
s3.put_object(Bucket='compworkshop', Key='example.txt', Body="Hello, World!")
s3.put_object(Bucket='compworkshop', Key='temp.txt', Body='This file will be delete')

# Удаление файла
s3.delete_object(Bucket='compworkshop', Key="temp.txt")

# Получение данных из бакета
for key in s3.list_objects(Bucket='compworkshop')['Contents']:
	print(key['Key'])

# Получить определенный объект
object = s3.get_object(Bucket='compworkshop', Key='example.txt')
print(object['Body'].read())
