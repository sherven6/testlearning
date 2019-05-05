import yaml


def yml_data_with_file():
    with open("./data/message_data.yaml", 'r') as f:
        data = yaml.load(f)
        print(data)


yml_data_with_file()

# data = {'Search_Data': {
#     'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
#     'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
# with open("./text.yaml", "w") as f:  # 在当前目录下生成text.yaml文件，若文件存在直接更新内容
#     yaml.dump(data, f)
