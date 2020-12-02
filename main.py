import pathlib
import os
import pprint
import sys


dao_folder = sys.argv[1]
dao_package = sys.argv[2]
dao_class_suffix = sys.argv[3]
repository_package = sys.argv[4]
repository_impl_package = sys.argv[5]

print('dao_folder      : ', dao_folder)
print('dao_package      : ', dao_package)
print('dao_class_suffix      : ', dao_class_suffix)
print('repository_package      : ', repository_package)
print('repository_impl_package      : ', repository_impl_package)


p_dir = pathlib.Path(dao_folder)

print(p_dir)
for dao_path in p_dir.iterdir():
    print(dao_path)
    name = dao_path.stem.rstrip(dao_class_suffix)
    lower_camel_name = name[0].lower() + name[1:]
    print(name)
    print(lower_camel_name)

    with open("./template/RepositoryTemplate.java", encoding="utf-8") as f:
        data_lines = f.read()

    data_lines = data_lines.replace("${repository_impl_package}", repository_impl_package)
    data_lines = data_lines.replace("${dao_package}", dao_package)
    data_lines = data_lines.replace("${repository_package}", repository_package)
    data_lines = data_lines.replace("${name}", name)
    data_lines = data_lines.replace("${lower_camel_name}", lower_camel_name)
    data_lines = data_lines.replace("${dao_class_suffix}", dao_class_suffix)

    # 変換結果を出力
    with open("./output/repository/" + name + "Repository.java", mode="w", encoding="utf-8") as f:
        f.write(data_lines)

    with open("./template/RepositoryImplTemplate.java", encoding="utf-8") as f:
        data_lines = f.read()

    data_lines = data_lines.replace("${repository_impl_package}", repository_impl_package)
    data_lines = data_lines.replace("${dao_package}", dao_package)
    data_lines = data_lines.replace("${repository_package}", repository_package)
    data_lines = data_lines.replace("${name}", name)
    data_lines = data_lines.replace("${lower_camel_name}", lower_camel_name)
    data_lines = data_lines.replace("${dao_class_suffix}", dao_class_suffix)

    # 変換結果を出力
    with open("./output/repository_impl/" + name + "RepositoryImpl.java", mode="w", encoding="utf-8") as f:
        f.write(data_lines)

print("DONE")

