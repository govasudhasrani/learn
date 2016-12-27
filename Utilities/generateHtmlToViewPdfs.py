import sys
import os


def sort_files_based_on_creation_time(directory):
    """
    Sort files based on last modified time of files
    :param directory:
    :return:
    """

    files = [os.path.join(directory, item) for item in os.listdir(directory)]

    files.sort(key=lambda file: os.path.getmtime(file))

    return files

def buildSinglePageView(src_dir, sorted_files):
    objectsHtml = "".join(map(lambda file: "<object width='100%' height='1250px' " \
                                           "type='application/pdf' trusted='yes' " \
                                           "data='file://{0}#zoom=180&view=Fit'> " \
                                           "</object>".format(file), sorted_files))
    htmlDoc = '''
                <!DOCTYPE html>
                <body>
                {0}
                </body>
                </html>
              '''.format(objectsHtml)
    file = os.path.join(src_dir, "pdfViewer.html")
    print "File:>>> " + file
    with open(file, 'w') as fh:
        print htmlDoc
        fh.write(htmlDoc)

def buildNavigationalPage(src_dir, sorted_files):
    srcIndexedFiles = [];
    for index in xrange(0, len(sorted_files)):
        srcIndexedFiles.append(str(index) + ":'" + sorted_files[index] + "'")
    jsFileList = "{" + ",".join(srcIndexedFiles) + "}"
    htmlDoc = '''
<!DOCTYPE html>

<body>
<label>Index -> </label>
<input type="text" id="index" size="4"/>
<button type="button" onclick="goToFile()">GO!</button>
<button type="button" onclick="goNext()">Next</button>
<button type="button" onclick="goPrev()">Prev</button>
<span id="filename"></span>
<div id="content" width="100%" height="100%" style='overflow:auto'>
</div>
<button type="button" onclick="goNext()">Next</button>
<button type="button" onclick="goPrev()">Prev</button>
</body>
<script>
var indexedFiles = ''' + jsFileList + ''';
var currentIdx = 1;

function showContent(fileIdx)
{
	var res = indexedFiles[fileIdx];
    document.getElementById("index").value = fileIdx;
    document.getElementById("filename").innerHTML = res;
    currentIdx = fileIdx;
	document.getElementById("content").innerHTML = "<object id='obj' width='100%' height='600px' style='overflow:auto' type='application/pdf'" +
	"trusted='yes'  data='file://" + res + "#zoom=280&view=Fit,100'></object>"
	document.getElementById("obj").scrollLeft = 300;
	document.getElementById("content").scrollLeft = 300;
	document.getElementById("obj").focus();
}

function goToFile()
{
	var index = document.getElementById('index').value;
    showContent(index);
}

function goNext()
{
	currentIdx++;
    showContent(currentIdx);
}

function goPrev()
{
	currentIdx--;
    showContent(currentIdx);
}

</script>
</html>
       '''
    file = os.path.join(src_dir, "pdfViewer.html")
    print "File generated is: " + file
    with open(file, 'w') as fh:
        print htmlDoc
        fh.write(htmlDoc)

if __name__ == "__main__":
    """
    Usage example:

        Please specify source files directory:
    """

    src_dir = sys.argv[1] if len(sys.argv) else raw_input("Please specify source files directory(cwd:{0}): ".format(os.getcwd()))

    # Sorted files
    sorted_files = sort_files_based_on_creation_time(src_dir)

    #buildSinglePageView(src_dir, sorted_files)
    buildNavigationalPage(src_dir, sorted_files)



















