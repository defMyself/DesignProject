
filename = "zzu.txt"

def handleSubresult(filename):
    """
    处理Sublist3r重定向产生的txt文件
    返回子域名列表
    """
    with open(filename) as f:
        contents = f.read()
        c = contents.split('\n')
        result = []

        # print(c[0])
        # 22 line total unique found : 14
        # print(c[22])
        
        # 
        for i in range(23, len(c)-1):
            result.append(c[i])

        return result


re = handleSubresult(filename)
for i in re:
    print(i)

print("total number = {}".format(len(re)))

