import json
import flask

def JSONEncoder(messages):
    " Serialize collection in each message"
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

