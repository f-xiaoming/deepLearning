# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:17:53 2019

@author: Auser
"""
from math import log
import operator
import math


def cal_entropy(dataSet_train):  # 计算熵

    # numEntries为训练集样本数
    numEntries = len(dataSet_train)
    labelCounts = {}
    for featVec in dataSet_train:  # 遍历训练样本
        label = featVec[-1]  # 将每个训练样本的类别标签作为类别列表
        if label not in labelCounts.keys():  # 如果一个训练样本的类别不在类别列表字典中
            labelCounts[label] = 0  # 将该训练样本类别进行标记
        labelCounts[label] += 1  # 否则，给类别字典对应的类别+1
    entropy = 0.0  # 初始化香浓商
    for key in labelCounts.keys():  # 遍历类别字典的每个类别
        p_i = float(labelCounts[key] / numEntries)  # 计算每个类别的样本数占总的训练样本数的占比（即某一样本是类i的概率）
        entropy -= p_i * log(p_i, 2)  # log(x,10)表示以10 为底的对数，计算香浓熵
    return entropy


def split_data(dataSet_train, feature_index, value):  # 按照选出的最优的特征的特征值将训练集进行分裂，并将使用过的特征进行删除
    '''
    划分数据集，特征为离散值
    feature_index：用于划分特征的列数，例如“年龄”
    value:划分后的属性值：例如“青少年”
    '''
    data_split = []  # 划分后的数据集
    for feature in dataSet_train:  # 遍历训练集
        if feature[feature_index] == value:  # 如果训练集的特征索引的值等于划分后的属性值
            reFeature = feature[:feature_index]  # 删除使用过的特征
            reFeature = list(reFeature)
            reFeature.extend(feature[feature_index + 1:])
            data_split.append(reFeature)
    return data_split


def split_countinue_data(dataSet_train, feature_index, value, direction):  # 特征为连续值
    data_split = []
    for feature in dataSet_train:
        if feature[feature_index] > value:
            reFeature = feature[:feature_index]
            reFeature = list(reFeature)
            reFeature.extend(feature[feature_index + 1:])
            data_split.append(reFeature)
        else:
            if feature[feature_index] <= value:
                reFeature = feature[:feature_index]
                reFeature = list(reFeature)
                reFeature.extend(feature[feature_index + 1:])
                data_split.append(reFeature)

    return data_split


def choose_best_to_split(dataSet_train):  #

    '''
    根据每个特征的信息增益率，选择最大的划分数据集的索引特征
    '''

    count_feature = len(dataSet_train[0]) - 1  # 特征个数4
    base_entropy = cal_entropy(dataSet_train)  # 原数据初始的信息熵

    max_info_gain_ratio = 0.0  # 信息增益率最大
    split_fea_index = -1  # 信息增益率最大，对应的特征索引号
    # split_fea_value=0#信息增益率最大没对应的特征的特征值
    # split_fea_value=None#特征是连续取值时的最好的划分值
    # c=[]
    for i in range(count_feature):  # 遍历特征
        feature_list = [fe_index[i] for fe_index in dataSet_train]  # 分别获取每每个元组的第i个特征值
        #######################################
        unqval = set(feature_list)  # 去除每一个特征重复的特征值
        Pro_entropy = 0.0  # 初始化条件熵
        split_info = 0.0
        for value in unqval:  # 遍历该特征下的所有属性的唯一值，分别使用每个特征取值划分数据集，计算各个子集的信息熵
            sub_data = split_data(dataSet_train, i, value)  # 将分裂后的数据作为子数据集，递归使用某一特征i的每个特征值来分裂训练集
            pro = len(sub_data) / float(len(dataSet_train))  # 某一训练样本是某一子集的概率，分裂后每一个子集占训练集总数的概率
            Pro_entropy += pro * cal_entropy(sub_data)  # 在某一属性i下的条件熵
            split_info += -pro * log(pro, 2)

        info_gain = base_entropy - Pro_entropy  # 一个训练样本在某一属性下的信息增益
        if (split_info == 0):
            continue
        info_gain_ratio = info_gain / split_info  # 一个训练样本在某一属性下的信息增益率
        # print('增益率')
        # print(info_gain_ratio)
        if (info_gain_ratio > max_info_gain_ratio):  # 选择值最大的信息增益率
            max_info_gain_ratio = info_gain_ratio
            split_fea_index = i
            # split_fea_value=value
            # print('最大增益率')
            # print(max_info_gain_ratio)
    return split_fea_index  # 返回分裂特征值对应的特征索引


##################################################
def most_occur_label(classList):
    # sorted_label_count[0][0]  次数最多的类标签
    label_count = {}  # 创建类别标签字典，key为类别，item为每个类别的样本数
    for label in classList:  # 遍历类列表
        if label not in label_count.keys():  # 如果类标签不在类别标签的字典中
            label_count[label] = 0  # 将该类别标签置为零
        else:
            label_count[label] += 1  # 否则，给对应的类别标签+1
            # 按照类别字典的值排序
    sorted_label_count = sorted(label_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_label_count[0][0]  # 返回样本量最多的类别标签


def build_decesion_tree(dataSet_train, featnames):  # 建立决策树,featLabels存储选择的最优的特征标签
    '''
    字典的键存放节点信息，分支及叶子节点存放值
    '''
    featname = featnames[:]  ################特证名
    classlist = [featvec[-1] for featvec in dataSet_train]  # 此节点的分类情况
    if classlist.count(classlist[0]) == len(classlist):  # 全部属于一类
        return classlist[0]
    if len(dataSet_train[0]) == 1:  # 分完了,没有属性了
        return most_occur_label(classlist)  # 少数服从多数，返回训练样本数最多的类别作为叶节点
    # 选择一个最优特征的最优特征值进行划分
    bestFeat = choose_best_to_split(dataSet_train)
    bestFeatname = featname[bestFeat]
    del (featname[bestFeat])  # 删除已经使用过的特征
    DecisionTree = {bestFeatname: {}}
    # 创建分支,先找出所有属性值,即分支数
    allvalue = [vec[bestFeat] for vec in dataSet_train]  # 将每个训练样本的最优特征值作为分裂时的特征值
    specvalue = sorted(list(set(allvalue)))  # 对分支使有一定顺序
    for v in specvalue:
        copyfeatname = featname[:]  # 复制特证名，在下一轮建造子树时使用
        # 递归建造决策树，split——data()对源数据集进行分裂，
        DecisionTree[bestFeatname][v] = build_decesion_tree(split_data(dataSet_train, bestFeat, v), copyfeatname)

    return DecisionTree


def classify(Tree, featnames, X):  # 对测试集使用训练好的决策树进行分类
    # classLabel=' '
    global classLabel
    root = list(Tree.keys())[0]  # 树的根节点
    firstDict = Tree[root]  # 去除根节点剩余的部分
    featindex = featnames.index(root)  # 根节点特征的下标
    # classLabel='0'
    for key in firstDict.keys():  # 根属性的取值,取哪个就走往哪颗子树（遍历子节点）
        if X[featindex] == key:  # 如果测试样本的特征索引等于key
            if type(firstDict[key]) == type({}):  # 如果有下一层节点
                classLabel = classify(firstDict[key], featnames, X)  # 递归调用分类
            else:  # 否则
                classLabel = firstDict[key]  # 将去除根节点剩余部分的类别给classlabel
    return classLabel


def getCount(Tree, dataSet_train, featnames, count):  # 计算每个叶子结点中正确分类和错误分类的样本数
    root = list(Tree.keys())[0]  # 树根节点
    nextNode = Tree[root]  # 去除根节点剩下的部分
    index = featnames.index(root)  # 获取根节点特征的下标
    # del(featnames[index])#删除使用过的特征
    for key in nextNode.keys():  # 遍历子节点
        rightCount = 0  # 统计每个节点中分类正确的样本数
        wrongCount = 0  # 统计每个节点中分类错误的样本数
        data_split = split_data(dataSet_train, index, key)  # 分裂子数据集
        # 判断是否是叶子结点，不是则迭代进入下一层
        if (isinstance(nextNode[key], dict)):  # 如果有下一层节点
            getCount(nextNode[key], data_split, featnames, count)  # 递归调用getcount函数,获取下一层子节点中的正确和错误数
        else:  # 没有下一层节点
            for i in data_split:  # 遍历训练集的子数据集
                # 判断数组给定的分类是否与叶子结点的值相同
                if (str(i[-1]) == str(nextNode[key])):
                    rightCount += 1  # 分类正确的样本数加一
                else:
                    wrongCount += 1  # 分类错误的样本数加一
            count.append([rightCount, wrongCount])  # 将每个叶子结点中的分类正确和错误的样本数添加到列表中
    return count


def cutBranch(Tree, dataSet_train, featnames):  # 使用悲观剪枝
    root = list(Tree.keys())[0]  # 树的根节点
    # print(root)
    nextNode = Tree[root]  # 除去根节点后剩余的部分
    # print(nextNode)
    index = featnames.index(root)  # 根节点的特征下标
    # print(index)
    newTree = {root: {}}
    for key in nextNode.keys():  # 遍历每个子树
        if (isinstance(nextNode[key], dict)):  # 当子节点不是叶子结点则判断是否是满足剪枝
            data_split = split_data(dataSet_train, index, key)  # 分裂根节点中的数据
            # print(nextNode[key])#第key个子树
            count = []  # 叶子结点列表
            getCount(nextNode[key], data_split, featnames, count)  # 获取每个叶子结点的正确分类数，错误分类数
            # print(count)#每个子树中的叶子结点的分类正确和错误样本数
            allnum = 0  # 整个树的数据的样本总数
            errnum = 0  # 所有叶子节点错误分类的总的样本数
            for i in count:  # 遍历每个叶子结点
                allnum += i[0] + i[1]  # 整个树的数据的样本总数
                errnum += i[1]  # 所有叶子节点错误分类的总的样本数
            if (errnum == 0):  # 当该子树分类时不存在错误，不对其进行剪枝操作#进行下一循环
                newTree[root][key] = nextNode[key]
                #   print(newTree[root][key])
                continue
            # 当子树分类存在错误
            old = errnum + len(count) * 0.5  # 子树的误判数，len（count）为叶子节点数
            # print(old)
            new = errnum + 0.5  # 将子树剪枝后，只剩下根节点的叶节点的误判个数
            # print(new)
            p = old / allnum  # 子树的误判率
            s = math.sqrt(allnum * p * (1 - p))  # 计算标准差
            # print(old-new)
            # print(s)
            if (old - new >= s):  # 当剪枝前的误判率-剪枝后的误判率>=标准差则剪枝
                # 用当前分类是出现最多的类别代替孩子树
                classList = [i[-1] for i in data_split]
                newTree[root][key] = most_occur_label(classList)  # 将数量最多的类别作为叶子结点类别
            #   print(newTree[root][key])

            else:
                # 不满足剪枝则进入子树内部继续进行剪枝操作
                newTree[root][key] = cutBranch(nextNode[key], data_split, featnames)
            #  print('!!!!!!!!!!!!!!')
            # print(newTree[root][key])
        else:  # 否则当子节点是叶子结点
            newTree[root][key] = nextNode[key]
            # print('+++++++++++++++')
            # print(newTree[root][key])
    return newTree


# 计算叶结点数
def getNumLeafs(Tree):
    numLeafs = 0
    firstStr = list(Tree.keys())[0]
    secondDict = Tree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':  # 测试结点的数据类型是否为字典
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


# 计算树的深度
def getTreeDepth(Tree):
    maxDepth = 0
    firstStr = list(Tree.keys())[0]
    secondDict = Tree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':  # 测试结点的数据类型是否为字典
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth


