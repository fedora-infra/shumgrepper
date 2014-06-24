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

def uncommon_files(messages_list):
    '''return uncommon filenames present in packages'''
    final_list = []
    for messages in messages_list:
        sha256_list = []
        for msg in messages:
            sha256_list.append(msg["sha256sum"])
        final_list.append(sha256_list)

    common_sha256 = set(final_list[0]).intersection(*final_list)
    print common_sha256
    for messages in messages_list:
        for sha256 in common_sha256:
            for msg in messages:
                if sha256 == msg["sha256sum"]:
                    messages.remove(msg)

    return messages_list

