# coding: utf-8
import tensorflow as tf
import numpy as np


def getResult(picturePath):
    lines = tf.gfile.GFile('output_labels.txt').readlines()
    print(lines)
    uid_to_human = {}
    # 一行一行读取数据
    for uid, line in enumerate(lines):
        # 去掉换行符
        line = line.strip('\n')
        uid_to_human[uid] = line

    def id_to_string(node_id):
        if node_id not in uid_to_human:
            return ''
        return uid_to_human[node_id]

    with tf.gfile.FastGFile('output_graph.pb', 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

    result = ''
    maxScore = 0
    image_data = tf.gfile.FastGFile(picturePath, 'rb').read()
    predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})  # 图片格式是jpg格式
    predictions = np.squeeze(predictions)  # 把结果转为1维数据
    # 排序
    top_k = predictions.argsort()[::-1]
    print(top_k)
    for node_id in top_k:
        # 获取分类名称
        category = id_to_string(node_id)
        # 获取该分类的置信度
        score = predictions[node_id]
        # print('%s (score = %.5f)' % (human_string, score))
        if score > maxScore:
            maxScore = score
            result = category
    return result
