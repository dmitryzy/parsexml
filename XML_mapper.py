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
        self.dom=dom.parse(path)
        #
        self.dom.normalize()
        self.tree = etree.parse(path)
        self.root = self.tree.getroot()
        self.results_of_element=[]
        self.filtred_results_of_element=[]
        self.name_parse_obj={}
        self.model_tags={}
        self.model_tag_type=['value','link','list','text']

    def add_parse_objects(self,element_name):
        """Метод для добавления интересующих элементов
        element_name - имя объекта
        """
        self.name_parse_obj[element_name]=self.tree.findall('*'+element_name)
        self.find(element_name)

    def add_parse_tags(self,model_tag_name, model_tag_type):
        """Метод для добавления интересующих тегов
        model_tag_name - название тега
        model_tag_type - тип
        """
        if model_tag_type not in self.model_tag_type:
            model_tag_type=None
        self.model_tags[model_tag_name]=model_tag_type

    def is_parse_tag(self,tag_name):
        """Метод проверки наличия тега в списке
        Используется для фильтра в методе __find()
        tag_name - Имя тега
        """
        res=True if ((tag_name in self.model_tags)or(tag_name in self.name_parse_obj)) else False
        return res

    def tojson(self,file_json_name):
        """ Метод для преобразования результатов работы парсера в json формат
        file_json_name - имя файла
        """
        with open(file_json_name+'.json', 'w'):
            write(json.dumps(self.filtred_results_of_element, sort_keys=True, indent=4))

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
