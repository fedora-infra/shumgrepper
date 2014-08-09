def JSONEncoder(messages):
    ''' Serialize collection in each message '''
    msg_list = []
    for message in messages:
        new_dict = dict(
            tarball=message.tarball,
            md5sum=message.md5sum,
            sha256sum=message.sha256sum,
            pkg_name=message.pkg_name,
            filename=message.filename,
            tar_sum=message.tar_sum,
            sha1sum=message.sha1sum,
        )
        msg_list.append(new_dict)
    return msg_list


def to_dict(messages):
    msg_dict = {}
    for message in messages:
        msg_dict[message.sha256sum] = message.filename

    return msg_dict
