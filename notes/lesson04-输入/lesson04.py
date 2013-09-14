#Crossin lesson04 输入
 
#python有一个接收命令行下输入的方法：input()
 
print "Who do you think I am?"
input() #和print不同，input必须加上()
print "Oh, yes!"
 
#运行该文件，会直接显示「Who do you think I am?」这句话，接下来输入答案（如果答案是字符串，需要加上''或""，如果是数字或变量则不用。），程序会回答「Oh, yes!」

#Python 还有另一个输入的方法：raw_input()，它把所有的输入都直接当做一串字符，可以不用加引号。