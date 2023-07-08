import pandas as pd
import os
#data = pd.read_excel('go_pla.xlsx')
#路径r'.\outmap\go_pla.xlsx'
#data2=data.groupby('学校').count()#人数统计
#data3=data.groupby('省').count()#省统计
'''print(data2)
print('####'*10)
print(data3)
print(data)
'''
def find_stu():
    data = pd.read_excel('go_pla.xlsx')
    str0=input('>>>请输入关键字')
    
    log=[]
    for i in data.values:
        #loc=i[1].find('大学')
        #if str0==i[0] or str0==i[1][0:loc+2] or str0==i[2] or str0==i[3] or str0==i[0][0]:
            #log.append(i)
        str123=''
        for a in i:
            str123+=a
        if str0 in str123:
            log.append(i)
            
        
    if len(log)==0:
        print('>>>未查到该关键字')
    else:
        print('姓名，     学校，     省，     地区')
        for i in log:
            print(i)
#print(find_stu('杭州')[0])

def add_val():
    print('>>>请输入姓名')
    stu_name=input('>>>')
    
    print('>>>请输入大学名称(带上校区),例如：四川大学江安校区/输入‘end’结束输入')
    sch_name=input('>>>')
    if sch_name=='end':
        return '0'
    print('>>>请输入省名称,例如：浙江/输入‘end’结束输入')
    dir_name=input('>>>')
    if dir_name=='end':
        return '0'
        
    print('>>>请输入地区名称，可适当详细,例如：杭州市西湖区或南京市鼓楼区/输入‘end’结束输入')
    dirs_name=input('>>>')
    if dirs_name=='end':
        return '0'
    log=[stu_name,sch_name,dir_name,dirs_name]    #名字，大学，省，地区
    return log


def add_excel():
    #import pandas as pd
    log=add_val()
    if log=='0':
        print('>>>已退出')
        return '0'
    
    else:
        newdata = pd.read_excel('go_pla.xlsx')
        #newdata.loc[len(newdata)]=log
        #print(newdata)
        #newdata = newdata._append(log,ignore_index=True)
        newdata.loc[newdata.shape[0]] = dict(zip(newdata.columns, log))
        newdata.to_excel('go_pla.xlsx', sheet_name='Sheet1', index=False)
        print('添加成功')
#add_excel()        
 
 
def change_excel():
     data4 = pd.read_excel('go_pla.xlsx')
     #newdata=data[['城市','人数']]
     data4=data4.groupby('地区',as_index=False).count()
     newdata=data4[['地区','姓名']]
     newdata.columns = ['地区','人数']
     newdata.to_excel('go_pla_count.xlsx', sheet_name='Sheet1', index=False)
     print(newdata)    
#change_excel()
if __name__=='__main__':
    print('>>>‘毕业，是一场远行的开始’')
    print('>>>欢迎来到whereWEgo去向统计，输入‘help’求助')
    while True :
        try:
            put=input('>>>')
            if put == 'help':
                print('>>>1.‘sr’:输入增加学生去向信息// 2.‘cx’:关键字查询（地区或学校）// 3.‘dt’:显示现有热力地图 // 4.‘gxdt’:更新并显示去向统计热力地图')
                print('>>>输入‘dt’后，若地图未显示请尝试修改默认浏览器或直接用浏览器打开‘out_gomap.html’文件')
            elif put == 'sr':
                add_excel()
            elif put== 'cx':
                find_stu()
            elif put=='gxdt':
                change_excel()
                
                os.system('outmap.exe')
            elif put=='dt':
                os.system('out_gomap.html')
                
            else:
                print('>>>我还不会这条指令哦')
        except :
           print('>>>出现问题，请重试，多次重试仍失败请联系开发者,地图未显示请尝试修改默认浏览器或直接用浏览器打开打开‘out_gomap.html’文件')
           from time import sleep
           sleep(5)
                
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
    