import random
import urllib2
import mimetypes


def post(uri, values, files):
    boundary = getBoundary()
    request = urllib2.Request(uri)
    request.add_header(
        'Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    request_data = getFormData(values, files, boundary)
    request.add_data(request_data)
    response = urllib2.urlopen(request)
    response_data = response.read()
    return response_data


def getFormData(dictionary, files, boundary):
    form_boundary = '--' + boundary
    result = []
    for key, value in dictionary.items():
        for e in [
            form_boundary,
            'Content-Disposition: form-data; name="%s"' % key.encode('ascii'),
            '',
            value.encode('ascii')
        ]:
            result.append(e)

    for name, file_name, file_data in files:
        for e in [
            form_boundary,
            'Content-Disposition: form-data; name="%s"; filename="%s"' % (
                name, file_name),
            'Content-Type: %s' % mimetypes.guess_type(
                file_name)[0] or 'application/octet-stream',
            '',
            file_data
        ]:
            result.append(e)

    result.append(form_boundary + '--')
    result.append('')
    request_data = '\r\n'.join(result)
    return request_data


def getBoundary():
    result = ''
    for i in range(30):
        result += str(int(random.random() * 10))

    return result
