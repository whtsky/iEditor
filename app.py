from bottle import get, run

@get('/')
@get('/<type>')
def hello(type='python'):
    return """
     <style type="text/css">
        #e{position:absolute;top:0;right:0;bottom:0;left:0;}
    </style>
    <div id="e"></div>
    <script src="http://d1n0x3qji82z53.cloudfront.net/src-min-noconflict/ace.js"
     type="text/javascript" charset="utf-8">
    </script>
    <script>
        var e = ace.edit("e");
        e.setTheme("ace/theme/monokai");
        e.getSession().setMode("ace/mode/%s");
    </script>
    """ % type

run(host='127.0.0.1', port=10080, server='tornado')