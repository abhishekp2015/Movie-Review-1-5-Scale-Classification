
def convert_file_to_dictionary(file_name):
    f_content = open(file_name, 'r', encoding="latin1")
    f_doc = f_content.read()
    file_data=f_doc.split('\n')
    file_data=file_data[:-1]
    print(file_data)
    new_dict = {}
    new_dict['helpfulness']=float(file_data[0].split(':')[1].strip().split('/')[0])/float(file_data[0].split(':')[1].strip().split('/')[1])
    new_dict['score']=int(float(file_data[1].split(':')[1].strip()))
    new_dict['text']=file_data[2].split(':')[1].strip()
    return new_dict