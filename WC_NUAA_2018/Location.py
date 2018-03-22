# -*- coding: utf-8 -*-
#wordcloud生成中文词云

from wordcloud import WordCloud, ImageColorGenerator
import codecs
import jieba
#import jieba.analyse as analyse
from scipy.misc import imread
import os
from os import path
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


# 绘制词云
def draw_wordcloud():
    #读入一个txt文件
    comment_text = open('Location.txt','r').read()
    #结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
    jieba.load_userdict('Location.txt')	
    cut_text = " ".join(jieba.cut(comment_text))
    d = path.dirname(__file__) # 当前文件文件夹所在目录
    color_mask = imread("Cloud.png") # 读取背景图片
    cloud = WordCloud(
        #设置字体，不指定就会出现乱码
        font_path="SIMHEI.TTF",
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色
        background_color='white',
        #词云形状
        mask=color_mask,
        #允许最大词汇
        max_words=2000,
        #最大号字体
        max_font_size=250,
	min_font_size=45,
        width=1920,
        height=1080,
	prefer_horizontal=0.95,
        margin=0
    )
    word_cloud = cloud.generate(cut_text) # 产生词云
    image_colors = ImageColorGenerator(color_mask)
    word_cloud.to_file("Location.png") #保存图片
    #  显示词云图片
    #plt.imshow(word_cloud,interpolation="bilinear")
    #plt.imshow(word_cloud.recolor(color_func=image_colors))
    #plt.axis('off')
    #plt.show()



if __name__ == '__main__':

    draw_wordcloud()
