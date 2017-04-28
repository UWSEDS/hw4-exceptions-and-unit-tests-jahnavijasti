import os
import urllib


def get_data(url):
    try:
        filename = os.path.basename(url)
        # urllib.urlopen(url)
        if not os.path.exists(filename):
            request = urllib.request.Request(url)
            with urllib.request.urlopen(request) as response:
                csv = response.read()

            with open(os.path.join("/Users/tondapu/analysis", filename), 'wb') as file:
                file.write(csv)
            return('downloading')
        else:
            return('file exists')

    except urllib.error.HTTPError as error:
        return(error.code)

    except urllib.error.URLError as error:
        return(error.code)


def del_data(url):
    filename = os.path.basename(url)
    if os.path.isfile(filename):
        os.remove(filename)
        return('deleted file')
    else:
        return('no file to delete')