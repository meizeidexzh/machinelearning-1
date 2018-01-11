
# coding: utf-8

# In[1]:


#读取视频文件
def loadmkv(file):
    import cv2
    import csv
    epochs_path = './epochs/'
    cap = cv2.VideoCapture(epochs_path + file +'_front.mkv')
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
    with open(epochs_path + file + '_steering.csv', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            labels_list.append(row['wheel'])
        
    dict['labels']=labels_list
    return dict

for i in range(1,2):
    dict = loadmkv('epoch0' + str(i))
print(dict['labels'][0])


# In[25]:


def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

dict = unpickle('C:\\machinelearning\\image-classification\\cifar-10-batches-py\\data_batch_1')
print(dict.keys())
print(dict[b'data'][0],dict[b'labels'][0],dict[b'filenames'][0],dict[b'batch_label'][0])
print(dict[b'data'][1],dict[b'labels'][1],dict[b'filenames'][1],dict[b'batch_label'][1])

