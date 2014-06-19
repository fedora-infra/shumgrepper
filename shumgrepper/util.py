import json
import flask

def JSONEncoder(messages):
    ''' Serialize collection in each message '''
    msg_list = []
    for message in messages:
        new_dict = dict(
            tar_file = message.tar_file,
            md5sum = message.md5sum,
            sha256sum = message.sha256sum,
            pkg_name = message.pkg_name,
            filename = message.filename,
            tar_sum = message.tar_sum,
            sha1sum = message.sha1sum,
        )
        msg_list.append(new_dict)
    return msg_list

def request_wants_html():
    best = flask.request.accept_mimetypes \
        .best_match(['application/json', 'text/html', 'text/plain'])
    return best == 'text/html'

def common_files(messages_list):
    '''return common filenames present in packages'''
    final_list = []
    for messages in messages_list:
        sha1sum_list = []
        for msg in messages:
            sha1sum_list.append(msg.sha1sum)
        final_list.append(sha1sum_list)

    common_sha1 = set(final_list[0]).intersection(*final_list)
    common_filenames = []
    for sha1sum in common_sha1:
        for msg in messages:
            if sha1sum == msg.sha1sum:
                common_filenames.append(msg.filename)

    return common_filenames

