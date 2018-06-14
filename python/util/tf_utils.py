#coding:utf-8
import os
import tensorflow as tf

def get_batch_from_tfrecords(filenames, reader_buffer_size = 2000, shuffle_buffer_size = 200, batch_size = 100, repeat_times = 1):
    dataset = tf.data.TFRecordDataset(filenames,buffer_size=reader_buffer_size)
    dataset = dataset.shuffle(buffer_size=shuffle_buffer_size).repeat(repeat_times).batch(batch_size)
    batch_iter = dataset.make_one_shot_iterator()
    features = tf.parse_example(batch_iter.get_next(),
        features = {
            'qvleft': tf.FixedLenFeature([128], tf.float32),
            'qvright': tf.FixedLenFeature([128], tf.float32)
                    })
    query_batch = features['qvleft']
    doc_batch = features['qvright']
    return [query_batch, doc_batch]

def get_cnn_batch_from_tfrecords(filenames, reader_buffer_size = 2000, shuffle_buffer_size = 200, batch_size = 100, repeat_times = 1):
    dataset = tf.data.TFRecordDataset(filenames, buffer_size=reader_buffer_size).shuffle(buffer_size=shuffle_buffer_size).repeat(repeat_times).batch(batch_size)
    batch_iter = dataset.make_one_shot_iterator()
    features = tf.parse_example(batch_iter.get_next(),
        features = {
            'qvleft': tf.FixedLenFeature([10], tf.int64),
            'qvright': tf.FixedLenFeature([10], tf.int64)
                    })
    query_batch = features['qvleft']
    doc_batch = features['qvright']
    return [query_batch, doc_batch]
    
def get_default_config():
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    config.allow_soft_placement = True
    config.gpu_options.per_process_gpu_memory_fraction = 0.5 
    config.log_device_placement = True
    return config
