
# coding: utf-8

# In[1]:


from os.path import isfile, isdir
import csv
import pickle

#读取视频文件
def loadmkv(file):
    import cv2
    cap = cv2.VideoCapture(file +'_front.mkv')
    ret = True
    frame_list = []
    dict = {}
    while(ret == True):
        ret, frame = cap.read()
        if (ret == True):
            frame_list.append(frame)
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #cv2.imshow('frame',gray)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    dict['data']=frame_list
    cap.release()
    cv2.destroyAllWindows()
    
    labels_list = []
    with open(file + '_steering.csv', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            labels_list.append(row['wheel'])
        
    dict['labels']=labels_list
   
    return dict

epochs_path = '/epochs/'
for i in range(1,2):
    filename = epochs_path + 'epoch0' + str(i)
    outputfile = '/output/' + 'epoch0' + str(i)
    if not isfile(filename + '.p'):
        dict = loadmkv(filename)
        pickle.dump((dict['data'], dict['labels']), open(outputfile + '.p', 'wb'))
print('load file completion')





