#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Дмитрий
#
# Created:     12.03.2016
# Copyright:   (c) Дмитрий 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import XML_mapper
def main():
    #Подключаем модуль
    mapper=XML_mapper.XmlMmapper('test.xml')
    # Указываем объект
    mapper.add_parse_objects('event')
    #Указываем теги, которые следует учитывать в модели
    mapper.add_parse_tags('title','value')
    mapper.add_parse_tags('runtime','value')
    mapper.add_parse_tags('age_restricted','value')
    mapper.add_parse_tags('tags','list')
    mapper.add_parse_tags('gallery','list')
    mapper.add_parse_tags('text','value')
    mapper.add_parse_tags('tag','value')
    mapper.add_parse_tags('description','value')
    mapper.add_parse_tags('stage_theatre','value')
    #Выполняем поиск
    mapper.find('event')
    #Выводим на печать результат
    print(mapper.results_of_element[1])
    #Импорт в json для дальнейшей работы с моделью
    #Задаем имя файла 'test'
    mapper.tojson('test')
    #Фильтруем теги, оставляя только заданные
    mapper.tag_filter('model')
    #Выводим на печать результат фильтрации
    print(mapper.results_of_element[1])

if __name__ == '__main__':
    main()
