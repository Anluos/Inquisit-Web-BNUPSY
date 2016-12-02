
work_dir="D:/Iquisit/class/gray/"

f = open('item.txt','w')
for i in range(0,16):
    #f.write('/item = \''+str(i)+'.bmp'+'\'\n')
   f.write('<item pic'+str(i)+'>'+'\n'+'/'+str(i)+'='+'"pic'+str(i)+'.jpg"'+'\n'+'</item>'+'\n')
f.close()

f = open('pic.txt','w')
for i in range(1,16):
    f.write('<picture pic'+str(i)+'>'+'\n'+'/erase = true(0,0,0)'+'\n'+'/position = (38%,50%)'+'\n'+'/items = ("pic'+str(i)+'.jpg")'+'\n'+'</picture>'+'\n')
f.close()

f = open('trail.txt','w')
for i in range(1,16)
   f.write('<trial pic'+str(i)+'>'+'\n'+'/validresponse = (pic01,pic'+str(i)+',pic03,pic04)'+'\n'+'/correctresponse = (pic'+str(i)+')'+'\n'+'/pretrialpause = 500'+'\n'+'/stimulusframes = [1=fixation;100=pic01,pic'+str(i)+',pic03,pic04]'+'\n'+'/correctmessage = (correctmsg,500)'+'\n'+'/errormessage = (errormsg,500)'+'\n'+'</trial>'+'\n')
f.close()
