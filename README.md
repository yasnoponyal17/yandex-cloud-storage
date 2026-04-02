# Лабораторная работа. Объектное хранилище S3.
## Постановка задачи
1. Создайте бакет в Yandex Cloud
2. Создайте сервисный аккаунт
3. Реализуйте функции (локально) для выполнения основных операций с объектами в хранилище: получение списка загруженных файлов, загрузка файла в бакет, получение файла, удаление файла. Продемонстрируйте их работу.
## Код программы
```python
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

# Получить содержимое файла
object = s3.get_object(Bucket='compworkshop', Key='example.txt')
print(object['Body'].read())

```
## Пояснение к коду
1. Cохраняем два файла example.txt и temp.txt
2. Удаляем файл temp.txt
3. Выводим все файлы, которые есть в бакете
4. Выводим содержимое файла example.txt
## Результат работы
![result](images/result.png)
