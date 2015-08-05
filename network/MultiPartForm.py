import urllib2
import itertools
import mimetools
import mimetypes


class MultiPartForm(object):

    def __init__(self):
        self.files = []
        self.fields = []
        self.boundary = mimetools.choose_boundary().replace('.', '')
        return

    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        self.fields.append((name, value))
        return

    def add_file(self, fieldname, filename, fileHandle, mimetype=None):
        body = fileHandle.read()
        if mimetype is None:
            mimetype = mimetypes.guess_type(filename)[0]\
                or 'application/octet-stream'
        self.files.append((fieldname, filename, mimetype, body))
        return

    def __str__(self):
        # Build a list of lists, each containing "lines" of the
        # request.  Each part is separated by a boundary string.
        # Once the list is built, return a string where each
        # line is separated by '\r\n'.
        # '--' is important .
        parts = []
        part_boundary = '--' + self.boundary

        # Add the form fields
        parts.extend(
            [part_boundary,
             'Content-Disposition: form-data; name="%s"' % name,
             '',
             value,
             ]
            for name, value in self.fields
        )

        # Add the files to upload
        parts.extend(
            [part_boundary,
             'Content-Disposition: file; name="%s"; filename="%s"' % (
                 fieldname, filename),
             'Content-Type: %s' % content_type,
             '',
             body,
             ]
            for fieldname, filename, content_type, body in self.files
        )

        # Flatten the list and add closing boundary marker,
        # then return CR+LF separated data
        flattened = list(itertools.chain(*parts))
        # this line is import, two files and above need it.
        flattened.append('--' + self.boundary + '--')
        flattened.append('')
        result = '\r\n'.join(flattened)
        return result

if __name__ == '__main__':
    # Create the form with simple fields
    form = MultiPartForm()
    form.add_field('contents', 'Doug')
    form.add_field('lastname', 'Hellmann')

    # Add a fake file
    fileHandle = open('/root/Workspaces/python/ad-server/1.jpg')
    form.add_file('biography', '1.jpg', fileHandle)

    content_type = form.get_content_type()
    body = str(form)
    content_length = len(body)

    # Build the request
    request = urllib2.Request('http://192.168.11.237:8090/controller/advertise')
    request.add_header('Content-type', content_type)
    request.add_header('Content-length', content_length)
    request.add_data(body)
    print
    print 'OUTGOING DATA:'
    print request.get_data()
    print
    print 'SERVER RESPONSE:'
    print urllib2.urlopen(request).read()
