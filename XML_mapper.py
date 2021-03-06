﻿# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        модуль1
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
        with open(file_json_name+'.json', 'w') as f:
            f.write(json.dumps(self.filtred_results_of_element, sort_keys=True, indent=4))

    def tag_filter(self,model_name):
        """Метод для фильтрации тегов
        model_name - имя модели
        """
        pk=0
        res=[]
        for element in self.results_of_element:
            for obj,tags in element.items():
                tag_model={"model": model_name,"pk":pk}
                for tag in tags:
                    for tag_name,tag_value in tag.items():
                        if self.is_parse_tag(tag_name):
                            tag_model.update({tag_name:tag_value})
                res.append({obj:tag_model})
                pk+=1
        self.filtred_results_of_element=res

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
        res={}
        res.update({element_name.tag:[]})
        if len(element_name)==0:
            if element_name.text!=None:
                res[element_name.tag].append(element_name.text)
            if (element_name.attrib!={}):
                res[element_name.tag].append(element_name.attrib)
        else:
            for child in element_name:
                res[element_name.tag].append(self.__find(child))
        return res

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
        if node.nodeType == node.TEXT_NODE:
            if node.nodeValue.strip():
                print(str(". "*level)+"  "+node.nodeValue.strip())
        else: # ELEMENT_NODE или DOCUMENT_NODE
            atts = node.attributes or {}
            att_string = ", ".join(["%s=%s " % (k, v) for k, v in atts.items()])
            print(str(". "*level)+"  "+node.nodeName+"  "+str(att_string))
            for child in node.childNodes:
                self.__output_tree(child, level+1)


def main():
    mapper=XmlMmapper('test.xml')
    mapper.add_parse_objects('event')
    #
    #mapper.add_parse_tags('title','value')
    mapper.add_parse_tags('runtime','value')
    mapper.add_parse_tags('age_restricted','value')
    mapper.add_parse_tags('tags','list')
    mapper.add_parse_tags('gallery','list')
    mapper.add_parse_tags('text','value')
    mapper.add_parse_tags('tag','value')
    mapper.add_parse_tags('description','value')
    mapper.add_parse_tags('stage_theatre','value')
    mapper.find('event')
    print(mapper.results_of_element)
    mapper.tojson('test')
    #print(mapper.is_parse_tag('title'))
    mapper.tag_filter('model')
    print(mapper.filtred_results_of_element)


def main():
    pass

if __name__ == '__main__':
    main()
