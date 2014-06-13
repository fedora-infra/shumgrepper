import json
import flask

def JSONEncoder(message):
    msg_list = []
    for msg in message:
        new_dict = {}
        new_dict['tar_file'] = msg.tar_file
        new_dict['md5sum'] = msg.md5sum
        new_dict['sha256sum'] = msg.sha256sum
        new_dict['pkg_name'] = msg.pkg_name
        new_dict['filename'] = msg.filename
        new_dict['tar_sum'] = msg.tar_sum
        new_dict['sha1sum'] = msg.sha1sum

        msg_list.append(new_dict)
    return msg_list

def request_wants_html():
    best = flask.request.accept_mimetypes \
        .best_match(['application/json', 'text/html', 'text/plain'])
    return best == 'text/html'

