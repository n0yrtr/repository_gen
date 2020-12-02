# 概要
doma-genを利用してDaoを生成しているが、
Logicクラスから、直接利用するわけではなく、Repositoryクラスを
腐敗防止層として作成している。

Daoは自動生成されるが、Repositoryインタフェース、RepositoryImplクラスも自動生成させたいためこれを作成。

## 環境
python version 3.8.6

## 使い方
`$python main.py [dao_folder] [dao_package] [dao_class_suffix] [repository_package] [repository_impl_package]`

ex >>>
`$python main.py /Users/n0yrtr/project/src/main/java/com/example/repository/dao com.example.repository.dao Dao com.example.domain.repository com.example.repository.impl`

 outputフォルダーに生成されたファイルができあがるので、プロジェクトに