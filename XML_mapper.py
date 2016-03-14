# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        XMLmapper
# Author:      Дмитрий Цымай
#
#-------------------------------------------------------------------------------

import xml.dom.minidom as dom
import xml.etree.ElementTree as etree
import json



class XmlMmapper:
    """Класс парсера XML
    """

    def __init__(self,path=None,url=None):
        """Инициализация
        Выполняется подключение файла-источника
        path Путь к файлу XML
        """

    def add_parse_objects(self,element_name):
        """Метод для добавления интересующих элементов
        element_name - имя объекта
        """

    def is_parse_tag(self,tag_name):
        """Метод проверки наличия тега в списке
        Используется для фильтра в методе __find()
        tag_name - Имя тега
        """

    def tojson(self,file_json_name):
        """ Метод для преобразования результатов работы парсера в json формат
        file_json_name - имя файла
        """

    def tag_filter(self):
        """Метод для фильтрации тегов
        """

    def find(self,element_name):
        """Метод для поиска заданного элемента
        element_name - искомый элемент
        """
        element_list=self.name_parse_obj[element_name]
        for element in element_list:
            self.results_of_element.append(self.__find(element))

    def __find(self,element_name):
        """Метод для поиска заданного элемента
        element_name - искомый элемент
        Метод является вспомогательным к find(). Вызывается рекурсивно.
        """

    def output_tree(self):
        """Вывод на печать древа dom XML документа
        использует вспомогательный метод __output_tree()
        """
        self.__output_tree(self.dom)

    def __output_tree(self, node, level=0):
        """Вывод на печать древа dom XML документа
        Вспомогательный метод для output_tree().
        Вызывается рекурсивно
        """



def main():
    pass

if __name__ == '__main__':
    main()
